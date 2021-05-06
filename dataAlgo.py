import pandas as pd
import matplotlib.pyplot as plt
class Data():
    def __init__(self):
        self.fileName=input('Enter the file name-->')
    def checking_columns(self):
        self.df=pd.read_csv(self.fileName)
        self.usable_df=self.df.dropna()
        details=self.df.dtypes
        self.column_detail=self.df.columns
    def histo(self):
        for x in self.column_detail:
            plt.figure(figsize = (10, 7))
            a = self.usable_df[x]
            plt.hist(a, bins = 20, color = "purple")
            plt.title(x)
            plt.xlabel(x)
            plt.ylabel("Frequency")
            plt.show()
        
D=Data()
if __name__=='__main__':
    D.checking_columns()
    D.histo()