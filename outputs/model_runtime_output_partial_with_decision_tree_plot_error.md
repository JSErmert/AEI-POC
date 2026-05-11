> library(nnet)
> library(class)
> library(rpart)
> library(rpart.plot)
Warning message:
package ‘rpart.plot’ was built under R version 4.5.3 

> # -------------------------
> # 1. Load data
> # -------------------------
> df <- read.csv("diabetes_012_health_indicators_BRFSS2015_PRO.csv")
Error in file(file, "rt") : cannot open the connection
In addition: Warning message:
In file(file, "rt") :
  cannot open file 'diabetes_012_health_indicators_BRFSS2015_PRO.csv': No such file or directory

> setwd("C:/Users/JSEer/OneDrive/Desktop/SDSU Spring 2026/MIS401.Ermert.Joshua/Project (Prototype)")
> library(nnet)
> library(class)
> library(rpart)
> library(rpart.plot)
> # -------------------------
> # 1. Load data
> # -------------------------
> df <- read.csv("diabetes_012_health_indicators_BRFSS2015_PRO.csv")
> # Basic inspection
> str(df)
'data.frame':	253680 obs. of  22 variables:
 $ Diabetes_012        : int  0 0 0 0 0 0 0 0 2 0 ...
 $ HighBP              : int  1 0 1 1 1 1 1 1 1 0 ...
 $ HighChol            : int  1 0 1 0 1 1 0 1 1 0 ...
 $ CholCheck           : int  1 0 1 1 1 1 1 1 1 1 ...
 $ BMI                 : int  40 25 28 27 24 25 30 25 30 24 ...
 $ Smoker              : int  1 1 0 0 0 1 1 1 1 0 ...
 $ Stroke              : int  0 0 0 0 0 0 0 0 0 0 ...
 $ HeartDiseaseorAttack: int  0 0 0 0 0 0 0 0 1 0 ...
 $ PhysActivity        : int  0 1 0 1 1 1 0 1 0 0 ...
 $ Fruits              : int  0 0 1 1 1 1 0 0 1 0 ...
 $ Veggies             : int  1 0 0 1 1 1 0 1 1 1 ...
 $ HvyAlcoholConsump   : int  0 0 0 0 0 0 0 0 0 0 ...
 $ AnyHealthcare       : int  1 0 1 1 1 1 1 1 1 1 ...
 $ NoDocbcCost         : int  0 1 1 0 0 0 0 0 0 0 ...
 $ GenHlth             : int  5 3 5 2 2 2 3 3 5 2 ...
 $ MentHlth            : int  18 0 30 0 3 0 0 0 30 0 ...
 $ PhysHlth            : int  15 0 30 0 0 2 14 0 30 0 ...
 $ DiffWalk            : int  1 0 1 0 0 0 0 1 1 0 ...
 $ Sex                 : int  0 0 0 0 0 1 0 0 0 1 ...
 $ Age                 : int  9 7 9 11 11 10 9 11 9 8 ...
 $ Education           : int  4 6 4 3 5 6 6 4 5 4 ...
 $ Income              : int  3 1 8 6 4 8 7 4 1 3 ...
