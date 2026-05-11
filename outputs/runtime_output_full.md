Warning message:
package 'rpart.plot' was built under R version 4.5.3 
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
[1] 253680     22
 [1] "Diabetes_012"         "HighBP"               "HighChol"            
 [4] "CholCheck"            "BMI"                  "Smoker"              
 [7] "Stroke"               "HeartDiseaseorAttack" "PhysActivity"        
[10] "Fruits"               "Veggies"              "HvyAlcoholConsump"   
[13] "AnyHealthcare"        "NoDocbcCost"          "GenHlth"             
[16] "MentHlth"             "PhysHlth"             "DiffWalk"            
[19] "Sex"                  "Age"                  "Education"           
[22] "Income"              
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
Training rows: 177576 
Testing rows: 76104 

Training set class proportions:

 NoDiabetes Prediabetes    Diabetes 
 0.84214083  0.01811619  0.13974298 

Testing set class proportions:

 NoDiabetes Prediabetes    Diabetes 
 0.84304373  0.01857984  0.13837643 

Multinomial Logistic Regression Summary:
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

Multinomial Logistic Regression Confusion Matrix:
             Actual
Predicted     NoDiabetes Prediabetes Diabetes
  NoDiabetes       62617        1291     8713
  Prediabetes          0           0        0
  Diabetes          1542         123     1818

Multinomial Logistic Regression Accuracy: 0.8467 

KNN Confusion Matrix (k = 5 ):
             Actual
Predicted     NoDiabetes Prediabetes Diabetes
  NoDiabetes       60860        1201     8183
  Prediabetes         50           2       36
  Diabetes          3249         211     2312

KNN Accuracy: 0.8301 

KNN Accuracy by K:
  K  Accuracy
1 3 0.8160149
2 5 0.8302980
3 7 0.8354357
4 9 0.8382214

Best KNN K: 9 
Best KNN Accuracy: 0.8382 

Decision Tree CP Table:
           CP nsplit rel error   xerror        xstd
1 0.006349886      0 1.0000000 1.000000 0.005481070
2 0.001000000      5 0.9669663 0.966895 0.005406277

Decision Tree Summary:
Call:
rpart(formula = Diabetes_012 ~ ., data = train_data, method = "class", 
    control = tree_control)
  n= 177576 

           CP nsplit rel error   xerror        xstd
1 0.006349886      0 1.0000000 1.000000 0.005481070
2 0.001000000      5 0.9669663 0.966895 0.005406277

Variable importance
              HighBP              GenHlth             HighChol 
                  37                   22                    9 
            DiffWalk                  Age             PhysHlth 
                   8                    7                    6 
                 BMI HeartDiseaseorAttack             MentHlth 
                   5                    4                    2 
              Income 
                   1 

Node number 1: 177576 observations,    complexity param=0.006349886
  predicted class=NoDiabetes  expected loss=0.1578592  P(node) =1
    class counts: 149544  3217 24815
   probabilities: 0.842 0.018 0.140 
  left son=2 (101437 obs) right son=3 (76139 obs)
  Primary splits:
      HighBP   splits as  LR,       improve=3230.629, (0 missing)
      GenHlth  < 2.5  to the left,  improve=3020.446, (0 missing)
      DiffWalk splits as  LR,       improve=2151.912, (0 missing)
      BMI      < 31.5 to the left,  improve=1941.909, (0 missing)
      HighChol splits as  LR,       improve=1904.471, (0 missing)
  Surrogate splits:
      HighChol             splits as  LR,       agree=0.657, adj=0.200, (0 split)
      Age                  < 9.5  to the left,  agree=0.650, adj=0.185, (0 split)
      GenHlth              < 2.5  to the left,  agree=0.635, adj=0.149, (0 split)
      DiffWalk             splits as  LR,       agree=0.630, adj=0.137, (0 split)
      HeartDiseaseorAttack splits as  LR,       agree=0.618, adj=0.110, (0 split)

Node number 2: 101437 observations
  predicted class=NoDiabetes  expected loss=0.07225174  P(node) =0.5712315
    class counts: 94108  1197  6132
   probabilities: 0.928 0.012 0.060 

Node number 3: 76139 observations,    complexity param=0.006349886
  predicted class=NoDiabetes  expected loss=0.2719106  P(node) =0.4287685
    class counts: 55436  2020 18683
   probabilities: 0.728 0.027 0.245 
  left son=6 (55854 obs) right son=7 (20285 obs)
  Primary splits:
      GenHlth  < 3.5  to the left,  improve=1468.4930, (0 missing)
      BMI      < 31.5 to the left,  improve=1075.6200, (0 missing)
      DiffWalk splits as  LR,       improve= 969.0327, (0 missing)
      HighChol splits as  LR,       improve= 659.4215, (0 missing)
      PhysHlth < 7.5  to the left,  improve= 633.1898, (0 missing)
  Surrogate splits:
      PhysHlth  < 14.5 to the left,  agree=0.822, adj=0.331, (0 split)
      DiffWalk  splits as  LR,       agree=0.779, adj=0.171, (0 split)
      MentHlth  < 14.5 to the left,  agree=0.759, adj=0.095, (0 split)
      Income    < 2.5  to the right, agree=0.748, adj=0.053, (0 split)
      Education < 3.5  to the right, agree=0.740, adj=0.022, (0 split)

Node number 6: 55854 observations
  predicted class=NoDiabetes  expected loss=0.2114262  P(node) =0.3145357
    class counts: 44045  1331 10478
   probabilities: 0.789 0.024 0.188 

