import pandas as pd

def parse_file() -> pd.DataFrame:
    df = pd.read_csv('ChicagoCrimes2021.csv')
    df = df[['CASE#', 'DATE  OF OCCURRENCE', ' PRIMARY DESCRIPTION', 'ARREST', 'LOCATION']]
    df = df.rename(columns={'DATE  OF OCCURRENCE': 'DATETIME', ' PRIMARY DESCRIPTION': 'TYPE'})
    df['HOUR'] = df['DATETIME'].apply(lambda x: (int(x[11:13]) + (12 if x[20] == "P" else 0)))
    df['MINUTE'] = df['DATETIME'].apply(lambda x: int(x[14:16]))
    df['MONTH'] = df['DATETIME'].apply(lambda x: int(x[0:2]))
    df['ARREST'] = df['ARREST'] == 'Y'
    return df
