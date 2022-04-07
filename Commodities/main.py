import pandas as pd
import numpy as np
import os

# Commodities Data
commodities = [
    'Brent Oil',
    'Gold',
    'Natural Gas',
    'Nickel',
    'Palladium',
    'Wheat'
]
commodities_df = {}

# Setting Up DataFrames - Indexed on 'Date' and Created 'Change' Column
df = pd.read_csv('commodity_data_2000_2022.csv')
for commodity in commodities:
    commodities_df[commodity] = df[df['Symbol'] == commodity]
    commodities_df[commodity].set_index('Date', inplace=True)
    commodities_df[commodity]['Change'] = commodities_df[commodity]['Close'] - commodities_df[commodity]['Open']

# DataFrame for Aggregate Commodity Movements
movement_df = pd.DataFrame()
for commodity in commodities:
    movement_df[commodity] = commodities_df[commodity]['Change']
    #print(commodity, commodities_df[commodity]['Change'])

print(movement_df.corr())

#print(movement_df.head(n=1000))