> summary(df)
  Diabetes_012        HighBP         HighChol        CholCheck     
 Min.   :0.0000   Min.   :0.000   Min.   :0.0000   Min.   :0.0000  
 1st Qu.:0.0000   1st Qu.:0.000   1st Qu.:0.0000   1st Qu.:1.0000  
 Median :0.0000   Median :0.000   Median :0.0000   Median :1.0000  
 Mean   :0.2969   Mean   :0.429   Mean   :0.4241   Mean   :0.9627  
 3rd Qu.:0.0000   3rd Qu.:1.000   3rd Qu.:1.0000   3rd Qu.:1.0000  
 Max.   :2.0000   Max.   :1.000   Max.   :1.0000   Max.   :1.0000  
      BMI            Smoker           Stroke        HeartDiseaseorAttack
 Min.   :12.00   Min.   :0.0000   Min.   :0.00000   Min.   :0.00000     
 1st Qu.:24.00   1st Qu.:0.0000   1st Qu.:0.00000   1st Qu.:0.00000     
 Median :27.00   Median :0.0000   Median :0.00000   Median :0.00000     
 Mean   :28.38   Mean   :0.4432   Mean   :0.04057   Mean   :0.09419     
 3rd Qu.:31.00   3rd Qu.:1.0000   3rd Qu.:0.00000   3rd Qu.:0.00000     
 Max.   :98.00   Max.   :1.0000   Max.   :1.00000   Max.   :1.00000     
  PhysActivity        Fruits          Veggies       HvyAlcoholConsump
 Min.   :0.0000   Min.   :0.0000   Min.   :0.0000   Min.   :0.0000   
 1st Qu.:1.0000   1st Qu.:0.0000   1st Qu.:1.0000   1st Qu.:0.0000   
 Median :1.0000   Median :1.0000   Median :1.0000   Median :0.0000   
 Mean   :0.7565   Mean   :0.6343   Mean   :0.8114   Mean   :0.0562   
 3rd Qu.:1.0000   3rd Qu.:1.0000   3rd Qu.:1.0000   3rd Qu.:0.0000   
 Max.   :1.0000   Max.   :1.0000   Max.   :1.0000   Max.   :1.0000   
 AnyHealthcare     NoDocbcCost         GenHlth         MentHlth     
 Min.   :0.0000   Min.   :0.00000   Min.   :1.000   Min.   : 0.000  
 1st Qu.:1.0000   1st Qu.:0.00000   1st Qu.:2.000   1st Qu.: 0.000  
 Median :1.0000   Median :0.00000   Median :2.000   Median : 0.000  
 Mean   :0.9511   Mean   :0.08418   Mean   :2.511   Mean   : 3.185  
 3rd Qu.:1.0000   3rd Qu.:0.00000   3rd Qu.:3.000   3rd Qu.: 2.000  
 Max.   :1.0000   Max.   :1.00000   Max.   :5.000   Max.   :30.000  
    PhysHlth         DiffWalk           Sex              Age        
 Min.   : 0.000   Min.   :0.0000   Min.   :0.0000   Min.   : 1.000  
 1st Qu.: 0.000   1st Qu.:0.0000   1st Qu.:0.0000   1st Qu.: 6.000  
 Median : 0.000   Median :0.0000   Median :0.0000   Median : 8.000  
 Mean   : 4.242   Mean   :0.1682   Mean   :0.4403   Mean   : 8.032  
 3rd Qu.: 3.000   3rd Qu.:0.0000   3rd Qu.:1.0000   3rd Qu.:10.000  
 Max.   :30.000   Max.   :1.0000   Max.   :1.0000   Max.   :13.000  
   Education        Income     
 Min.   :1.00   Min.   :1.000  
 1st Qu.:4.00   1st Qu.:5.000  
 Median :5.00   Median :7.000  
 Mean   :5.05   Mean   :6.054  
 3rd Qu.:6.00   3rd Qu.:8.000  
 Max.   :6.00   Max.   :8.000  
> dim(df)
[1] 253680     22
> names(df)
 [1] "Diabetes_012"         "HighBP"               "HighChol"            
 [4] "CholCheck"            "BMI"                  "Smoker"              
 [7] "Stroke"               "HeartDiseaseorAttack" "PhysActivity"        
