import pandas as pd

exclude={
    'time':['time','Time','Month','month','week','week','Date'],
    'types':['int64','float64','datetime64','bool']
}

df=pd.read_csv('Iris.csv')
a=[]
rows=list(df.index)
sum(rows)
colmn=df.columns
print(df.dtypes)
for col in df.columns:
    #print(col.dtypes)
    if (col in exclude['time'] and df[col].dtypes == 'object') or df[col].dtypes in exclude['types']:
        pass
    else:
        df.drop([col], axis = 1 ,inplace = True)
#print(rows,':',colmn)       
print(df)