import pandas as pd
import numpy as np

data = {'Товар': ['Молоко', 'Хлеб', 'Сыр', 'Мясо', 'Молоко'],
        'Стоимость': [80, 50, 550, 700, 80],
        'Количество': [20, 50, 10, 5, 25]}

df = pd.DataFrame(data)

# print(
#     df[['Товар', 'Количество']]
#     .groupby('Товар')
#     .sum()
 
# )

# --------------------------------------

data = {'Студент': ['Анна Крайнова', 'Михаил Иванов', 'Жанна Белова', 'Борис Степанов', 
                    'Виктор Столяров', 'Анна Егорова', 'Никита Куликов'],
        'Предмет': ['Математика', 'Математика', 'Физика', 'Физика', 
                    'Математика', 'История', 'Математика'],
        'Баллы': [85, 80, 78, 82, 88, 100, 91]}

df = pd.DataFrame(data)

# print(
#     df
#     .groupby('Предмет')
#     .agg({'Баллы': ['min', 'max', 'mean']})
# )


data = {'Сотрудник': ['Екатерина Фролова', 'Илья Дмитриевский', 'Филипп Галин', 'Михаил Волков', 
                      'Ирина Кузнецова', 'Дмитрий Якубов', 'Азамат Хайруллин'],
        'Департамент': ['IT', 'Маркетинг', 'IT', 'Маркетинг', 'HR', 'IT', 'IT'],
        'Зарплата': [150000, 110000, 85000, 140000, 80000, 126000, 130000]}

df = pd.DataFrame(data)

# print(
#     df
#     .groupby('Департамент')
#     .agg({'Зарплата':'median', 'Сотрудник':'count'})
# )

data = {'Город': ['Сочи', 'Анапа', 'Сочи', 'Геленджик', 
                  'Геленджик', 'Анапа', 'Сочи', 'Геленджик'],
        'Месяц': ['Апрель', 'Май', 'Апрель', 'Апрель', 'Май', 'Апрель', 'Май', 'Май'],
        'Пассажиры': [30000, 25000, 28000, 14000, 18000, 24000, 27000, 15000]}

df = pd.DataFrame(data)

# print(
#     df
#     .groupby('Город')
#     ['Пассажиры']
#     .mean()
# )


data = {'Город': ['Сочи', 'Анапа', 'Сочи', 'Геленджик', 
                  'Геленджик', 'Анапа', 'Сочи', 'Геленджик'],
        'Месяц': ['Апрель', 'Май', 'Апрель', 'Апрель', 'Май', 'Апрель', 'Май', 'Май'],
        'Пассажиры': [30000, 25000, 28000, 14000, 18000, 24000, 27000, 15000]}

df = pd.DataFrame(data)

# print(
#     df
#     .groupby(['Город', 'Месяц'])
#     ['Пассажиры']
#     .sum()
# )

depo_values = [['New Energy Bank', 1_000_000_000, 8.30, 'O/N'],
               ['Cryptocurrencybank', 2_700_000_000, 8.35, 'O/N'],
               ['Big Business Bank', 1_500_000_000, 8.27, 'O/N'],
               ['GreenEnergyBank', 1_800_000_000, 8.35, 'O/N'],
               ['Allmoneybank', 5_900_000_000, 8.45, 'O/N'],
               ['ClearWaterBank', 3_000_000_000, 8.40, 'O/N'],
               ['First Ecologic Bank', 3_000_000_000, 8.41, 'O/N'],
               ['Cryptocurrencybank', 7_500_000_000, 8.50, 'O/N'],
               ['Big Business Bank', 2_500_000_000, 8.35, 'O/N'],
               ['AgroFoodBank', 700_000_000, 8.25, 'O/N'],
               ['Golden Silver Bank', 4_300_000_000, 8.42, 'O/N'],
               ['SmallBusinessBank', 2_000_000_000, 8.31, 'O/N']]
depo_columns = ['Банк', 'Сумма, руб.', 'Ставка', 'Срок']
depo = pd.DataFrame(depo_values, columns=depo_columns)



# print(
#         depo
#         .groupby('Банк')
#         .apply(lambda x: pd.Series({'Сумма, руб.': x['Сумма, руб.'].sum(), 'Cредневзвешенная ставка': 
#                 np.average(x['Ставка'], weights=x['Сумма, руб.']).round(2)}))   
#         .assign(**{'Сумма, руб.': lambda x: x['Сумма, руб.'].map(int)})
#         .reset_index()
# )

