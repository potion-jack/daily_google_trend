import pandas as pd
df=pd.read_csv("result.csv",index_col=0,header=None)

df.reset_index(inplace=True)

df.columns = ['name','rate','date']
df.date=pd.to_datetime(df.date,format="%Y_%m_%d")
df_sorted=df.sort_values(['date','rate'],ascending=[True,False])

df_a=df_sorted.loc[:,['name',"date"]].drop_duplicates()

df_ans=pd.merge(df_sorted.rate, df_a,
                left_index=True, right_index=True,
                how='left').dropna()

df_ans=df_ans[['name','rate','date']]
df_ans.to_csv('crwals/cleaned_result.csv')
