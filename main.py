import sys
import pandas as pd
from cleaning import clean_data
from analysis import analyze_data , graphs


def main(file_path):
    if len(sys.argv) < 2:
      print("Usage: main.py file.csv")
      return
    
    
    
    df=pd.read_csv(file_path)

    df=clean_data(file_path)

    analyze_data(df)
    graphs(df)


    print("project completed successfully")

if __name__=="__main__":
     file_path=sys.argv[1]
     main(file_path)
