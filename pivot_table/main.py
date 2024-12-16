import pandas as pd 
import numpy as np

df_values = [['China', 'Gold Reserves', 2192, 'Sep/23', 'Tonnes'],
             ['China', 'Employed Persons', 733510, 'Dec/22', 'Thousand'],
             ['China', 'Composite PMI', 50.0, 'Oct/23', 'points'],             
             ['France', 'Gold Reserves', 2437, 'Sep/23', 'Tonnes'],
             ['France', 'Employed Persons', 30411, 'Jun/23', 'Thousand'],
             ['France', 'Composite PMI', 44.6, 'Oct/23', 'points'],
             ['Germany', 'Gold Reserves', 3353, 'Sep/23', 'Tonnes'],
             ['Germany', 'Employed Persons', 45819, 'Sep/23', 'Thousand'],
             ['Germany', 'Composite PMI', 45.9, 'Oct/23', 'points'],
             ['India', 'Gold Reserves', 807, 'Sep/23', 'Tonnes'],
             ['India', 'Employed Persons', np.nan, np.nan, np.nan],
             ['India', 'Composite PMI', 58.4, 'Oct/23', 'points'],
             ['Italy', 'Gold Reserves', 2452, 'Sep/23', 'Tonnes'],
             ['Italy', 'Employed Persons', 23656, 'Sep/23', 'Thousand'],
             ['Italy', 'Composite PMI', 47.0, 'Oct/23', 'points'],
             ['Russia', 'Gold Reserves', 2333, 'Sep/23', 'Tonnes'],
             ['Russia', 'Employed Persons', 74000, 'Sep/23', 'Thousand'],
             ['Russia', 'Composite PMI', 54.7, 'Sep/23', 'points'],
             ['Russia', 'Composite PMI', 53.6, 'Oct/23', 'points'],
             ['United States', 'Gold Reserves', 8133, 'Sep/23', 'Tonnes'],
             ['United States', 'Employed Persons', 161222, 'Oct/23', 'Thousand'],
             ['United States', 'Composite PMI', 50.2, 'Sep/23', 'points'],
             ['United States', 'Composite PMI', 50.7, 'Oct/23', 'points']]
df_columns = ['Country', 'Indicator', 'Value', 'Reference', 'Unit']
df = (
    pd.DataFrame(df_values, columns=df_columns)
    .assign(Reference = lambda x: pd.PeriodIndex(pd.to_datetime(x['Reference'], format='%b/%y'), freq='M'))
)

# print(df
#     .pivot_table(values='Value', columns='Indicator', index='Country')      
# )

# print(
#     df
#     .pivot_table(values='Value', index=['Indicator', 'Country'])
# )

# print(
#     df
#     .pivot_table(values='Value', columns='Reference', index=['Indicator', 'Country'], fill_value='-')
# )


# -----------------------------TASKS -------------------------------------------
stocks_values = {'Дата': ['16/08/2023','21/08/2023', '21/08/2023', '21/08/2023', '22/08/2023', 
                '22/08/2023', '22/08/2023', '22/08/2023', '22/08/2023', '22/08/2023',
                '24/08/2023', '24/08/2023', '24/08/2023', '24/08/2023', '24/08/2023', 
                '24/08/2023'],
       'Компания': ['Аэрофлот','Сбербанк ао', 'ВТБ', 'Газпром', 'Норникель', 'Новатэк', 'Сбербанк п', 
                    'Лукойл', 'Лукойл', 'Аэрофлот', 'Газпром', 'ВТБ', 'Сбербанк ао', 'Русгидро', 'НЛМК', 
                    'Сбербанк ао'],
       'Цена, руб./акцию': [43.30, 261.40, 0.028, 176.70, 16300, 1670, 260, 6280, 6595, 45.20,
                           174, 0.027, 257, 0.8830, 194, 256.70],
       'Количество, шт.': [3000, 100, 500_000, 100, 2, 20, 300, 30, 30, 3000, 100,
                           500_000, 200, 10000, 300, 100],
       'Итого, руб.': [129900, 26140, 14000, 17670, 32600, 33400, 78000, 188400, 197850, 
                       135600, 17400, 13500, 51400, 8830, 58200, 25670],
       'Сделка': ['куплено', 'куплено', 'куплено', 'куплено', 'куплено', 'куплено', 'куплено', 
                  'куплено', 'продано', 'продано', 'куплено', 'куплено', 'куплено', 'куплено', 
                  'куплено', 'куплено']}
