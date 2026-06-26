import pandas as pd
df=pd.read_excel('Sales_Dataset.xlsx')
df=df.drop_duplicates()
df['Age']=df['Age'].fillna(df['Age'].mean())
df['Gender']=df['Gender'].fillna('Unknown')
df.to_excel('Cleaned_Sales_Dataset.xlsx',index=False)
