"""SPPU Group B #3: bank churn neural network (sklearn multi-layer perceptron)."""
import argparse
from pathlib import Path
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
DATA=Path(__file__).resolve().parent/'datasets'/'Churn_Modelling.csv'
def run(quick=False):
    df=pd.read_csv(DATA)
    if quick:df=df.sample(n=min(3000,len(df)),random_state=42)
    target=df['Exited'].astype(int);X=df.drop(columns=['Exited','RowNumber','CustomerId','Surname'],errors='ignore')
    categoricals=['Geography','Gender'];numeric=[c for c in X.columns if c not in categoricals]
    # fit preprocessing ONLY on the training split via Pipeline
    preprocess=ColumnTransformer([('cat',OneHotEncoder(handle_unknown='ignore'),categoricals),('numeric',StandardScaler(),numeric)])
    model=Pipeline([('prepare',preprocess),('ann',MLPClassifier(hidden_layer_sizes=(14,7),max_iter=55 if quick else 130,early_stopping=True,n_iter_no_change=12,random_state=42))])
    X_train,X_test,y_train,y_test=train_test_split(X,target,test_size=.2,random_state=42,stratify=target)
    model.fit(X_train,y_train);pred=model.predict(X_test)
    result={'accuracy':float(accuracy_score(y_test,pred)),'confusion_matrix':confusion_matrix(y_test,pred).tolist()}
    print(result);print(classification_report(y_test,pred,zero_division=0))
    print('Neural network: MLP with backpropagation (sklearn), no TensorFlow requirement')
    return result
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--quick',action='store_true');run(p.parse_args().quick)
