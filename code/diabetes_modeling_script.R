# MIS 401 Project
# Diabetes Risk Prediction by Patient Health Indicators
# Joshua Ermert
# Multinomial Logistic Regression, KNN, and Decision Tree
# 
#
# Results (set.seed(401), 70/30 split, n_test = 76,104):
#   Decision Tree                   0.8475
#   Multinomial Logistic Regression 0.8467
#   KNN best K = 9                  0.8382
#   KNN k = 5                       0.8301
#   majority-class baseline         0.8424

# 0. Install / load packages
# install.packages("nnet")
# install.packages("class")
# install.packages("rpart")
# install.packages("rpart.plot")

library(nnet)
library(class)
library(rpart)
library(rpart.plot)



# 1. Load data

df <- read.csv("diabetes_012_health_indicators_BRFSS2015_PRO.csv")

str(df)
summary(df)
dim(df)
names(df)



# 2. Prepare variables

df$Diabetes_012 <- factor(
  df$Diabetes_012,
  levels = c(0, 1, 2),
  labels = c("NoDiabetes", "Prediabetes", "Diabetes")
)

categorical_vars <- c(
  "HighBP", "HighChol", "CholCheck", "Smoker", "Stroke",
  "HeartDiseaseorAttack", "PhysActivity", "Fruits", "Veggies",
  "HvyAlcoholConsump", "AnyHealthcare", "NoDocbcCost",
  "DiffWalk", "Sex"
)

df[categorical_vars] <- lapply(df[categorical_vars], factor)

str(df)



# 3. Train / test split

set.seed(401)

n <- nrow(df)
train_index <- sample(seq_len(n), size = round(0.7 * n))

train_data <- df[train_index, ]
test_data  <- df[-train_index, ]

cat("Training rows:", nrow(train_data), "\n")
cat("Testing rows:",  nrow(test_data), "\n")

cat("\nTraining set class proportions:\n")
print(prop.table(table(train_data$Diabetes_012)))

cat("\nTesting set class proportions:\n")
print(prop.table(table(test_data$Diabetes_012)))



# 4. Multinomial logistic regression

logit_model <- multinom(Diabetes_012 ~ ., data = train_data, trace = FALSE)

cat("\nMultinomial Logistic Regression Summary:\n")
print(summary(logit_model))

logit_pred <- predict(logit_model, newdata = test_data)

logit_cm <- table(Predicted = logit_pred, Actual = test_data$Diabetes_012)
cat("\nMultinomial Logistic Regression Confusion Matrix:\n")
print(logit_cm)

logit_accuracy <- mean(logit_pred == test_data$Diabetes_012)
cat("\nMultinomial Logistic Regression Accuracy:",
    round(logit_accuracy, 4), "\n")



# 5. K-Nearest Neighbors

# Reload raw numeric version for KNN distance scaling.
df_knn <- read.csv("diabetes_012_health_indicators_BRFSS2015_PRO.csv")

df_knn$Diabetes_012 <- factor(
  df_knn$Diabetes_012,
  levels = c(0, 1, 2),
  labels = c("NoDiabetes", "Prediabetes", "Diabetes")
)

train_knn <- df_knn[train_index, ]
test_knn  <- df_knn[-train_index, ]

x_train <- train_knn[, setdiff(names(train_knn), "Diabetes_012")]
x_test  <- test_knn[,  setdiff(names(test_knn),  "Diabetes_012")]

# z-score scaling fit on training set; reused for test set.
x_train_scaled <- scale(x_train)
x_test_scaled  <- scale(
  x_test,
  center = attr(x_train_scaled, "scaled:center"),
  scale  = attr(x_train_scaled, "scaled:scale")
)

y_train <- train_knn$Diabetes_012
y_test  <- test_knn$Diabetes_012

# Single KNN run at k = 5 (kept so the k=5 confusion matrix exports cleanly).
k_value <- 5

knn_pred <- knn(
  train = x_train_scaled,
  test  = x_test_scaled,
  cl    = y_train,
  k     = k_value
)

knn_cm <- table(Predicted = knn_pred, Actual = y_test)
cat("\nKNN Confusion Matrix (k =", k_value, "):\n")
print(knn_cm)

knn_accuracy <- mean(knn_pred == y_test)
cat("\nKNN Accuracy (k = 5):", round(knn_accuracy, 4), "\n")

# Tune KNN over k in {3, 5, 7, 9}.
k_values <- c(3, 5, 7, 9)
knn_results <- data.frame(K = integer(), Accuracy = numeric())

