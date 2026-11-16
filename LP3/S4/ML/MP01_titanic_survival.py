"""SPPU Group B mini-project #8: Titanic survival classifier; requires Kaggle train.csv."""
import argparse
from pathlib import Path
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

def build_model():
    return Pipeline([('features',ColumnTransformer([
        ('numeric',SimpleImputer(strategy='median'),['Age','Fare','SibSp','Parch','Pclass']),
        ('categorical',Pipeline([('impute',SimpleImputer(strategy='most_frequent')),('onehot',OneHotEncoder(handle_unknown='ignore'))]),['Sex','Embarked'])
    ])),('model',RandomForestClassifier(n_estimators=90,max_depth=6,random_state=42))])

def train_and_evaluate(df):
    feature_cols=['Age','Fare','SibSp','Parch','Pclass','Sex','Embarked']
    missing=[c for c in feature_cols+['Survived'] if c not in df]
    if missing:raise ValueError(f'Missing Titanic columns: {missing}')
    X=df[feature_cols];y=df['Survived'].astype(int)
    Xt,Xv,yt,yv=train_test_split(X,y,test_size=.25,random_state=42,stratify=y)
    model=build_model();model.fit(Xt,yt);pred=model.predict(Xv)
    result={'accuracy':float(accuracy_score(yv,pred)),'confusion_matrix':confusion_matrix(yv,pred).tolist()}
    print(result);print(classification_report(yv,pred,zero_division=0));return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--csv',type=Path,default=Path(__file__).resolve().parent/'datasets'/'titanic_train.csv');args=p.parse_args()
    if not args.csv.exists():p.error('Titanic dataset missing: expected ML/datasets/titanic_train.csv')
    train_and_evaluate(pd.read_csv(args.csv))