[10] "Fruits"               "Veggies"              "HvyAlcoholConsump"   
[13] "AnyHealthcare"        "NoDocbcCost"          "GenHlth"             
[16] "MentHlth"             "PhysHlth"             "DiffWalk"            
[19] "Sex"                  "Age"                  "Education"           
[22] "Income"              
> # -------------------------
> # 2. Prepare variables
> # -------------------------
> # Convert response variable to factor with readable labels
> df$Diabetes_012 <- factor(
+   df$Diabetes_012,
+   levels = c(0, 1, 2),
+   labels = c("NoDiabetes", "Prediabetes", "Diabetes")
+ )
> # Convert binary/categorical predictors to factors
> categorical_vars <- c(
+   "HighBP", "HighChol", "CholCheck", "Smoker", "Stroke",
+   "HeartDiseaseorAttack", "PhysActivity", "Fruits", "Veggies",
+   "HvyAlcoholConsump", "AnyHealthcare", "NoDocbcCost",
+   "DiffWalk", "Sex"
+ )
> df[categorical_vars] <- lapply(df[categorical_vars], factor)
> # Confirm structure after conversion
> str(df)
'data.frame':	253680 obs. of  22 variables:
 $ Diabetes_012        : Factor w/ 3 levels "NoDiabetes","Prediabetes",..: 1 1 1 1 1 1 1 1 3 1 ...
 $ HighBP              : Factor w/ 2 levels "0","1": 2 1 2 2 2 2 2 2 2 1 ...
 $ HighChol            : Factor w/ 2 levels "0","1": 2 1 2 1 2 2 1 2 2 1 ...
 $ CholCheck           : Factor w/ 2 levels "0","1": 2 1 2 2 2 2 2 2 2 2 ...
 $ BMI                 : int  40 25 28 27 24 25 30 25 30 24 ...
 $ Smoker              : Factor w/ 2 levels "0","1": 2 2 1 1 1 2 2 2 2 1 ...
 $ Stroke              : Factor w/ 2 levels "0","1": 1 1 1 1 1 1 1 1 1 1 ...
 $ HeartDiseaseorAttack: Factor w/ 2 levels "0","1": 1 1 1 1 1 1 1 1 2 1 ...
 $ PhysActivity        : Factor w/ 2 levels "0","1": 1 2 1 2 2 2 1 2 1 1 ...
 $ Fruits              : Factor w/ 2 levels "0","1": 1 1 2 2 2 2 1 1 2 1 ...
 $ Veggies             : Factor w/ 2 levels "0","1": 2 1 1 2 2 2 1 2 2 2 ...
 $ HvyAlcoholConsump   : Factor w/ 2 levels "0","1": 1 1 1 1 1 1 1 1 1 1 ...
 $ AnyHealthcare       : Factor w/ 2 levels "0","1": 2 1 2 2 2 2 2 2 2 2 ...
 $ NoDocbcCost         : Factor w/ 2 levels "0","1": 1 2 2 1 1 1 1 1 1 1 ...
 $ GenHlth             : int  5 3 5 2 2 2 3 3 5 2 ...
 $ MentHlth            : int  18 0 30 0 3 0 0 0 30 0 ...
 $ PhysHlth            : int  15 0 30 0 0 2 14 0 30 0 ...
 $ DiffWalk            : Factor w/ 2 levels "0","1": 2 1 2 1 1 1 1 2 2 1 ...
 $ Sex                 : Factor w/ 2 levels "0","1": 1 1 1 1 1 2 1 1 1 2 ...
 $ Age                 : int  9 7 9 11 11 10 9 11 9 8 ...
 $ Education           : int  4 6 4 3 5 6 6 4 5 4 ...
 $ Income              : int  3 1 8 6 4 8 7 4 1 3 ...
> # -------------------------
> # 3. Train/test split
> # -------------------------
> set.seed(401)
> n <- nrow(df)
> train_index <- sample(seq_len(n), size = round(0.7 * n))
> train_data <- df[train_index, ]
> test_data  <- df[-train_index, ]
> cat("Training rows:", nrow(train_data), "\n")
Training rows: 177576 
> cat("Testing rows:", nrow(test_data), "\n")
Testing rows: 76104 
> # Check class proportions
> cat("\nTraining set class proportions:\n")

Training set class proportions:
> print(prop.table(table(train_data$Diabetes_012)))

 NoDiabetes Prediabetes    Diabetes 
 0.84214083  0.01811619  0.13974298 
> cat("\nTesting set class proportions:\n")

Testing set class proportions:
> print(prop.table(table(test_data$Diabetes_012)))

 NoDiabetes Prediabetes    Diabetes 
 0.84304373  0.01857984  0.13837643 
> # -------------------------
> # 4. Multinomial logistic regression
> # -------------------------
> logit_model <- multinom(Diabetes_012 ~ ., data = train_data, trace = FALSE)
> cat("\nMultinomial Logistic Regression Summary:\n")

Multinomial Logistic Regression Summary:
> print(summary(logit_model))
Call:
multinom(formula = Diabetes_012 ~ ., data = train_data, trace = FALSE)

Coefficients:
            (Intercept)   HighBP1 HighChol1 CholCheck1        BMI     Smoker1
Prediabetes   -7.668424 0.3817433 0.5034012  0.8490401 0.05146440 -0.02564118
Diabetes      -7.910139 0.7699226 0.5976581  1.2746681 0.06349212 -0.01500115
               Stroke1 HeartDiseaseorAttack1 PhysActivity1     Fruits1
Prediabetes -0.1449180           -0.02075913  -0.009596978 -0.03284304
Diabetes     0.1460733            0.22380839  -0.060090214 -0.04526214
               Veggies1 HvyAlcoholConsump1 AnyHealthcare1 NoDocbcCost1
Prediabetes -0.03676043         -0.2346309     -0.1416974   0.38528972
Diabetes    -0.03658928         -0.7851043      0.0388253   0.07022695
              GenHlth     MentHlth     PhysHlth   DiffWalk1      Sex1       Age
Prediabetes 0.3020645  0.006520458 -0.005467132 -0.01581085 0.1276495 0.1320894
Diabetes    0.5439943 -0.003425725 -0.007458639  0.11073545 0.2612589 0.1286757
              Education      Income
Prediabetes -0.08529258 -0.05435818
Diabetes    -0.03854624 -0.05107703