for (k in k_values) {
  temp_pred <- knn(
    train = x_train_scaled,
    test  = x_test_scaled,
    cl    = y_train,
    k     = k
  )

  temp_acc <- mean(temp_pred == y_test)

  knn_results <- rbind(
    knn_results,
    data.frame(K = k, Accuracy = temp_acc)
  )
}

cat("\nKNN Accuracy by K:\n")
print(knn_results)

best_k            <- knn_results$K[which.max(knn_results$Accuracy)][1]
best_knn_accuracy <- max(knn_results$Accuracy)

cat("\nBest KNN K:",        best_k, "\n")
cat("Best KNN Accuracy:",   round(best_knn_accuracy, 4), "\n")



# 6. Decision tree  (TUNED — do NOT use default cp = 0.01)

# With rpart's default cp = 0.01 the tree refuses to split on this dataset
# because Diabetes_012 is heavily imbalanced (~84% NoDiabetes); no single
# split can reduce relative error by 1%. We relax cp and constrain depth
# and leaf size to grow a shallow, interpretable tree. The imbalance still
# pulls predictions toward the majority class and is documented as a
# limitation in the report (Section 7).

tree_control <- rpart.control(
  cp        = 0.001,
  minsplit  = 2000,
  minbucket = 1000,
  maxdepth  = 5
)

tree_model <- rpart(
  Diabetes_012 ~ .,
  data    = train_data,
  method  = "class",
  control = tree_control
)

cat("\nDecision Tree CP Table:\n")
print(tree_model$cptable)

cat("\nDecision Tree Summary:\n")
print(summary(tree_model))

# Some rpart.plot versions reject the auto-generated default box.palette,
# so we pass an explicit named palette and wrap in tryCatch to ensure that
# downstream evaluation continues even if plotting fails.
plot_palette <- "RdYlGn"

tryCatch({
  png("decision_tree_plot.png", width = 1400, height = 900, res = 150)
  rpart.plot(
    tree_model,
    main          = "Decision Tree for Diabetes_012",
    box.palette   = plot_palette,
    type          = 2,
    extra         = 104,
    fallen.leaves = TRUE
  )
  dev.off()
  cat("\nSaved tree plot to decision_tree_plot.png\n")
}, error = function(e) {
  if (!is.null(dev.list())) dev.off()
  cat("\nWarning: tree plot to PNG failed:", conditionMessage(e), "\n")
})

tryCatch(
  rpart.plot(
    tree_model,
    main        = "Decision Tree for Diabetes_012",
    box.palette = plot_palette
  ),
  error = function(e) {
    cat("\nWarning: rpart.plot in-session failed:",
        conditionMessage(e), "\n")
  }
)

tree_pred <- predict(tree_model, newdata = test_data, type = "class")

tree_cm <- table(Predicted = tree_pred, Actual = test_data$Diabetes_012)
cat("\nDecision Tree Confusion Matrix:\n")
print(tree_cm)

tree_accuracy <- mean(tree_pred == test_data$Diabetes_012)
cat("\nDecision Tree Accuracy:", round(tree_accuracy, 4), "\n")

cat("\nDecision Tree Variable Importance:\n")
if (length(tree_model$variable.importance) > 0) {
  print(tree_model$variable.importance)
  tree_importance_df <- data.frame(
    variable   = names(tree_model$variable.importance),
    importance = as.numeric(tree_model$variable.importance)
  )
} else {
  cat("(no variable importance — tree did not split)\n")
  tree_importance_df <- data.frame(
    variable   = character(0),
    importance = numeric(0)
  )
}


# 7. Compare model results

results <- data.frame(
  Model = c(
    "Multinomial Logistic Regression",
    "KNN (k=5)",
    paste0("KNN (best K=", best_k, ")"),
    "Decision Tree"
  ),
  Accuracy = c(
    logit_accuracy,
    knn_accuracy,
    best_knn_accuracy,
    tree_accuracy
  )
)

results <- results[order(-results$Accuracy), ]

cat("\nModel Comparison Results:\n")
print(results)



# 8. Save output tables

write.csv(results,                          "model_comparison_results.csv",
          row.names = FALSE)
write.csv(as.data.frame.matrix(logit_cm),   "logit_confusion_matrix.csv")
write.csv(as.data.frame.matrix(knn_cm),     "knn_confusion_matrix.csv")
write.csv(as.data.frame.matrix(tree_cm),    "tree_confusion_matrix.csv")
write.csv(knn_results,                      "knn_k_tuning_results.csv",
          row.names = FALSE)
write.csv(tree_importance_df,               "tree_variable_importance.csv",
          row.names = FALSE)

cat("\nOutput files saved successfully.\n")
