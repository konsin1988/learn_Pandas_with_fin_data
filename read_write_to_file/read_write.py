import pandas as pd
import os
import numpy as np


# df_weekly = pd.read_excel('vix.xlsx', sheet_name='weekly', index_col=0, parse_dates=True)

# print(df_weekly.info())
# print(df_weekly.head(10))



# df_monthly = pd.read_excel('vix.xlsx', index_col=0, parse_dates=True)
# print(df_monthly.head(10))

# df = pd.read_excel('vix.xlsx', sheet_name=False, parse_dates=['Дата'], date_format='%d.%m.%Y')
# print(df.head(10))
# print(df.info())

# df_fond_market = pd.read_excel('bag_fond_market.xlsx', thousands=',')
# print(df_fond_market.head(10))
# print(df_fond_market.info())

# ---------------------------------------------
# df_2017 = pd.read_excel('USD000UTSTOM_170101_171231.xlsx', parse_dates=['<DATE>'])
# df_2022 = pd.read_excel('USD000UTSTOM_220101_221231.xlsx', parse_dates=['<DATE>'])

# print(round(df_2017['<HIGH>'].max() - df_2017['<LOW>'].min(), 2))
# print(round(df_2022['<HIGH>'].max() - df_2022['<LOW>'].min(), 2))

# -----------------------------------------------------
dir = './tabs_2018-2022/'
# for x in sorted(os.listdir(dir)):
#     year = '20' + x.split('_')[-1][:2]
#     df = pd.read_excel(dir + x)
#     print(f'{year}: {df['<CLOSE>'].mean().__round__(4)}')

df = pd.read_excel(dir + sorted(os.listdir(dir))[0], parse_dates=['<DATE>'])
df = df[['<DATE>', '<CLOSE>']]
print(df.head())
(df
    .assign(DATE = lambda x: x['<DATE>'].apply(lambda x: pd.Timestamp(x).strftime('%d.%m.%Y')))
    .drop(['<DATE>'], axis=1)
    .set_axis(['DATE', '<CLOSE>'], axis=1)
    .to_excel('result.xlsx', index=False, sheet_name='123')
    
)