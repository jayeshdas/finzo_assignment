import pandas as pd
import os,sys
class Report:

    def __init__(self) -> None:
        file=input("Enter csv File path :")
        if os.path.exists(file):
            data=self.readFile(file)
            if data.shape[0]:
                result=self.dataAnalysis(data)
                print(result)
        else:
            print(f"file not found {file}!!\nEnter Valid File Path")
            sys.exit(1)

        
    def readFile(self,file):
        data=pd.read_csv(file)
        return data
        
    
    def dataAnalysis(self,data):
        try:
            data['Daily Returns']=(data['Close '] / data['Close '].shift(1)) - 1
            Daily_Volatility=data['Daily Returns'].std()
            Annualized_Volatility = Daily_Volatility * (len(data) ** 0.5)
            return {"Daily_Volatility":Daily_Volatility,"Annualized_Volatility":Annualized_Volatility}
        except Exception as e:
            print("Error on dataAnalysis def ",e)
            return None

Report()