Std. Errors:
            (Intercept)    HighBP1  HighChol1 CholCheck1         BMI    Smoker1
Prediabetes   0.2281767 0.04036445 0.03835793 0.15607263 0.002389509 0.03720708
Diabetes      0.1123987 0.01765646 0.01627883 0.08261664 0.001087317 0.01583099
               Stroke1 HeartDiseaseorAttack1 PhysActivity1    Fruits1
Prediabetes 0.08161571            0.05512099    0.04143084 0.03876008
Diabetes    0.03014041            0.02141503    0.01733481 0.01643137
              Veggies1 HvyAlcoholConsump1 AnyHealthcare1 NoDocbcCost1
Prediabetes 0.04521478         0.08997905     0.08324695   0.05887871
Diabetes    0.01909715         0.04643200     0.03990806   0.02754572
                GenHlth    MentHlth    PhysHlth  DiffWalk1       Sex1
Prediabetes 0.022463576 0.002331714 0.002286984 0.04984909 0.03792266
Diabetes    0.009745425 0.001030747 0.000942777 0.02042018 0.01613569
                    Age   Education      Income
Prediabetes 0.007761060 0.019480108 0.010078429
Diabetes    0.003361834 0.008357953 0.004280948

Residual Deviance: 142377.2 
AIC: 142465.2 
> logit_pred <- predict(logit_model, newdata = test_data)
> logit_cm <- table(Predicted = logit_pred, Actual = test_data$Diabetes_012)
> cat("\nMultinomial Logistic Regression Confusion Matrix:\n")

Multinomial Logistic Regression Confusion Matrix:
> print(logit_cm)
             Actual
Predicted     NoDiabetes Prediabetes Diabetes
  NoDiabetes       62617        1291     8713
  Prediabetes          0           0        0
  Diabetes          1542         123     1818
> logit_accuracy <- mean(logit_pred == test_data$Diabetes_012)
> cat("\nMultinomial Logistic Regression Accuracy:", round(logit_accuracy, 4), "\n")

Multinomial Logistic Regression Accuracy: 0.8467 
> # -------------------------
> # 5. K-Nearest Neighbors
> # -------------------------
> # Reload raw numeric version for easier KNN scaling
> df_knn <- read.csv("diabetes_012_health_indicators_BRFSS2015_PRO.csv")
> # Convert response variable to factor
> df_knn$Diabetes_012 <- factor(
+   df_knn$Diabetes_012,
+   levels = c(0, 1, 2),
+   labels = c("NoDiabetes", "Prediabetes", "Diabetes")
+ )
> train_knn <- df_knn[train_index, ]
> test_knn  <- df_knn[-train_index, ]
> x_train <- train_knn[, setdiff(names(train_knn), "Diabetes_012")]
> x_test  <- test_knn[, setdiff(names(test_knn), "Diabetes_012")]
> # Scale predictors using training set parameters
> x_train_scaled <- scale(x_train)
> x_test_scaled <- scale(
+   x_test,
+   center = attr(x_train_scaled, "scaled:center"),
+   scale  = attr(x_train_scaled, "scaled:scale")
+ )
> y_train <- train_knn$Diabetes_012
> y_test  <- test_knn$Diabetes_012
> # Initial KNN model
> k_value <- 5
> knn_pred <- knn(
+   train = x_train_scaled,
+   test = x_test_scaled,
+   cl = y_train,
+   k = k_value
+ )
> knn_cm <- table(Predicted = knn_pred, Actual = y_test)
> cat("\nKNN Confusion Matrix (k =", k_value, "):\n")

KNN Confusion Matrix (k = 5 ):
> print(knn_cm)
             Actual
Predicted     NoDiabetes Prediabetes Diabetes
  NoDiabetes       60860        1201     8183
  Prediabetes         50           2       36
  Diabetes          3249         211     2312
> knn_accuracy <- mean(knn_pred == y_test)
> cat("\nKNN Accuracy:", round(knn_accuracy, 4), "\n")

KNN Accuracy: 0.8301 
> # Tune KNN using several k values
> k_values <- c(3, 5, 7, 9)
> knn_results <- data.frame(K = integer(), Accuracy = numeric())
> for (k in k_values) {
+   temp_pred <- knn(
+     train = x_train_scaled,
+     test = x_test_scaled,
+     cl = y_train,
+     k = k
+   )
+   
+   temp_acc <- mean(temp_pred == y_test)
+   
+   knn_results <- rbind(
+     knn_results,
+     data.frame(K = k, Accuracy = temp_acc)
+   )
+ }
> cat("\nKNN Accuracy by K:\n")

KNN Accuracy by K:
> print(knn_results)
  K  Accuracy
