"""SPPU Group B #2: Email spam detection via KNN and linear SVM."""
import argparse
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectKBest,chi2
from sklearn.preprocessing import MaxAbsScaler
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
DATA=Path(__file__).resolve().parent/'datasets'/'emails.csv'
def run(quick=False):
    df=pd.read_csv(DATA,nrows=1700 if quick else None,low_memory=False)
    if 'Prediction' not in df:raise ValueError('Missing target column Prediction')
    y=df['Prediction'].astype(int);X=df.drop(columns=['Prediction','Email No.'],errors='ignore')
    X=X.apply(pd.to_numeric,errors='coerce').fillna(0).clip(lower=0)
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.2,random_state=42,stratify=y)
    k=min(200,X_train.shape[1])
    models={
        'KNN':Pipeline([('select',SelectKBest(chi2,k=k)),('scale',MaxAbsScaler()),('model',KNeighborsClassifier(n_neighbors=5,n_jobs=2))]),
        'Linear SVM':Pipeline([('select',SelectKBest(chi2,k=k)),('scale',MaxAbsScaler()),('model',LinearSVC(C=0.5,max_iter=2500,random_state=42))]),
    }
    results={}
    for name,model in models.items():
        model.fit(X_train,y_train);pred=model.predict(X_test)
        results[name]=float(accuracy_score(y_test,pred))
        print('\n',name,'accuracy:',round(results[name],4),'confusion matrix:',confusion_matrix(y_test,pred).tolist())
        print(classification_report(y_test,pred,zero_division=0))
    return results
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--quick',action='store_true');run(p.parse_args().quick)
