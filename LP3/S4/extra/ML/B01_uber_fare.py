"""SPPU Group B #1: Uber fare regression, correlation, outlier analysis, LR vs RF."""
import argparse
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error

DATA=Path(__file__).resolve().parent/'datasets'/'uber.csv'
def prepare(df):
    required=['fare_amount','pickup_datetime','pickup_longitude','pickup_latitude','dropoff_longitude','dropoff_latitude','passenger_count']
    df=df[required].copy()
    for col in required:
        if col!='pickup_datetime':df[col]=pd.to_numeric(df[col],errors='coerce')
    df['pickup_datetime']=pd.to_datetime(df['pickup_datetime'],utc=True,errors='coerce')
    before=len(df);df=df.dropna()
    valid=(df['fare_amount']>0)&df['passenger_count'].between(1,8)
    for pre in ['pickup','dropoff']:
        valid &= df[f'{pre}_latitude'].between(-90,90)&df[f'{pre}_longitude'].between(-180,180)
    df=df.loc[valid].copy()
    # Haversine distance in kilometers for route-distance feature (geodesic approximation).
    lat1=np.radians(df.pickup_latitude);lat2=np.radians(df.dropoff_latitude)
    dlat=lat2-lat1;dlon=np.radians(df.dropoff_longitude-df.pickup_longitude)
    a=np.sin(dlat/2)**2+np.cos(lat1)*np.cos(lat2)*np.sin(dlon/2)**2
    df['distance_km']=6371*2*np.arcsin(np.sqrt(np.clip(a,0,1)))
    df=df[df.distance_km.between(0.01,130)].copy()
    df['hour']=df.pickup_datetime.dt.hour;df['day_of_week']=df.pickup_datetime.dt.dayofweek
    df['year']=df.pickup_datetime.dt.year;df['month']=df.pickup_datetime.dt.month
    return df, before-len(df)

def run(quick=False,seed=42):
    df=pd.read_csv(DATA,nrows=16000 if quick else None,low_memory=False)
    df,dropped=prepare(df)
    if len(df)<50:raise ValueError('Too few valid data rows')
    print('Valid rows:',len(df),'removed invalid/missing/outlier coordinates or fares:',dropped)
    cols=['pickup_longitude','pickup_latitude','dropoff_longitude','dropoff_latitude','passenger_count','distance_km','hour','day_of_week','year','month']
    print('Correlation with fare (top numeric):',df[cols+['fare_amount']].corr(numeric_only=True)['fare_amount'].sort_values(ascending=False).round(3).to_dict())
    train,test=train_test_split(df,test_size=.2,random_state=seed)
    # Remove extreme target outliers based ONLY on training targets (avoid test-set leakage).
    q1,q3=train.fare_amount.quantile([.25,.75]);hi=q3+3*(q3-q1)
    old=len(train);train=train[train.fare_amount<=hi].copy()
    print('Training fare IQR upper cap:',round(hi,2),'training rows excluded:',old-len(train))
    models={'Linear Regression':LinearRegression(),'Random Forest':RandomForestRegressor(n_estimators=25 if quick else 60,max_depth=18,min_samples_leaf=2,random_state=seed,n_jobs=2)}
    results={}
    for name,model in models.items():
        model.fit(train[cols],train.fare_amount)
        pred=model.predict(test[cols]);results[name]={'R2':float(r2_score(test.fare_amount,pred)),'RMSE':float(np.sqrt(mean_squared_error(test.fare_amount,pred))),'MAE':float(mean_absolute_error(test.fare_amount,pred))}
        print(name,{k:round(v,4) for k,v in results[name].items()})
    return results
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--quick',action='store_true');args=p.parse_args();run(args.quick)