stocks = pd.DataFrame(stocks_values)

# print(
#     stocks
#     .pivot_table(index=['Дата', 'Компания'], values='Итого, руб.', aggfunc='sum')
# )

stocks_values = {'Дата': ['16/08/2023','21/08/2023', '21/08/2023', '21/08/2023', '22/08/2023', 
                '22/08/2023', '22/08/2023', '22/08/2023', '22/08/2023', '22/08/2023',
                '24/08/2023', '24/08/2023', '24/08/2023', '24/08/2023', '24/08/2023', 
                '24/08/2023'],
       'Компания': ['Аэрофлот','Сбербанк ао', 'ВТБ', 'Газпром', 'Норникель', 'Новатэк', 'Сбербанк п', 
                    'Лукойл', 'Лукойл', 'Аэрофлот', 'Газпром', 'ВТБ', 'Сбербанк ао', 'Русгидро', 'НЛМК', 
                    'Сбербанк ао'],
       'Цена, руб./акцию': [43.30, 261.40, 0.028, 176.70, 16300, 1670, 260, 6280, 6595, 45.20,
                           174, 0.027, 257, 0.8830, 194, 256.70],
       'Количество, шт.': [3000, 100, 500_000, 100, 2, 20, 300, 30, 30, 3000, 100,
                           500_000, 200, 10000, 300, 100],
       'Итого, руб.': [129900, 26140, 14000, 17670, 32600, 33400, 78000, 188400, 197850, 
                       135600, 17400, 13500, 51400, 8830, 58200, 25670],
       'Сделка': ['куплено', 'куплено', 'куплено', 'куплено', 'куплено', 'куплено', 'куплено', 
                  'куплено', 'продано', 'продано', 'куплено', 'куплено', 'куплено', 'куплено', 
                  'куплено', 'куплено']}
stocks = pd.DataFrame(stocks_values)

# print(
#     stocks
#     .pivot_table(values=['Итого, руб.', 'Количество, шт.'], index=['Дата', 'Компания'], aggfunc='sum')
# )

stocks_values = {'Дата': ['16/08/2023','21/08/2023', '21/08/2023', '21/08/2023', '22/08/2023', 
                '22/08/2023', '22/08/2023', '22/08/2023', '22/08/2023', '22/08/2023',
                '24/08/2023', '24/08/2023', '24/08/2023', '24/08/2023', '24/08/2023', 
                '24/08/2023'],
       'Компания': ['Аэрофлот','Сбербанк ао', 'ВТБ', 'Газпром', 'Норникель', 'Новатэк', 'Сбербанк п', 
                    'Лукойл', 'Лукойл', 'Аэрофлот', 'Газпром', 'ВТБ', 'Сбербанк ао', 'Русгидро', 'НЛМК', 
                    'Сбербанк ао'],
       'Цена, руб./акцию': [43.30, 261.40, 0.028, 176.70, 16300, 1670, 260, 6280, 6595, 45.20,
                           174, 0.027, 257, 0.8830, 194, 256.70],
       'Количество, шт.': [3000, 100, 500_000, 100, 2, 20, 300, 30, 30, 3000, 100,
                           500_000, 200, 10000, 300, 100],
       'Итого, руб.': [129900, 26140, 14000, 17670, 32600, 33400, 78000, 188400, 197850, 
                       135600, 17400, 13500, 51400, 8830, 58200, 25670],
       'Сделка': ['куплено', 'куплено', 'куплено', 'куплено', 'куплено', 'куплено', 'куплено', 
                  'куплено', 'продано', 'продано', 'куплено', 'куплено', 'куплено', 'куплено', 
                  'куплено', 'куплено']}
