import pandas as pd


def read_csv(file_name):
  try:
    null_values = ["n/a", "na", "undefined"]
    df = pd.read_csv(f'../data/{file_name}', na_values=null_values)
    return df
  except:
    print("Log:-> File Not Found")

  
def show_info(df):
    print(f"Data Frame contain {df.shape[0]} rows and {df.shape[1]} columns")