1 3 0.8160149
2 5 0.8302980
3 7 0.8354357
4 9 0.8382214
> best_k <- knn_results$K[which.max(knn_results$Accuracy)][1]
> best_knn_accuracy <- max(knn_results$Accuracy)
> cat("\nBest KNN K:", best_k, "\n")

Best KNN K: 9 
> cat("Best KNN Accuracy:", round(best_knn_accuracy, 4), "\n")
Best KNN Accuracy: 0.8382 
> # -------------------------
> # 6. Decision tree
> # -------------------------
> tree_model <- rpart(Diabetes_012 ~ ., data = train_data, method = "class")
> cat("\nDecision Tree Summary:\n")

Decision Tree Summary:
> print(summary(tree_model))
Call:
rpart(formula = Diabetes_012 ~ ., data = train_data, method = "class")
  n= 177576 

  CP nsplit rel error xerror xstd
1  0      0         1      0    0

Node number 1: 177576 observations
  predicted class=NoDiabetes  expected loss=0.1578592  P(node) =1
    class counts: 149544  3217 24815
   probabilities: 0.842 0.018 0.140 

n= 177576 

node), split, n, loss, yval, (yprob)
      * denotes terminal node

1) root 177576 28032 NoDiabetes (0.84214083 0.01811619 0.13974298) *
> # Plot the tree
> rpart.plot(tree_model, main = "Decision Tree for Diabetes_012")
Error: box.palette: c("#F7FCF5", "#EEF8EA", "#E5F5E0", "#D6EFD0", "#C7E9C0", "#B4E1AD", "#A1D99B", "#8ACE88", "#74C476") is neither a color nor a palette.
Try something like box.palette="blue" or box.palette="Blues".
The predefined palettes are (with an optional "-" prefix):
  Grays Greys Greens Blues Browns Oranges Reds Purples
  Gy Gn Bu Bn Or Rd Pu (alternative names for the above palettes)
  BuGn BuBn GnRd etc.  (two-color diverging palettes: any combination of two palettes)
  RdYlGn GnYlRd BlGnYl YlGnBl (three color palettes)

> cat("\nDecision Tree Confusion Matrix:\n")

Decision Tree Confusion Matrix:
> print(tree_cm)
Error: object 'tree_cm' not found

> tree_accuracy <- mean(tree_pred == test_data$Diabetes_012)
Error: object 'tree_pred' not found

> cat("\nDecision Tree Accuracy:", round(tree_accuracy, 4), "\n")
Error: object 'tree_accuracy' not found

> # Variable importance
> cat("\nDecision Tree Variable Importance:\n")

Decision Tree Variable Importance:
> print(tree_model$variable.importance)
NULL
> # -------------------------
> # 7. Compare model results
> # -------------------------
> results <- data.frame(
+   Model = c("Multinomial Logistic Regression", "KNN (k=5)", "KNN (best K)", "Decision Tree"),
+   Accuracy = c(logit_accuracy, knn_accuracy, best_knn_accuracy, tree_accuracy)
+ )
Error: object 'tree_accuracy' not found

> results <- results[order(-results$Accuracy), ]
Error: object 'results' not found

> cat("\nModel Comparison Results:\n")

Model Comparison Results:
> print(results)
Error: object 'results' not found

> # -------------------------
> # 8. Save output tables
> # -------------------------
> write.csv(results, "model_comparison_results.csv", row.names = FALSE)
Error in eval(expr, p) : object 'results' not found

> write.csv(as.data.frame.matrix(logit_cm), "logit_confusion_matrix.csv")
> write.csv(as.data.frame.matrix(knn_cm), "knn_confusion_matrix.csv")
> write.csv(as.data.frame.matrix(tree_cm), "tree_confusion_matrix.csv")
Error in eval(expr, p) : object 'tree_cm' not found

> write.csv(knn_results, "knn_k_tuning_results.csv", row.names = FALSE)
> cat("\nOutput files saved successfully.\n")

Output files saved successfully.
> # -------------------------
> # 9. Quick interpretation prompts
> # -------------------------
> cat("\nInterpretation prompts:\n")

Interpretation prompts:
> cat("- Which model had the highest overall accuracy?\n")
- Which model had the highest overall accuracy?
> cat("- Did all models struggle with Prediabetes because of class imbalance?\n")
- Did all models struggle with Prediabetes because of class imbalance?
> cat("- Which predictors appear most important in the decision tree?\n")
- Which predictors appear most important in the decision tree?
> cat("- Are the strongest EDA findings reflected in the model results?\n")
- Are the strongest EDA findings reflected in the model results?