import pandas as pd

def readFile(file):
        data=pd.read_csv(file)
        return data
        
    
def dataAnalysis(data):
    try:
        data['Daily Returns']=(data['Close '] / data['Close '].shift(1)) - 1
        Daily_Volatility=data['Daily Returns'].std()
        Annualized_Volatility = Daily_Volatility * (len(data) ** 0.5)
        return {"Daily_Volatility":Daily_Volatility,"Annualized_Volatility":Annualized_Volatility}
    except Exception as e:
        print("Error on dataAnalysis def ",e)
        return None
