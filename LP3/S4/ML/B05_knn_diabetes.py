"""SPPU Group B #5: KNN for diabetes with correct train-only imputation and scaling."""
import argparse
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix,accuracy_score,precision_score,recall_score
DATA=Path(__file__).resolve().parent/'datasets'/'diabetes.csv'
def run(quick=False):
    df=pd.read_csv(DATA)
    X=df.drop(columns='Outcome').copy();y=df['Outcome']
    for c in ['Glucose','BloodPressure','SkinThickness','Insulin','BMI']:
        if c in X:X[c]=X[c].replace(0,np.nan)
    X_train,X_test,y_train,y_test=train_test_split(X,y,stratify=y,test_size=.2,random_state=42)
    pipe=Pipeline([('impute',SimpleImputer(strategy='median')),('scale',StandardScaler()),('knn',KNeighborsClassifier(n_neighbors=5))])
    pipe.fit(X_train,y_train);pred=pipe.predict(X_test)
    a=accuracy_score(y_test,pred)
    results={'accuracy':float(a),'error_rate':float(1-a),'precision':float(precision_score(y_test,pred,zero_division=0)),'recall':float(recall_score(y_test,pred,zero_division=0)),'confusion_matrix':confusion_matrix(y_test,pred).tolist()}
    print(results);return results
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--quick',action='store_true');run(p.parse_args().quick)
