# src/cleaning.py
# Example cleaning script. Edit paths and logic as needed.

import pandas as pd

def load_raw(path='data/raw/mabaat.csv'):
    df = pd.read_csv(path, encoding='utf-8')
    return df

def basic_clean(df):
    # drop unnamed empty columns if exist
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    # example: convert numeric columns
    for col in ['صافى كمية مبيعات', 'صافى قيمة مبيعات']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

if __name__ == '__main__':
    df = load_raw()
    print('Raw shape:', df.shape)
    df = basic_clean(df)
    print('Clean shape:', df.shape)
    df.to_csv('data/clean/Fact_Sales_Clean.csv', index=False, encoding='utf-8')
