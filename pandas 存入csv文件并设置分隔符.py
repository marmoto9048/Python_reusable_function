import pandas as pd 
df = pd.read_excel('./meta_info.xlsx')
df.to_csv('./meta_info.csv',sep=';')



