# Group B: Machine Learning

The required datasets are all in `datasets/`, not duplicated per notebook. All six numbered assignments have Python files and clean notebooks. All datasets are copied unchanged from user-provided Set 1/Set 2; Titanic was present only in Set 2.

| No. | Required subject | Program | Dataset |
|---|---|---|---|
| B01 | Uber fare prediction: regression, preprocessing, correlation and evaluation | `B01_uber_fare.py` | `uber.csv` |
| B02 | Email spam: KNN and SVM | `B02_email_spam.py` | `emails.csv` |
| B03 | Bank churn: neural-network classifier | `B03_bank_churn_ann.py` | `Churn_Modelling.csv` |
| B04 | Gradient descent y=(x+3)² | `B04_gradient_descent.py` | None |
| B05 | Diabetes KNN: confusion matrix/accuracy/precision/recall | `B05_knn_diabetes.py` | `diabetes.csv` |
| B06 | Sales clustering K-Means + elbow method | `B06_sales_kmeans.py` | `sales_data_sample.csv` |
| MP01 | Titanic survival (mini-project option 8) | `MP01_titanic_survival.py` | `titanic_train.csv` |

**Titanic:** 891 labeled rows, 12 columns, supplied in Set 2 as `titanic_data.csv`; renamed to `titanic_train.csv` without changing any CSV content. Set 1's RandomForest script now works with the included dataset; Set 2's logistic-regression approach is available under `alternatives/`.

```bash
python ML/B01_uber_fare.py --quick
python ML/MP01_titanic_survival.py
python ML/alternatives/MP01_titanic_logistic_regression.py
jupyter lab
```

The primary notebooks use the tested Python scripts. `notebooks/MP01_titanic_set2_reference.ipynb` preserves Set 2's more detailed visualization approach but is an optional reference notebook rather than the main tested execution path. It has no stored cell outputs.
