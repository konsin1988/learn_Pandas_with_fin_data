import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

# unemp = pd.read_excel('unemployment_eu.xlsx')

# unemp = (unemp
#     .assign(**{'Месяц': lambda x: x['Дата выпуска'].str.split(expand=True)[1].str.strip('()'),'Дата выпуска': lambda x: pd.to_datetime(x['Дата выпуска'].str.split(expand=True)[0], dayfirst=True)})
#     .sort_values(['Дата выпуска'], ignore_index=True)
#     .set_index('Дата выпуска')
#     [['Месяц', 'Факт', 'Прогноз']]
# )
# print(unemp.head(10))
# dates_str = unemp.reset_index()['Дата выпуска'].apply(lambda x: x.strftime('%d.%m.%Y')).to_list()
# print(dates_str)
# unemp.plot(y = ['Факт', 'Прогноз'], 
#            figsize=(10,8), 
#            ylim=[5,10], 
#            grid=True, 
#            rot=60, 
#            style=['o-', '*-'], 
#            color=['green', 'red'], 
#         #    subplots=True,
#         #    sharex=False,
#             secondary_y=True,
#            alpha=0.8,
#            )

# ----------------------------------------------------
# df_aap = pd.read_csv('aapl_close_revenue.csv', parse_dates=['Дата'], date_format='%m/%Y')
# print(df_aap.head(10))
# df_aap.plot(x = 'Дата', y = ['Выручка, млрд долл.США', 'Цена закрытия'], ylabel='Квартальная выручка, млрд долл. США')
# df_aap['Цена закрытия'].plot(figsize=(13,7), 
#                             title='Apple',
#                             ylabel='Цена закрытия, долл. США',
#                             ylim=[0,210],
#                             color='green', 
#                             alpha=0.7,
#                             legend=True)
# df_aap['Выручка, млрд долл.США'].plot(secondary_y=True,
#                                      xlabel='Месяц',
#                                      ylabel='Квартальная выручка, млрд долл. США',
#                                      ylim=[0,130],
#                                      color='red',
#                                      alpha=0.7,
#                                      grid=True,
#                                      style='o-',
#                                      legend=True)

# --------------------------------------------------------------------
# df_brent = pd.read_csv('brent_m_2008_2023.csv')
# print(df_brent.head())
# df_brent = (df_brent
#     .assign(high_low = lambda x: x['high'] - x['low'])
# )

# df_brent.loc[102:].plot(kind='bar', 
#                 x = 'date',
#                 y = 'high_low',
#                 ylim = [0, 50]
#                 )

# --------------------------------------------------------
# stocks_values = {'Дата': ['16/08/2023','16/08/2023', '16/08/2023', '17/08/2023', '17/08/2023', 
#                 '17/08/2023', '18/08/2023', '18/08/2023', '18/08/2023', '21/08/2023',
#                 '21/08/2023', '21/08/2023', '24/08/2023', '24/08/2023', '24/08/2023', 
#                 '24/08/2023'],
#        'Акция': ['Аэрофлот','Газпром', 'ВТБ', 'Аэрофлот','Газпром', 'ВТБ', 
#                  'Аэрофлот','Газпром', 'ВТБ', 'Аэрофлот','Газпром', 'ВТБ', 
#                  'Русгидро', 'Аэрофлот','Газпром', 'ВТБ'],       
#        'Куплено, руб.': [12900, 26240, 15000, 17670, 3700, 36500, 83250, 14885, 17580, 
#                        13700, 27354, 13590, 59400, 38830, 62052, 25708]}
# stocks = pd.DataFrame(stocks_values)
# stocks_new = stocks.pivot_table(values='Куплено, руб.', index='Дата', columns='Акция', 
#                                 aggfunc=sum, fill_value=0)

# stocks_new.plot(kind='bar', 
#                 figsize=(12,7),
#                 title='Покупка акций в портфель',
#                 xlabel='Дата',
#                 ylabel='Куплено, руб.',
#                 color=['violet', 'yellow', 'green', 'red'],
#                 alpha=0.4,
#                 rot=20)

# --------------------------------------------------------------------

# platinum_gold = pd.read_csv('platinum_gold_m_01.01.18_31.08.23.csv')

# platinum_gold.plot(kind='area',
#                    figsize=(15,7),
#                    x='Дата',
#                    y=['Цена_gold', 'Цена_platinum'],
#                    title='Цена закрытия фьючерсов на золото и платину (месячный таймфрейм)',
#                    xlabel='Дата',
#                    ylabel='Цена',
#                    color=['green', 'grey'],
#                    alpha=0.4,
#                    ylim=[0, 2400],
#                    stacked=False)

# ------------------------------------------
df_plat = pd.read_csv('platinum_gold_palladium_m_01.01.18_31.08.23.csv')
# df_plat.plot(x = 'Дата',
#             legend = False,
#             rot = -45,
#             subplots=True,
#             sharex=True,
#             sharey=True
#             )
# df_plat.plot(figsize=(12,7), x='Дата', y=['Цена_platinum', 'Цена_gold', 'Цена_palladium'], style=['o-', '*-', 'o--'])
# df_plat.plot(figsize=(12,7), x='Дата', y=['Цена_palladium', 'Цена_platinum', 'Цена_gold'], style=['o--', 'o-', '*-'])
# -------------------------------------------
# df_plat.plot(kind='area', x='Дата', rot='vertical', stacked=False)
# df_plat.plot(kind='area', figsize=(15,7), x='Дата', color=['green', 'yellow', 'grey'], ylim=[0,3500], stacked=False)
# df_plat.plot(kind='area', figsize=(15,7), x='Дата', color=['green', 'yellow', 'grey'], xlim=[0,80], stacked=False)
# df_plat.plot(kind='area', figsize=(15,7), x='Дата', color=['green', 'yellow', 'grey'], rot=0)
# df_plat.plot(kind='area', figsize=(15,7), color=['green', 'yellow', 'grey'], stacked=False)
# df_plat.plot(kind='area', figsize=(15,7), x='Дата', y=['Цена_platinum', 'Цена_gold', 'Цена_palladium'], stacked=False, label=['platinum', 'gold', 'palladium'])
df_plat.plot(kind='area', figsize=(15,7), x='Дата', stacked=False, label=['platinum', 'gold', 'palladium'])


plt.show()