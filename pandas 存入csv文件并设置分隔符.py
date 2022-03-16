import pandas as pd 
df = pd.read_excel('./meta_info.xlsx')
df.to_csv('./meta_info.csv',sep=';')
 
#设置列名
city = pd.DataFrame([['Sacramento', 'California'], ['Miami', 'Florida']], columns=['City', 'State'])
city.to_csv('city.csv')