stocks = pd.DataFrame(stocks_values)

# print(
#     stocks
#     .pivot_table(index=['Дата', 'Компания'], columns=['Сделка'], values='Итого, руб.', aggfunc='sum', fill_value=0)
# )

stocks_values = {'Дата': ['16/08/2023','21/08/2023', '21/08/2023', '21/08/2023', '22/08/2023', 
                '22/08/2023', '22/08/2023', '22/08/2023', '22/08/2023', '22/08/2023',
                '24/08/2023', '24/08/2023', '24/08/2023', '24/08/2023', '24/08/2023', 
                '24/08/2023'],
       'Компания': ['Аэрофлот','Сбербанк ао', 'ВТБ', 'Газпром', 'Норникель', 'Новатэк', 'Сбербанк п', 
                    'Лукойл', 'Лукойл', 'Аэрофлот', 'Газпром', 'ВТБ', 'Сбербанк ао', 'Русгидро', 'НЛМК', 
                    'Сбербанк ао'],
       'Цена, руб./акцию': [43.30, 261.40, 0.028, 176.70, 16300, 1670, 260, 6280, 6595, 45.20,
                           174, 0.027, 257, 0.8830, 194, 256.70],
       'Количество, шт.': [3000, 100, 500_000, 100, 2, 20, 300, 30, 30, 3000, 100,
                           500_000, 200, 10000, 300, 100],
       'Итого, руб.': [129900, 26140, 14000, 17670, 32600, 33400, 78000, 188400, 197850, 
                       135600, 17400, 13500, 51400, 8830, 58200, 25670],
       'Сделка': ['куплено', 'куплено', 'куплено', 'куплено', 'куплено', 'куплено', 'куплено', 
                  'куплено', 'продано', 'продано', 'куплено', 'куплено', 'куплено', 'куплено', 
                  'куплено', 'куплено']}
stocks = pd.DataFrame(stocks_values)

# print(
#     stocks
#     .pivot_table(index=['Дата', 'Компания'], columns='Сделка', values='Количество, шт.', aggfunc='count', fill_value=0)
# )

stocks_values = {'Дата': ['16/08/2023','21/08/2023', '21/08/2023', '21/08/2023', '22/08/2023', 
                '22/08/2023', '22/08/2023', '22/08/2023', '22/08/2023', '22/08/2023',
                '24/08/2023', '24/08/2023', '24/08/2023', '24/08/2023', '24/08/2023', 
                '24/08/2023'],
       'Компания': ['Аэрофлот','Сбербанк ао', 'ВТБ', 'Газпром', 'Норникель', 'Новатэк', 'Сбербанк п', 
                    'Лукойл', 'Лукойл', 'Аэрофлот', 'Газпром', 'ВТБ', 'Сбербанк ао', 'Русгидро', 'НЛМК', 
                    'Сбербанк ао'],
       'Цена, руб./акцию': [43.30, 261.40, 0.028, 176.70, 16300, 1670, 260, 6280, 6595, 45.20,
                           174, 0.027, 257, 0.8830, 194, 256.70],
       'Количество, шт.': [3000, 100, 500_000, 100, 2, 20, 300, 30, 30, 3000, 100,
                           500_000, 200, 10000, 300, 100],
       'Итого, руб.': [129900, 26140, 14000, 17670, 32600, 33400, 78000, 188400, 197850, 
                       135600, 17400, 13500, 51400, 8830, 58200, 25670],
       'Сделка': ['куплено', 'куплено', 'куплено', 'куплено', 'куплено', 'куплено', 'куплено', 
                  'куплено', 'продано', 'продано', 'куплено', 'куплено', 'куплено', 'куплено', 
                  'куплено', 'куплено']}
stocks = pd.DataFrame(stocks_values)

# print(
#     stocks
#     .pivot_table(index=['Компания', 'Дата'], values='Итого, руб.', columns='Сделка', fill_value=0, aggfunc='sum')
# )

