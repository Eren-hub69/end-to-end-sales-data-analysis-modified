import pandas as pd
import os

def analyze_data(df):
    if not os.path.exists("outputs"):
        os.makedirs("outputs")

    numeric_col=df.select_dtypes(include=['int64','float64']).columns
    categorical_col=df.select_dtypes(include=['object']).columns 
    print(" \ninside the analyze\n")

    with open("outputs/insights.txt","w" ) as f:
            f.write("Data insights-->\n\n")
            f.write("NUMERIC COLUMN ANALYSIS:\n")

            for col in numeric_col:
                f.write(f"column: {col}")
                f.write(f"mean: {df[col].mean()}\n")
                f.write(f"median: {df[col].median()}\n")
                f.write(f"max: {df[col].max()}\n")
                f.write(f"min: {df[col].min()}\n")

            f.write("categorical column analysis: \n")
        
        
            for col in categorical_col:
             f.write(f"\ncolumn: {col}\n")
             f.write(f"\nunique values: {df[col].nunique()}\n")
             f.write(f"\ntop value : {df[col].mode()[0]}\n")

             f.write("TOP 5 value counts:\n")
             value_counts=df[col].value_counts().head(5)
             f.write(str(value_counts)+"\n") 

          
            f.write("\n\n correlation matrix: ")
            corr=df[numeric_col].corr()
            f.write(str(corr))

        

    

def graphs(df):
    if not os.path.exists("outputs"):
         os.makedirs("outputs")

    if not os.path.exists("outputs/graphs"):
        os.makedirs("outputs/graphs")

    import matplotlib.pyplot as plt
    numeric_col=df.select_dtypes(include=['int64','float64']).columns
    categorical_col=df.select_dtypes(include=['object']).columns 
    print("inside the graphs")

    for col in numeric_col:
       plt.figure()
       df[col].hist()
       plt.title(col)
       safe_col=col.replace("/","_").replace(" ","_")

       plt.savefig(f"outputs/graphs/{safe_col}_hist.png")
       plt.close()

    for col in categorical_col:
        plt.figure()
        df[col].value_counts().head().plot(kind='bar')
        plt.title(col)
        safe_col=col.replace("/","_").replace(" ","_")

        plt.savefig(f"outputs/graphs/{safe_col}_bar.png")
        plt.close()

    
    for  col in df.columns:
        if'date'in col.lower():
            df[col] = pd.to_datetime(df[col], errors='coerce')
            df_sorted = df.sort_values(by=col)
            numeric_cols = df.select_dtypes(include=['int64','float64']).columns

            if len(numeric_cols)>0:
                target=numeric_cols[0]
                plt.figure()
                df_sorted.groupby(col)[target].sum().plot()

                plt.title("trend line sales X dates")
                plt.xlabel("dates")
                plt.ylabel(target)
                safe_col=target.replace("/","_").replace(" ","_")

                plt.savefig(f"outputs/graphs/{safe_col}_trend.png")
                plt.close()





    