Node number 7: 20285 observations,    complexity param=0.006349886
  predicted class=NoDiabetes  expected loss=0.4384521  P(node) =0.1142328
    class counts: 11391   689  8205
   probabilities: 0.562 0.034 0.404 
  left son=14 (7056 obs) right son=15 (13229 obs)
  Primary splits:
      BMI                  < 27.5 to the left,  improve=361.91790, (0 missing)
      HighChol             splits as  LR,       improve=204.11970, (0 missing)
      Age                  < 5.5  to the left,  improve= 54.68143, (0 missing)
      HeartDiseaseorAttack splits as  LR,       improve= 50.64040, (0 missing)
      GenHlth              < 4.5  to the left,  improve= 46.34539, (0 missing)
  Surrogate splits:
      Age < 12.5 to the right, agree=0.672, adj=0.056, (0 split)

Node number 14: 7056 observations
  predicted class=NoDiabetes  expected loss=0.3055556  P(node) =0.0397351
    class counts:  4900   187  1969
   probabilities: 0.694 0.027 0.279 

Node number 15: 13229 observations,    complexity param=0.006349886
  predicted class=NoDiabetes  expected loss=0.5093356  P(node) =0.07449768
    class counts:  6491   502  6236
   probabilities: 0.491 0.038 0.471 
  left son=30 (4086 obs) right son=31 (9143 obs)
  Primary splits:
      HighChol             splits as  LR,       improve=139.74500, (0 missing)
      BMI                  < 32.5 to the left,  improve= 79.35715, (0 missing)
      Age                  < 5.5  to the left,  improve= 66.40471, (0 missing)
      GenHlth              < 4.5  to the left,  improve= 51.80742, (0 missing)
      HeartDiseaseorAttack splits as  LR,       improve= 37.42236, (0 missing)
  Surrogate splits:
      Age < 3.5  to the left,  agree=0.694, adj=0.008, (0 split)

Node number 30: 4086 observations
  predicted class=NoDiabetes  expected loss=0.3994126  P(node) =0.02300987
    class counts:  2454   145  1487
   probabilities: 0.601 0.035 0.364 

Node number 31: 9143 observations,    complexity param=0.006349886
  predicted class=Diabetes    expected loss=0.4805862  P(node) =0.05148781
    class counts:  4037   357  4749
   probabilities: 0.442 0.039 0.519 
  left son=62 (5182 obs) right son=63 (3961 obs)
  Primary splits:
      BMI                  < 34.5 to the left,  improve=84.93918, (0 missing)
      GenHlth              < 4.5  to the left,  improve=34.57610, (0 missing)
      DiffWalk             splits as  LR,       improve=18.03747, (0 missing)
      Age                  < 6.5  to the left,  improve=16.68844, (0 missing)
      HeartDiseaseorAttack splits as  LR,       improve=10.90823, (0 missing)
  Surrogate splits:
      Age < 8.5  to the right, agree=0.582, adj=0.035, (0 split)

Node number 62: 5182 observations
  predicted class=NoDiabetes  expected loss=0.4986492  P(node) =0.02918187
    class counts:  2598   200  2384
   probabilities: 0.501 0.039 0.460 

Node number 63: 3961 observations
  predicted class=Diabetes    expected loss=0.4029286  P(node) =0.02230594
    class counts:  1439   157  2365
   probabilities: 0.363 0.040 0.597 

n= 177576 

node), split, n, loss, yval, (yprob)
      * denotes terminal node

 1) root 177576 28032 NoDiabetes (0.84214083 0.01811619 0.13974298)  
   2) HighBP=0 101437  7329 NoDiabetes (0.92774826 0.01180043 0.06045131) *
   3) HighBP=1 76139 20703 NoDiabetes (0.72808942 0.02653042 0.24538016)  
     6) GenHlth< 3.5 55854 11809 NoDiabetes (0.78857378 0.02382999 0.18759623) *
     7) GenHlth>=3.5 20285  8894 NoDiabetes (0.56154794 0.03396598 0.40448607)  
      14) BMI< 27.5 7056  2156 NoDiabetes (0.69444444 0.02650227 0.27905329) *
      15) BMI>=27.5 13229  6738 NoDiabetes (0.49066445 0.03794693 0.47138862)  
        30) HighChol=0 4086  1632 NoDiabetes (0.60058737 0.03548703 0.36392560) *
        31) HighChol=1 9143  4394 Diabetes (0.44153998 0.03904626 0.51941376)  
          62) BMI< 34.5 5182  2584 NoDiabetes (0.50135083 0.03859514 0.46005403) *
          63) BMI>=34.5 3961  1596 Diabetes (0.36329210 0.03963646 0.59707145) *

Saved tree plot to decision_tree_plot.png

Decision Tree Confusion Matrix:
             Actual
Predicted     NoDiabetes Prediabetes Diabetes
  NoDiabetes       63541        1358     9572
  Prediabetes          0           0        0
  Diabetes           618          56      959

Decision Tree Accuracy: 0.8475 

Decision Tree Variable Importance:
              HighBP              GenHlth             HighChol 
          3230.62925           1950.59018            786.68555 
            DiffWalk                  Age             PhysHlth 
           694.54691            621.65426            485.46773 
                 BMI HeartDiseaseorAttack             MentHlth 
           446.85712            354.33858            139.79096 
              Income            Education 
            77.75013             32.79405 

Model Comparison Results:
                            Model  Accuracy
4                   Decision Tree 0.8475244
1 Multinomial Logistic Regression 0.8466703
3                    KNN (best K) 0.8382214
2                       KNN (k=5) 0.8301009

Output files saved successfully.

Interpretation prompts:
- Which model had the highest overall accuracy?
- Did all models struggle with Prediabetes because of class imbalance?
- Which predictors appear most important in the decision tree?
- Are the strongest EDA findings reflected in the model results?
