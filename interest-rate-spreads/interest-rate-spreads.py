import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    df = pd.read_csv('data/T10Y2Y.csv')
    df2 = pd.read_csv('data/T10Y3M.csv')
    df = df.tail(10000)
    df2 = df2.tail(10000)
    #df = df.head()

    df.loc[df['T10Y2Y'] == '.', 'T10Y2Y'] = np.nan
    df2.loc[df2['T10Y3M'] == '.', 'T10Y3M'] = np.nan

    df['DATE'] = pd.to_datetime(df['DATE'])
    df['T10Y2Y'] = df['T10Y2Y'].astype(float)

    df2['DATE'] = pd.to_datetime(df2['DATE'])
    df2['T10Y3M'] = df2['T10Y3M'].astype(float)
    #treasury_10y_2y.fillna('NA', inplace=True)
    #treasury_10y_3m.fillna('NA', inplace=True)

    #treasury_10y_3m.reset_index(inplace=True)

    plt.plot(df['DATE'], df['T10Y2Y'])
    plt.plot(df2['DATE'], df2['T10Y3M'])
    plt.axhline(y=0, color='r', linestyle='-')
    plt.tick_params(axis='x', which='major', labelsize=8)

    plt.show()


    #treasury_10y_2y.set_axis(['DATE'], inplace=True)
    #treasury_10y_3m.set_axis(['DATE'], inplace=True)

    print(df)
    print(df.dtypes)
    pass

def main():
    load_data()
    pass

if __name__ == '__main__':
    main()