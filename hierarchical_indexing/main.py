import pandas as pd
import numpy as np 

df = pd.read_excel('TURNOVER_DEPO_2023.xlsx', skiprows=5, skipfooter=3, header=[0,1], index_col=0).T
# print(df.head(20))

# print(['Депозитные операции', 'РЕПО'] * 5)

df_values = [[ 902329,  955877, 1062054, 1034478, 1191104, 1285753, 1153421, 1157938, 1140147],
             [1189139, 1064640, 1252892, 1220073, 1254018, 1330504, 1529282, 1773959, 1962971],
             [  29122,   20309,   18777,   21316,   21475,   23376,   18052,   26469,   38998],
             [  15461,   29644,   38711,  104118,   30658,   33601,   52193,   68238,   46057],
             [  16413,   20132,   20742,   15648,   20347,   18378,   19397,   16351,   17790],
             [   5299,    1663,    1085,    3021,    1171,    1172,    1066,    1648,    1798],
             [   4960,   33426,    5498,    8091,   19317,   22751,   39579,   31368,   17375],
             [  26791,   28538,   45002,   58244,   42802,   42763,   40212,   39897,   46704],
             [    456,     365,     938,     910,     561,     581,    3142,    4429,    4504],
             [      0,       0,       0,       0,       0,       0,       0,       0,       0]]
df_columns = [['2023, млн рублей'] * 9, 
              ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь']]
df_index = [['РОССИЙСКИЙ РУБЛЬ (RUB)'] * 2 + ['ДОЛЛАР США (USD)']*2 + 
            ['ЕВРО (EUR)'] * 2 + ['КИТАЙСКИЙ ЮАНЬ (CNY)'] * 2 +
            ['ПРОЧИЕ'] * 2, ['Депозитные операции', 'РЕПО']*5]
df = pd.DataFrame(df_values, columns=df_columns, index=df_index)

# print(df.index)

columns = list(zip(['2023, млн рублей'] * 9, ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь']))
index = list(zip(['РОССИЙСКИЙ РУБЛЬ (RUB)'] * 2 + ['ДОЛЛАР США (USD)']*2 + 
            ['ЕВРО (EUR)'] * 2 + ['КИТАЙСКИЙ ЮАНЬ (CNY)'] * 2 +
            ['ПРОЧИЕ'] * 2, ['Депозитные операции', 'РЕПО']*5))

index = pd.MultiIndex.from_arrays([['РОССИЙСКИЙ РУБЛЬ (RUB)'] * 2 + ['ДОЛЛАР США (USD)']*2 + 
            ['ЕВРО (EUR)'] * 2 + ['КИТАЙСКИЙ ЮАНЬ (CNY)'] * 2 +
            ['ПРОЧИЕ'] * 2, ['Депозитные операции', 'РЕПО']*5], names=['Валюта', 'Вид операции'])

# print(index)
columns = pd.MultiIndex.from_arrays([['2023, млн рублей'] * 9, ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь']], names=['Год', 'Месяц'])
# print(columns)

df = pd.DataFrame(df_values, columns=columns, index=index)
# print(df)

# print(
#     df.loc[('РОССИЙСКИЙ РУБЛЬ (RUB)'), ('2023, млн рублей', 'февраль')]
# )
print(df.iloc[0:4, 0:4])