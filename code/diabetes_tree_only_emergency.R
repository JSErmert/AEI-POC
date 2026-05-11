# =========================================================
# EMERGENCY FALLBACK SCRIPT
# Runs ONLY the decision tree section using the same seed and
# split as the main script, so tree evidence can be produced
# without waiting on KNN tuning.
# =========================================================

library(rpart)
library(rpart.plot)

df <- read.csv("diabetes_012_health_indicators_BRFSS2015_PRO.csv")

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

set.seed(401)
n <- nrow(df)
train_index <- sample(seq_len(n), size = round(0.7 * n))
train_data <- df[train_index, ]
test_data  <- df[-train_index, ]

tree_control <- rpart.control(
  cp = 0.001,
  minsplit = 2000,
  minbucket = 1000,
  maxdepth = 5
)

tree_model <- rpart(
  Diabetes_012 ~ .,
  data = train_data,
  method = "class",
  control = tree_control
)

cat("\nDecision Tree CP Table:\n")
print(tree_model$cptable)

cat("\nDecision Tree Summary:\n")
print(summary(tree_model))

plot_palette <- "RdYlGn"

tryCatch({
  png("decision_tree_plot.png", width = 1400, height = 900, res = 150)
  rpart.plot(
    tree_model,
    main = "Decision Tree for Diabetes_012",
    box.palette = plot_palette,
    type = 2,
    extra = 104,
    fallen.leaves = TRUE
  )
  dev.off()
  cat("\nSaved decision_tree_plot.png\n")
}, error = function(e) {
  if (!is.null(dev.list())) dev.off()
  cat("\nWarning: tree plot to PNG failed:", conditionMessage(e), "\n")
})

tree_pred <- predict(tree_model, newdata = test_data, type = "class")
tree_cm <- table(Predicted = tree_pred, Actual = test_data$Diabetes_012)
cat("\nDecision Tree Confusion Matrix:\n")
print(tree_cm)

tree_accuracy <- mean(tree_pred == test_data$Diabetes_012)
cat("\nDecision Tree Accuracy:", round(tree_accuracy, 4), "\n")

cat("\nDecision Tree Variable Importance:\n")
if (length(tree_model$variable.importance) > 0) {
  print(tree_model$variable.importance)
} else {
  cat("(no variable importance — tree did not split)\n")
}

write.csv(as.data.frame.matrix(tree_cm), "tree_confusion_matrix.csv")

# Build comparison table from existing logit + KNN tuning CSVs
knn_results <- read.csv("knn_k_tuning_results.csv")
best_k <- knn_results$K[which.max(knn_results$Accuracy)][1]
best_knn_accuracy <- max(knn_results$Accuracy)
knn_k5_accuracy <- knn_results$Accuracy[knn_results$K == 5]
logit_accuracy <- 0.8467  # from prior validated run, see runtime_output_full.md

results <- data.frame(
  Model = c(
    "Multinomial Logistic Regression",
    "KNN (k=5)",
    paste0("KNN (best K=", best_k, ")"),
    "Decision Tree"
  ),
  Accuracy = c(logit_accuracy, knn_k5_accuracy, best_knn_accuracy, tree_accuracy)
)
results <- results[order(-results$Accuracy), ]

cat("\nModel Comparison Results:\n")
print(results)
write.csv(results, "model_comparison_results.csv", row.names = FALSE)
cat("\nEmergency tree-only run complete.\n")
