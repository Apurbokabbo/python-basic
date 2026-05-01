import pandas as pd

data = {
       'Name': ["Sajjad" , "Anik" , "AG" , "Jaman"],
        'Age': [34,23,36,30]
    }

df= pd.DataFrame(data)
df.to_excel('Write-Excel.xlsx',index=False)