import pandas as pd
depo_values = [['New Energy Bank', 1_000_000_000, 8.30, 'O/N'],
               ['AgroFoodBank', 5_000_000_000, 8.50, '1W'],
               ['First Ecologic Bank', 4_500_000_000, 8.60, '1M'],
               ['Golden Silver Bank', 3_800_000_000, 8.67, '1M'],
               ['Big Business Bank', 1_500_000_000, 8.27, 'O/N'],
               ['Big Business Bank', 3_000_000_000, 8.30, 'O/N'],
               ['New Energy Bank', 5_000_000_000, 8.84, '3M'],
               ['New Energy Bank', 2_000_000_000, 8.32, 'O/N'],
               ['First Ecologic Bank', 2_000_000_000, 8.40, 'O/N'],
               ['AgroFoodBank', 2_000_000_000, 8.45, '1W'],
               ['AgroFoodBank', 1_000_000_000, 8.30, 'O/N'],
               ['Big Business Bank', 2_800_000_000, 8.30, 'O/N'],
               ['Golden Silver Bank', 2_500_000_000, 8.65, '1M'],
               ['New Energy Bank', 2_000_000_000, 8.45, '1W'],
               ['First Ecologic Bank', 2_000_000_000, 8.50, '1M'],
               ['Golden Silver Bank', 4_300_000_000, 8.40, 'O/N'],
               ['Golden Silver Bank', 2_200_000_000, 8.35, 'O/N'],
               ['First Ecologic Bank', 4_500_000_000, 8.50, '1M'],
               ['New Energy Bank', 4_000_000_000, 8.80, '3M']]
depo_columns = ['Банк', 'Сумма, руб.', 'Ставка', 'Срок']
depo = pd.DataFrame(depo_values, columns=depo_columns)

# print(
#         depo
#         .groupby(['Банк', 'Срок'])
#         .agg({'Сумма, руб.': 'sum'})
# )

depo_values = [['New Energy Bank', 1_000_000_000, 8.30, 'O/N'],
               ['AgroFoodBank', 5_000_000_000, 8.50, '1W'],
               ['First Ecologic Bank', 4_500_000_000, 8.60, '1M'],
               ['Golden Silver Bank', 3_800_000_000, 8.67, '1M'],
               ['Big Business Bank', 1_500_000_000, 8.27, 'O/N'],
               ['Big Business Bank', 3_000_000_000, 8.30, 'O/N'],
               ['New Energy Bank', 6_000_000_000, 8.84, '3M'],
               ['New Energy Bank', 2_000_000_000, 8.32, 'O/N'],
               ['First Ecologic Bank', 3_000_000_000, 8.41, 'O/N'],
               ['AgroFoodBank', 2_000_000_000, 8.45, '1W'],
               ['AgroFoodBank', 1_000_000_000, 8.30, 'O/N'],
               ['Big Business Bank', 2_500_000_000, 8.30, 'O/N'],
               ['Golden Silver Bank', 2_500_000_000, 8.65, '1M'],
               ['New Energy Bank', 2_000_000_000, 8.45, '1W'],
               ['First Ecologic Bank', 2_000_000_000, 8.50, '1M'],
               ['Golden Silver Bank', 4_300_000_000, 8.40, 'O/N'],
               ['Golden Silver Bank', 2_000_000_000, 8.35, 'O/N'],
               ['First Ecologic Bank', 4_000_000_000, 8.55, '1M'],
               ['New Energy Bank', 4_000_000_000, 8.80, '3M']]
depo_columns = ['Банк', 'Сумма, руб.', 'Ставка', 'Срок']
depo = pd.DataFrame(depo_values, columns=depo_columns)
# print(depo
#         .groupby(['Банк', 'Срок'])
#         .apply(lambda x: pd.Series({'Средневзвешенная ставка': np.average(x['Ставка'], weights=x['Сумма, руб.']).round(2), 'Сумма, руб.': np.sum(x['Сумма, руб.'])}))
#         .assign(**{'Сумма, руб.': lambda x: x['Сумма, руб.'].map(int)})
# )

