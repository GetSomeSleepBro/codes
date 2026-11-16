# Group B: Machine Learning

| Assignment | Program | Dataset in `datasets/` |
|---|---|---|
| B(2) Email spam: KNN and SVM | [B02_email_spam.py](B02_email_spam.py) | `emails.csv` (excluded due to size) |
| B(3) Bank churn: neural-network classifier | [B03_bank_churn_ann.py](B03_bank_churn_ann.py) | `Churn_Modelling.csv` |
| B(4) Diabetes KNN | [B05_knn_diabetes.py](B05_knn_diabetes.py) | `diabetes.csv` |
| Mini-project: Titanic survival | [MP01_titanic_survival.py](MP01_titanic_survival.py) | `titanic_train.csv` |

The diabetes filename retains its original B05 identifier; it corresponds to B(4) in the selected report. Notebook launchers for email spam, bank churn, and diabetes remain in [notebooks/](notebooks/).

`emails.csv` is intentionally not included in LP3 due to its size. To run the spam practical, provide it locally at `ML/datasets/emails.csv`.

Run from `LP3/`:

```bash
python3 ML/B03_bank_churn_ann.py
python3 ML/B05_knn_diabetes.py
python3 ML/MP01_titanic_survival.py
```

Extra topics, their datasets and notebooks, and alternate Titanic implementations are preserved in [../extra/ML/](../extra/ML/).
