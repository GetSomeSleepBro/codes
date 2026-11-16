"""Alternative Set 2 Titanic mini-project: logistic regression with a leak-free preprocessing pipeline."""
from pathlib import Path
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

DATA = Path(__file__).resolve().parents[1] / 'datasets' / 'titanic_train.csv'

def main():
    data = pd.read_csv(DATA)
    cols = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
    x = data[cols]
    y = data['Survived']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, stratify=y, random_state=42)
    numeric = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
    categorical = ['Sex', 'Embarked']
    preprocess = ColumnTransformer([
        ('number', Pipeline([('missing', SimpleImputer(strategy='median')), ('scale', StandardScaler())]), numeric),
        ('category', Pipeline([('missing', SimpleImputer(strategy='most_frequent')), ('encode', OneHotEncoder(handle_unknown='ignore'))]), categorical),
    ])
    model = Pipeline([('prepare', preprocess), ('logistic', LogisticRegression(max_iter=1000, random_state=42))])
    model.fit(x_train, y_train)
    prediction = model.predict(x_test)
    print('Accuracy:', round(accuracy_score(y_test, prediction), 4))
    print('Confusion matrix:\n', confusion_matrix(y_test, prediction))
    print(classification_report(y_test, prediction, zero_division=0))
    return model

if __name__ == '__main__':
    main()