stocks_values = {'Дата': ['16/08/2023','21/08/2023', '21/08/2023', '21/08/2023', '22/08/2023', 
                '22/08/2023', '22/08/2023', '22/08/2023', '22/08/2023', '22/08/2023',
                '24/08/2023', '24/08/2023', '24/08/2023', '24/08/2023', '24/08/2023', 
                '24/08/2023'],
       'Компания': ['Аэрофлот','Сбербанк ао', 'ВТБ', 'Газпром', 'Норникель', 'Новатэк', 'Сбербанк п', 
                    'Лукойл', 'Лукойл', 'Аэрофлот', 'Газпром', 'ВТБ', 'Сбербанк ао', 'Русгидро', 'НЛМК', 
                    'Сбербанк ао'],
       'Цена, руб./акцию': [43.30, 261.40, 0.028, 176.70, 16300, 1670, 260, 6280, 6595, 45.20,
                           174, 0.027, 257, 0.8830, 194, 256.70],
       'Количество, шт.': [3000, 100, 500_000, 100, 2, 20, 300, 30, 30, 3000, 100,
                           500_000, 200, 10000, 300, 100],
       'Итого, руб.': [129900, 26140, 14000, 17670, 32600, 33400, 78000, 188400, 197850, 
                       135600, 17400, 13500, 51400, 8830, 58200, 25670],
       'Сделка': ['куплено', 'куплено', 'куплено', 'куплено', 'куплено', 'куплено', 'куплено', 
                  'куплено', 'продано', 'продано', 'куплено', 'куплено', 'куплено', 'куплено', 
                  'куплено', 'куплено']}
stocks = pd.DataFrame(stocks_values)


# print(stocks
#     .pivot_table(index=['Компания', 'Сделка'], columns='Дата', values='Количество, шт.', fill_value=0, aggfunc='sum')
#     .apply(lambda x: pd.to_numeric(x))
#     .assign(**{'Всего, шт.': lambda x: x.sum(axis=1)})
# )

stocks_values = {'Дата': ['16/08/2023','21/08/2023', '21/08/2023', '21/08/2023', '22/08/2023', 
                '22/08/2023', '22/08/2023', '22/08/2023', '22/08/2023', '22/08/2023',
                '24/08/2023', '24/08/2023', '24/08/2023', '24/08/2023', '24/08/2023', 
                '24/08/2023'],
       'Компания': ['Аэрофлот','Сбербанк ао', 'ВТБ', 'Газпром', 'Норникель', 'Новатэк', 'Сбербанк п', 
                    'Лукойл', 'Лукойл', 'Аэрофлот', 'Газпром', 'ВТБ', 'Сбербанк ао', 'Русгидро', 'НЛМК', 
                    'Сбербанк ао'],
       'Цена, руб./акцию': [43.30, 261.40, 0.028, 176.70, 16300, 1670, 260, 6280, 6595, 45.20,
                           174, 0.027, 257, 0.8830, 194, 256.70],
       'Количество, шт.': [3000, 100, 500_000, 100, 2, 20, 300, 30, 30, 3000, 100,
                           500_000, 200, 10000, 300, 100],
       'Итого, руб.': [129900, 26140, 14000, 17670, 32600, 33400, 78000, 188400, 197850, 
                       135600, 17400, 13500, 51400, 8830, 58200, 25670],
       'Сделка': ['куплено', 'куплено', 'куплено', 'куплено', 'куплено', 'куплено', 'куплено', 
                  'куплено', 'продано', 'продано', 'куплено', 'куплено', 'куплено', 'куплено', 
                  'куплено', 'куплено']}
stocks = pd.DataFrame(stocks_values)

print(
    stocks
    .pivot_table(index='Дата', 
                columns=['Компания', 'Сделка'], 
                values='Количество, шт.', 
                fill_value=0, 
                aggfunc='sum',
                margins=True, 
                margins_name='Всего, шт.')
    .loc[:,['Аэрофлот', 'ВТБ', 'Лукойл']]
)