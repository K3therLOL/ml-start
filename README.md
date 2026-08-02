## Chosen dataset
Obesity constitutes a **significant global public health burden**, associated with elevated risk of *cardiovascular disease*, *type 2 diabetes*, and *psychological comorbidities*, with prevalence rates continuing to rise worldwide every year. Identifying the behavioral and physiological determinants of obesity is therefore critical for developing effective prevention and medical intervention strategies.

This dataset was selected as it provides a multivariate representation of *eating and drinking habits*, *physical activity levels*, and *demographic characteristics* across individuals from **Mexico, Peru, and Colombia**, enabling systematic investigation of the factors associated with obesity and supporting the development of classification models across seven weight status categories.

## Hypotheses

1. Decision Tree will outperform Logistic Regression, because the boundaries between adjacent obesity classes (Normal_Weight, Overweight_Level_I, Overweight_Level_II) depend on non-linear interactions between features like Weight, Height, and lifestyle variable
2. F1-macro rankings of hardest classes will match between Logistic Regression and Decision Tree, since class difficulty comes from label ambiguity, not model choice.
3. Weight and Height will be the most important features according to the feature importance of the Decision Tree.
4. Removing outliers (values beyond 1.5 × IQR) from Age, Weight, and NCP will improve the F1-macro score of both Logistic Regression and Decision Tree compared to using the original data with outliers.
5. Applying L1 regularization to Logistic Regression will decrease F1-macro compared to the unregularized Logistic Regression by reducing the influence of more important features.
