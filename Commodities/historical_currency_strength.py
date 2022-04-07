import pandas as pd
import numpy as np
import re

# Setting Global Gold Price DataFrame
time_intervals = [
    'daily',
    'monthly',
    'quarterly'
]
gold_price_dfs = {}
for time_interval in time_intervals:
    gold_price_dfs[time_interval] = pd.read_csv(
        f'data/gold/global_gold_price_{time_interval}.csv', 
        index_col=0
    )

columns_rename_map = {}
for columns in gold_price_dfs[time_intervals[0]]:
    ccy_code = re.findall(r'\(.*?\)', columns)[0].replace('(', '').replace(')', '')
    columns_rename_map[columns] = ccy_code

for time_interval in time_intervals:
    gold_price_dfs[time_interval].rename(columns=columns_rename_map, inplace=True)

# Filtering Currencies
# ccy_code = ['USD', 'EUR', 'JPY', 'GBP', 'CAD']
# for time_interval in time_intervals:
#    gold_price_dfs[time_interval] = gold_price_dfs[time_interval][ccy_code]

# Calculating Correlations at Each Level
for time_interval in time_intervals:
    diff_df = gold_price_dfs['quarterly'].diff(periods=1, axis=0)
    print(time_interval, diff_df.corr())

print(gold_price_dfs['quarterly'].columns)

#print(gold_price_dfs)

# Quarter View
#print(gold_price_dfs['quarterly'].diff(periods=1, axis=0))


#print(gold_price_dfs)