depo_values = [['New Energy Bank', 1_000_000_000, 8.30, 'O/N'],
               ['Cryptocurrencybank', 2_500_000_000, 8.35, 'O/N'],
               ['Big Business Bank', 1_500_000_000, 8.27, 'O/N'],
               ['GreenEnergyBank', 1_800_000_000, 8.35, 'O/N'],
               ['Allmoneybank', 5_900_000_000, 8.45, 'O/N'],
               ['ClearWaterBank', 3_000_000_000, 8.40, 'O/N'],
               ['First Ecologic Bank', 3_000_000_000, 8.41, 'O/N'],
               ['Cryptocurrencybank', 7_500_000_000, 8.50, 'O/N'],
               ['Big Business Bank', 2_500_000_000, 8.35, 'O/N'],
               ['AgroFoodBank', 700_000_000, 8.25, 'O/N'],
               ['Golden Silver Bank', 4_300_000_000, 8.42, 'O/N'],
               ['SmallBusinessBank', 2_000_000_000, 8.31, 'O/N']]
depo_columns = ['Банк', 'Сумма, руб.', 'Ставка', 'Срок']
depo = pd.DataFrame(depo_values, columns=depo_columns)

limits_values = [['AgroFoodBank', 5],
                ['Allmoneybank', 8],
                ['Big Business Bank', 7.5],
                ['ClearWaterBank', 9],
                ['Cryptocurrencybank', 10],
                ['First Ecologic Bank', 4.5],
                ['Golden Silver Bank', 10],
                ['GreenEnergyBank', 2],
                ['New Energy Bank', 5],
                ['SmallBusinessBank', 3]]
limits_columns = ['Банк', 'Лимит, млрд руб.']
limits = pd.DataFrame(limits_values, columns=limits_columns)

# print(
#         limits
#         .merge(depo.groupby('Банк').apply(lambda x: 
#                 pd.Series({'Остаток лимита, млрд руб.': x['Сумма, руб.'].sum()})), on='Банк')
#         .assign(**{'Остаток лимита, млрд руб.': lambda x: (x['Лимит, млрд руб.'] * 1_000_000_000 - x['Остаток лимита, млрд руб.']) / 1_000_000_000})
# )

currency_values = [['CNYRUB_TOM', 12.894, 1_000_000, 'купля'],
                   ['CNYRUB_TOM', 12.905, 2_000_000, 'купля'],
                   ['USDRUB_TOM', 94.15, 500_000, 'продажа'],
                   ['EURRUB_TOM', 102.76, 200_000, 'купля'],
                   ['USDRUB_TOM', 94.15, 500_000, 'купля'],
                   ['USDRUB_TOM', 94.18, 100_000, 'купля'],
                   ['CNYRUB_TOM', 12.91, 500_000, 'продажа'],
                   ['EURRUB_TOM', 102.74, 50_000, 'купля'],
                   ['USDRUB_TOM', 94.21, 200_000, 'купля'],
                   ['USDRUB_TOM', 94.215, 20_000, 'продажа'],
                   ['CNYRUB_TOM', 12.90, 100_000, 'купля'],
                   ['USDRUB_TOM', 94.24, 300_000, 'продажа']]
currency_columns = ['Валютная пара', 'Цена', 'Объем в валюте', 'Направление сделки']
currency = pd.DataFrame(currency_values, columns=currency_columns)

# print(
#         currency
#         .query('`Направление сделки` == "купля"')
#         .groupby('Валютная пара')
#         .agg({'Объем в валюте': 'count'})
#         .rename({'Объем в валюте': 'Количество сделок'}, axis=1)
# )

currency_values = [['CNYRUB_TOM', 12.894, 1_000_000, 'купля'],
                   ['CNYRUB_TOM', 12.905, 2_000_000, 'купля'],
                   ['USDRUB_TOM', 94.15, 500_000, 'продажа'],
                   ['EURRUB_TOM', 102.76, 200_000, 'купля'],
                   ['USDRUB_TOM', 94.15, 500_000, 'купля'],
                   ['USDRUB_TOM', 94.18, 100_000, 'купля'],
                   ['CNYRUB_TOM', 12.91, 500_000, 'продажа'],
                   ['EURRUB_TOM', 102.74, 50_000, 'купля'],
                   ['USDRUB_TOM', 94.21, 200_000, 'купля'],
                   ['USDRUB_TOM', 94.215, 20_000, 'продажа'],
                   ['CNYRUB_TOM', 12.90, 100_000, 'купля'],
                   ['USDRUB_TOM', 94.24, 300_000, 'продажа']]
currency_columns = ['Валютная пара', 'Цена', 'Объем в валюте', 'Направление сделки']
currency = pd.DataFrame(currency_values, columns=currency_columns)

# print(
#         pd.Series(
#         currency
#         .groupby('Направление сделки')
#         .agg({'Цена': 'count'}), name='Направление сделки'
#         )
# )

