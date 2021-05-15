import pandas as pd
import matplotlib.pyplot as plt
exclude={
    'time':['time','Time','Month','month','week','week','Date'],
    'types':['int64','float64','datetime64','bool']
}

df=pd.read_csv('Iris.csv')
a=[]
rows=list(df.index)
sum(rows)
colmn=df.columns
#print(df.dtypes)
for col in df.columns:
    #print(col.dtypes)
    if (col in exclude['time'] and df[col].dtypes == 'object') or df[col].dtypes in exclude['types']:
        pass
    else:
        df.drop([col], axis = 1 ,inplace = True)
#print(rows,':',colmn)       
#print(df) #here we get the proper dataframe
column_detail=df.columns
#N_points = 100000
#n_bins = 20
df.plot(subplots=True)
df.plot(subplots=True,kind='bar')
df.plot(subplots=True,kind='hist')
plt.show()
#df.plot()
#fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)
'''for x in column_detail:
    if x in exclude['time']:
        pass
        #y=df[x]
        #plt.scatter(x,y)
        #plt.show()
    else:
        #axs[0].hist(x, bins=n_bins)
        #axs[1].hist(y, bins=n_bins)
        plt.figure(figsize = (10, 7))
        a = df[x]
        plt.hist(a, bins = 20, color = "purple")
        plt.title(x)
        plt.xlabel(x)
        plt.ylabel("Frequency")
        plt.show()
        
'''