import pandas as pd

def clean_data(file):
 
     df=pd.read_csv(file)
    
     numeric_cols=df.select_dtypes(include=['int64','float64']).columns 
     for col in numeric_cols:
      df[col]=df[col].fillna(df[col].mean())
     
    
     categorical_cols=df.select_dtypes(include=['object']).columns

     for col in categorical_cols:
        df[col]=df[col].fillna(df[col].mode()[0])

     for col in df.columns:
        if 'date' in col.lower():
           df[col]=pd.to_datetime(df[col],errors='coerce')
           df[col]=df[col].ffill()   

     return df