# print(
#         currency
#         ['Направление сделки']
#         .value_counts()
# )

# print(
#         currency
#         .groupby('Направление сделки')
#         .agg({'Направление сделки': 'count'})
#         ['Направление сделки']
# )

currency_values = [['CNYRUB_TOM', 12.894, 1_000_000, 'купля'],
                   ['CNYRUB_TOM', 12.905, 2_000_000, 'купля'],
                   ['USDRUB_TOM', 94.15, 500_000, 'продажа'],
                   ['EURRUB_TOM', 102.76, 200_000, 'купля'],
                   ['USDRUB_TOM', 94.15, 500_000, 'купля'],
                   ['USDRUB_TOM', 94.18, 100_000, 'купля'],
                   ['CNYRUB_TOM', 12.91, 500_000, 'продажа'],
                   ['EURRUB_TOM', 102.74, 50_000, 'купля'],
                   ['USDRUB_TOM', 94.21, 200_000, 'купля'],
                   ['USDRUB_TOM', 94.215, 20_000, 'продажа'],
                   ['CNYRUB_TOM', 12.90, 100_000, 'купля'],
                   ['USDRUB_TOM', 94.24, 300_000, 'продажа']]
currency_columns = ['Валютная пара', 'Цена', 'Объем в валюте', 'Направление сделки']
currency = pd.DataFrame(currency_values, columns=currency_columns)

# print(
#         currency
#         .groupby(['Валютная пара', 'Направление сделки'])
#         .agg({'Объем в валюте': 'sum'})
# )

currency_values = [['CNYRUB_TOM', 12.894, 1_000_000, 'купля'],
                   ['CNYRUB_TOM', 12.905, 2_000_000, 'купля'],
                   ['USDRUB_TOM', 94.15, 500_000, 'продажа'],
                   ['EURRUB_TOM', 102.76, 200_000, 'купля'],
                   ['USDRUB_TOM', 94.15, 500_000, 'купля'],
                   ['USDRUB_TOM', 94.18, 100_000, 'купля'],
                   ['CNYRUB_TOM', 12.91, 500_000, 'продажа'],
                   ['EURRUB_TOM', 102.74, 50_000, 'купля'],
                   ['USDRUB_TOM', 94.21, 200_000, 'купля'],
                   ['USDRUB_TOM', 94.215, 20_000, 'продажа'],
                   ['CNYRUB_TOM', 12.90, 100_000, 'купля'],
                   ['USDRUB_TOM', 94.24, 300_000, 'продажа']]
currency_columns = ['Валютная пара', 'Цена', 'Объем в валюте', 'Направление сделки']
currency = pd.DataFrame(currency_values, columns=currency_columns)

# print(
#         currency
#         .groupby(['Валютная пара', 'Направление сделки'])
#         .apply(lambda x: pd.Series({'Средневзвешенная': np.average(x['Цена'], weights=x['Объем в валюте']).round(4)}))
# )

currency_values = [['CNYRUB_TOM', 12.894, 1_000_000, 'купля'],
                   ['CNYRUB_TOM', 12.905, 2_000_000, 'купля'],
                   ['USDRUB_TOM', 94.15, 500_000, 'продажа'],
                   ['EURRUB_TOM', 102.76, 200_000, 'купля'],
                   ['USDRUB_TOM', 94.15, 500_000, 'купля'],
                   ['USDRUB_TOM', 94.18, 100_000, 'купля'],
                   ['CNYRUB_TOM', 12.91, 500_000, 'продажа'],
                   ['EURRUB_TOM', 102.74, 50_000, 'купля'],
                   ['USDRUB_TOM', 94.21, 200_000, 'купля'],
                   ['USDRUB_TOM', 94.215, 20_000, 'продажа'],
                   ['CNYRUB_TOM', 12.90, 100_000, 'купля'],
                   ['USDRUB_TOM', 94.24, 300_000, 'продажа']]
currency_columns = ['Валютная пара', 'Цена', 'Объем в валюте', 'Направление сделки']
currency = pd.DataFrame(currency_values, columns=currency_columns)

print(
        currency
        .groupby(['Валютная пара', 'Направление сделки'])
        .apply(lambda x: pd.Series({'Объем в валюте': x['Объем в валюте'].sum(), 'Средневзвешенная': np.average(x['Цена'], weights=x['Объем в валюте']).round(4)}))
        .assign(**{'Объем в валюте': lambda x: x['Объем в валюте'].map(int)})
)