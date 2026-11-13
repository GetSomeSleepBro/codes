"""SPPU Group B #6: customer RFM k-means clustering + elbow chart."""
import argparse
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
DATA=Path(__file__).resolve().parent/'datasets'/'sales_data_sample.csv'
def rfm_features(df):
    df=df.copy();df['ORDERDATE']=pd.to_datetime(df['ORDERDATE'],errors='coerce')
    df['SALES']=pd.to_numeric(df['SALES'],errors='coerce')
    df=df.dropna(subset=['CUSTOMERNAME','ORDERDATE','SALES','ORDERNUMBER'])
    reference=df.ORDERDATE.max()+pd.Timedelta(days=1)
    aggregated=df.groupby('CUSTOMERNAME').agg(
        recency=('ORDERDATE',lambda dates:(reference-dates.max()).days),
        frequency=('ORDERNUMBER','nunique'),monetary=('SALES','sum'))
    return aggregated

def run(quick=False,save_chart=False):
    df=pd.read_csv(DATA,encoding='latin-1');R=rfm_features(df)
    if len(R)<5:raise ValueError('Not enough customers for clustering')
    features=np.log1p(R[['recency','frequency','monetary']].clip(lower=0))
    values=StandardScaler().fit_transform(features)
    ks=list(range(1,min(9,len(R))))
    inertias=[]
    for k in ks:
        model=KMeans(n_clusters=k,n_init=10,random_state=42).fit(values)
        inertias.append(float(model.inertia_))
    # Elbow estimates from largest distance to line linking first/last inertia. Heuristic, not a proof.
    x=np.array(ks,dtype=float);y=np.array(inertias);xx=(x-x[0])/(x[-1]-x[0]);yy=(y-y[-1])/(y[0]-y[-1] or 1.)
    curvature=np.abs(yy-(1-xx));suggested=ks[int(np.argmax(curvature))]
    selected=max(2,suggested)
    model=KMeans(n_clusters=selected,n_init=10,random_state=42).fit(values)
    clusters=pd.Series(model.labels_,index=R.index,name='cluster')
    print('Customers:',len(R),'K vs inertia:',list(zip(ks,[round(v,2) for v in inertias])))
    print('Heuristic elbow:',suggested,'selected k:',selected,'cluster sizes:',clusters.value_counts().sort_index().to_dict())
    print('Silhouette:',round(float(silhouette_score(values,model.labels_)),4))
    if save_chart:
        import matplotlib;matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        fig,ax=plt.subplots();ax.plot(ks,inertias,marker='o');ax.set(xlabel='Number of clusters k',ylabel='Within-cluster SSE',title='Elbow method: customer RFM')
        fig.savefig(Path(__file__).resolve().parent/'elbow_chart.png',dpi=150,bbox_inches='tight');plt.close(fig)
        print('Saved ML/elbow_chart.png')
    return {'customers':len(R),'k':selected,'cluster_sizes':clusters.value_counts().to_dict()}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--quick',action='store_true');p.add_argument('--save-chart',action='store_true');a=p.parse_args();run(a.quick,a.save_chart)
