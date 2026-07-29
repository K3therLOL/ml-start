## Chosen dataset
Obesity constitutes a **significant global public health burden**, associated with elevated risk of *cardiovascular disease*, *type 2 diabetes*, and *psychological comorbidities*, with prevalence rates continuing to rise worldwide every year. Identifying the behavioral and physiological determinants of obesity is therefore critical for developing effective prevention and medical intervention strategies.

This dataset was selected as it provides a multivariate representation of *eating and drinking habits*, *physical activity levels*, and *demographic characteristics* across individuals from **Mexico, Peru, and Colombia**, enabling systematic investigation of the factors associated with obesity and supporting the development of classification models across seven weight status categories.

## Hypotheses

1. Logistic Regression will perform worse than a Decision Tree because of SCC class disbalance.
2. F1-macro will be noticeably lower than accuracy for both Logistic Regression and Decision Tree due to class imbalance (especially Insufficient_Weight and Obesity_Type_III).
3. Weight and Height will be the most important features according to the feature importance of the Decision Tree.
4. When the maximum depth of the Decision Tree exceeds 8, overfitting will occur: train accuracy will increase while test accuracy will decrease.
5. Applying L1 regularization (Lasso) to Logistic Regression will improve F1-macro compared to the unregularized Logistic Regression by reducing the influence of less important features.
