import pandas as pd 

tsla_values = [['2022-01-01', 382.58, 402.67, 264.0, 312.24, 1916006400],
       ['2022-02-01', 311.74, 315.92, 233.33, 290.14, 1391126700],
       ['2022-03-01', 289.89, 371.59, 252.01, 359.2, 1729272900],
       ['2022-04-01', 360.38, 384.29, 273.9, 290.25, 1520959800],
       ['2022-05-01', 286.92, 318.5, 206.86, 252.75, 1948221600],
       ['2022-06-01', 251.72, 264.21, 208.69, 224.47, 2011227900],
       ['2022-07-01', 227.0, 298.32, 216.17, 297.15, 1744884000],
       ['2022-08-01', 301.28, 314.67, 271.81, 275.61, 1695263200],
       ['2022-09-01', 272.58, 313.8, 262.47, 265.25, 1299271000],
       ['2022-10-01', 254.5, 257.5, 198.59, 227.54, 1735263100],
       ['2022-11-01', 234.05, 237.4, 166.19, 194.7, 1885275300],
       ['2022-12-01', 197.08, 198.92, 108.24, 123.18, 2944247700],
       ['2023-01-01', 118.47, 180.68, 101.81, 173.22, 3897499400],
       ['2023-02-01', 173.89, 217.65, 169.93, 205.71, 3624845100],
       ['2023-03-01', 206.21, 207.79, 163.91, 207.46, 3311619900],
       ['2023-04-01', 199.91, 202.69, 152.37, 164.31, 2505176300],
       ['2023-05-01', 163.17, 204.48, 158.83, 203.93, 2681994800],
       ['2023-06-01', 202.59, 276.99, 199.37, 261.77, 3440477900]]
tsla_columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
tsla = pd.DataFrame(tsla_values, columns=tsla_columns)

aapl_values = [['2022-01-01', 177.83, 182.94, 154.7, 174.78, 2108446000],
       ['2022-02-01', 174.01, 176.65, 152.0, 165.12, 1627516300],
       ['2022-03-01', 164.7, 179.61, 150.1, 174.61, 2180800100],
       ['2022-04-01', 174.03, 178.49, 155.38, 157.65, 1687795600],
       ['2022-05-01', 156.71, 166.48, 132.61, 148.84, 2401040300],
       ['2022-06-01', 149.9, 151.74, 129.04, 136.72, 1749099800],
       ['2022-07-01', 136.04, 163.63, 135.66, 162.51, 1447125400],
       ['2022-08-01', 161.01, 176.15, 157.14, 157.22, 1510239600],
       ['2022-09-01', 156.64, 164.26, 138.0, 138.2, 2084722800],
       ['2022-10-01', 138.21, 157.5, 134.37, 153.34, 1868139700],
       ['2022-11-01', 155.08, 155.45, 134.38, 148.03, 1724847700],
       ['2022-12-01', 148.21, 150.92, 125.87, 129.93, 1675731200],
       ['2023-01-01', 130.28, 147.23, 124.17, 144.29, 1443652500],
       ['2023-02-01', 143.97, 157.38, 141.32, 147.41, 1307198900],
       ['2023-03-01', 146.83, 165.0, 143.9, 164.9, 1520266600],
       ['2023-04-01', 164.27, 169.85, 159.78, 169.68, 969709700],
       ['2023-05-01', 169.28, 179.35, 164.31, 177.25, 1275155500],
       ['2023-06-01', 177.7, 194.48, 176.93, 193.97, 1297101100]]
aapl_columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
aapl = pd.DataFrame(aapl_values, columns=aapl_columns)

# print(
#     tsla
#     .query('Date.astype("datetime64[ns]").dt.year == 2022')
# ['Volume'].sum()
# )
# print(
#     aapl
#     .query('Date.astype("datetime64[ns]").dt.year == 2022')
# ['Volume'].sum()
# )

# -------------------------------------------------
# import numpy as np
# moscow_exchange_values = [['2023-03-01', 2279.65, 2258.89, 2287.48, 2255.45, 1.18],
#        ['2023-03-02', 2254.3, 2284.87, 2286.27, 2235.43, -1.11],
#        ['2023-03-03', 2272.2, 2250.12, 2273.52, 2249.81, 0.79],
#        ['2023-03-06', 2294.12, 2286.2, 2297.86, 2283.4, 0.96],
#        ['2023-03-07', 2295.6, 2294.32, 2298.93, 2281.46, 0.06],
#        ['2023-03-09', 2290.14, 2295.03, 2302.1, 2278.95, -0.24],
#        ['2023-03-10', 2276.25, 2272.61, 2283.18, 2266.33, -0.61]]
# moscow_exchange_columns = ['Дата', 'Цена', 'Откр.', 'Макс.', 'Мин.', 'Изм. %']
# moex = pd.DataFrame(moscow_exchange_values, columns=moscow_exchange_columns)  

# moex = (
#     moex
#     .set_index('Дата')
#     .transpose()
# )

# print(moex['2023-03-01'])
# print()
# print(moex[['2023-03-01', '2023-03-06']])

# ----------------------------------------------------------------------
# pmi_manufacturing_germany_values = [['03.07.2023 (июнь)', 40.6, 41.0, 43.2],
#        ['01.06.2023 (май)', 43.2, 42.9, 44.5], ['02.05.2023 (апр)', 44.5, 44.0, 44.7],
#        ['03.04.2023 (мар)', 44.7, 44.4, 46.3], ['01.03.2023 (фев)', 46.3, 46.5, 46.5],
#        ['01.02.2023 (янв)', 47.3, 47.0, 47.1], ['02.01.2023 (дек)', 47.1, 47.4, 46.2],
#        ['01.12.2022 (нояб)', 46.2, 46.7, 45.1], ['02.11.2022 (окт)', 45.1, 45.7, 47.8],
#        ['03.10.2022 (сент)', 47.8, 48.3, 49.1], ['01.09.2022 (авг)', 49.1, 49.8, 49.3],
#        ['01.08.2022 (июль)', 49.3, 49.2, 52.0], ['01.07.2022 (июнь)', 52.0, 52.0, 54.8],
#        ['01.06.2022 (май)', 54.8, 54.7, 54.6], ['02.05.2022 (апр)', 54.6, 54.1, 56.9],
#        ['01.04.2022 (мар)', 56.9, 57.6, 57.6], ['01.03.2022 (фев)', 58.4, 58.5, 59.8],
#        ['01.02.2022 (янв)', 59.8, 60.5, 57.4], ['03.01.2022 (дек)', 57.4, 57.9, 57.4],
#        ['01.12.2021 (нояб)', 57.4, 57.6, 57.6], ['02.11.2021 (окт)', 57.8, 58.2, 58.4],
#        ['01.10.2021 (сент)', 58.4, 58.5, 62.6], ['01.09.2021 (авг)', 62.6, 62.7, 65.9],
#        ['02.08.2021 (июль)', 65.9, 65.6, 65.1], ['01.07.2021 (июнь)', 65.1, 64.9, 64.4],
#        ['01.06.2021 (май)', 64.4, 64.0, 66.2], ['03.05.2021 (апр)', 66.2, 66.4, 66.4],
#        ['01.04.2021 (мар)', 66.6, 66.6, 60.7], ['01.03.2021 (фев)', 60.7, 60.6, 57.1],
#        ['01.02.2021 (янв)', 57.1, 57.0, 58.3]]
# pmi_manufacturing_germany_columns = ['Дата выпуска', 'Факт.', 'Прогноз', 'Пред.']
# pmi_manufacturing_germany = pd.DataFrame(pmi_manufacturing_germany_values, 
#                                         columns=pmi_manufacturing_germany_columns)

# print(pmi_manufacturing_germany
#     .assign(date = pd.to_datetime(pmi_manufacturing_germany['Дата выпуска']                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
#     .str.split(expand=True)[0], format="%d.%m.%Y"))
#     .query('(date <= "2023-01-02") and (date >= "2022.02.01")')
#     .drop('date', axis=1)
# )
# ------------------------------------------------------------------------------
# pmi_services_germany_values = [['05.07.2023 (июнь)', 54.1, 54.1, 57.2],
#        ['05.06.2023 (май)', 57.2, 57.8, 56.0], ['04.05.2023 (апр)', 56.0, 55.7, 53.7],
#        ['05.04.2023 (мар)', 53.7, 53.9, 50.9], ['03.03.2023 (фев)', 50.9, 51.3, 50.7],
#        ['03.02.2023 (янв)', 50.7, 50.4, 49.2], ['04.01.2023 (дек)', 49.2, 49.0, 46.1],
#        ['05.12.2022 (нояб)', 46.1, 46.4, 46.5], ['04.11.2022 (окт)', 46.5, 44.9, 45.0],
#        ['05.10.2022 (сент)', 45.0, 45.4, 47.7], ['05.09.2022 (авг)', 47.7, 48.2, 49.7],
#        ['03.08.2022 (июль)', 49.7, 49.2, 52.4], ['05.07.2022 (июнь)', 52.4, 52.4, 55.0],
#        ['03.06.2022 (май)', 55.0, 56.3, 56.3], ['04.05.2022 (апр)', 57.6, 57.9, 56.1],
#        ['05.04.2022 (мар)', 56.1, 55.0, 55.8], ['03.03.2022 (фев)', 55.8, 56.6, 52.2],
#        ['03.02.2022 (янв)', 52.2, 52.2, 48.7], ['05.01.2022 (дек)', 48.7, 48.4, 52.7],
#        ['03.12.2021 (нояб)', 52.7, 53.4, 52.4], ['04.11.2021 (окт)', 52.4, 52.4, 56.2],
#        ['05.10.2021 (сент)', 56.2, 56.0, 60.8], ['03.09.2021 (авг)', 60.8, 61.5, 61.8],
#        ['04.08.2021 (июль)', 61.8, 62.2, 57.5], ['05.07.2021 (июнь)', 57.5, 58.1, 52.8],
#        ['03.06.2021 (май)', 52.8, 52.8, 52.8], ['05.05.2021 (апр)', 49.9, 50.1, 51.5],
#        ['07.04.2021 (мар)', 51.5, 50.8, 45.7], ['03.03.2021 (фев)', 45.7, 45.9, 46.7],
#        ['03.02.2021 (янв)', 46.7, 46.8, 46.8]]
# pmi_services_germany_columns = ['Дата выпуска', 'Факт.', 'Прогноз', 'Пред.']
# pmi_services_germany = pd.DataFrame(pmi_services_germany_values, 
#                                         columns=pmi_services_germany_columns)

# print(pmi_services_germany
#     .assign(date = pd.to_datetime(pmi_services_germany['Дата выпуска']                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
#     .str.split(expand=True)[0], format="%d.%m.%Y"))
#     .query('(date <= "2023-01-05") and (date >= "2022.02.01")')
#     .drop('date', axis=1)[['Дата выпуска', 'Факт.']].iloc[::-1].reset_index(drop=True)
# )
# -------------------------------------------------------------------
# pmi_manufacturing_values = [['июнь 2023', 40.6, 46.0, 48.0, 45.1, 51.5],
#        ['май 2023', 43.2, 45.7, 47.4, 47.0, 51.5], ['апр 2023', 44.5, 45.6, 51.2, 46.6, 51.5],
#        ['мар 2023', 44.7, 47.3, 48.3, 48.3, 50.9], ['фев 2023', 46.3, 47.4, 47.5, 48.5, 50.1],
#        ['янв 2023', 47.3, 50.5, 50.0, 47.5, 50.1], ['дек 2022', 47.1, 49.2, 50.0, 45.6, 48.1],
#        ['нояб 2022', 46.2, 48.3, 51.2, 43.4, 45.7], ['окт 2022', 45.1, 47.2, 53.1, 42.0, 46.4],
#        ['сент 2022', 47.8, 47.7, 50.0, 43.0, 46.9], ['авг 2022', 49.1, 50.6, 52.3, 40.9, 47.4],
#        ['июль 2022', 49.3, 49.5, 54.6, 42.1, 46.9], ['июнь 2022', 52.0, 51.4, 56.4, 44.4, 48.1],
#        ['май 2022', 54.8, 54.6, 54.9, 48.5, 49.2], ['апр 2022', 54.6, 55.7, 60.6, 52.4, 49.2],
#        ['мар 2022', 56.9, 54.7, 59.6, 52.7, 49.4], ['фев 2022', 58.4, 57.2, 55.9, 54.7, 50.4],
#        ['янв 2022', 59.8, 55.5, 56.5, 54.5, 50.5], ['дек 2021', 57.4, 55.6, 58.0, 56.1, 52.1],
#        ['нояб 2021', 57.4, 55.9, 63.7, 54.4, 52.0], ['окт 2021', 57.8, 53.6, 58.5, 53.8, 51.2],
#        ['сент 2021', 58.4, 55.0, 59.2, 53.4, 52.5], ['авг 2021', 62.6, 57.5, 62.2, 56.0, 54.1],
#        ['июль 2021', 65.9, 58.0, 63.3, 57.6, 54.0], ['июнь 2021', 65.1, 59.0, 60.8, 59.4, 51.3],
#        ['май 2021', 64.4, 59.4, 58.5, 57.2, 49.3], ['апр 2021', 66.2, 58.9, 59.1, 53.7, 50.4],
#        ['мар 2021', 66.6, 59.3, 60.4, 54.3, 52.6], ['фев 2021', 60.7, 56.1, 56.1, 53.4, 51.7],
#        ['янв 2021', 57.1, 51.6, 51.8, 51.9, 54.4]]
# pmi_manufacturing_columns = ['Период', 'Факт_Германия', 'Факт_Франция', 'Факт_Норвегия',
#                              'Факт_Польша', 'Факт_Турция']
# pmi_manufacturing = pd.DataFrame(pmi_manufacturing_values, columns=pmi_manufacturing_columns)

# import locale
# import calendar
# locale.setlocale(locale.LC_TIME, 'ru_RU.utf8')
# month_names = [x[:3] for x in calendar.month_name if x]
# month_names[4] = 'май'
# print(month_names)

# print(
#     pmi_manufacturing[['Период', 'Факт_Германия', 'Факт_Франция']]
#     .assign(year = pmi_manufacturing['Период'].str.split(expand=True)[1].astype('int64'))
#     .assign(month = pmi_manufacturing['Период']
#         .str.split(expand=True)[0].str.lower().str[:3])
#     .query(f'(year == 2023) and (month.isin({month_names[:6]}))')
#     .drop(['year', 'month'], axis=1)
# )
#------------------------------------------------------------------
# depo_values = [['New Energy Bank', 1_000_000_000, 8.30, 'O/N'],
#                ['AgroFoodBank', 5_000_000_000, 8.50, '1W'],
#                ['First Ecologic Bank', 4_500_000_000, 8.60, '1M'],
#                ['Cryptocurrencybank', 2_700_000_000, 8.30, 'O/N'],
#                ['GreenEnergyBank', 1_800_000_000, 8.35, 'O/N'],
#                ['ClearWaterBank', 3_000_000_000, 8.40, 'O/N'],
#                ['First Ecologic Bank', 3_000_000_000, 8.41, 'O/N'],
#                ['Cryptocurrencybank', 7_500_000_000, 8.50, 'O/N'],
#                ['Golden Silver Bank', 2_500_000_000, 8.65, '1M'],
#                ['New Energy Bank', 2_000_000_000, 8.45, '1W'],
#                ['AgroFoodBank', 700_000_000, 8.25, 'O/N'],
#                ['Golden Silver Bank', 4_300_000_000, 8.40, 'O/N'],
#                ['New Energy Bank', 4_000_000_000, 8.80, '3M']]
# depo_columns = ['Банк', 'Сумма, руб.', 'Ставка', 'Срок']
# depo = pd.DataFrame(depo_values, columns=depo_columns)

# depo.loc[len(depo.index)] = ['Golden Silver Bank', 500_000_000, 8.20, 'O/N']
# print(depo)
# ------------------------------------------------------------------------
pmi_manufacturing_values = [['июнь 2023', 52.6, 57.8, 49.0, 46.0, 43.4],
       ['май 2023', 53.5, 58.7, 48.8, 46.9, 44.8], ['апр 2023', 52.6, 57.2, 49.2, 47.1, 45.8],
       ['мар 2023', 53.2, 56.4, 51.9, 46.3, 47.3], ['фев 2023', 53.6, 55.3, 52.6, 47.7, 48.5],
       ['янв 2023', 52.6, 55.4, 50.1, 47.4, 48.8], ['дек 2022', 53.0, 57.8, 47.0, 48.4, 47.8],
       ['нояб 2022', 53.2, 55.7, 48.0, 49.0, 47.1], ['окт 2022', 50.7, 55.3, 49.2, 50.2, 46.4],
       ['сент 2022', 52.0, 55.1, 50.1, 50.9, 48.4], ['авг 2022', 51.7, 56.2, 49.4, 52.8, 49.6],
       ['июль 2022', 50.3, 56.4, 49.0, 52.8, 49.8], ['июнь 2022', 50.9, 53.9, 50.2, 53.0, 52.1],
       ['май 2022', 50.8, 54.6, 49.6, 56.1, 54.6], ['апр 2022', 48.2, 54.7, 47.4, 55.4, 55.5],
       ['мар 2022', 44.1, 54.0, 49.5, 57.1, 56.5], ['фев 2022', 48.6, 54.9, 50.2, 58.6, 58.2],
       ['янв 2022', 51.8, 54.0, 50.1, 57.6, 58.7], ['дек 2021', 51.6, 55.5, 50.3, 58.7, 58.0],
       ['нояб 2021', 51.7, 57.6, 50.1, 61.1, 58.4], ['окт 2021', 51.6, 55.9, 49.2, 60.8, 58.3],
       ['сент 2021', 49.8, 53.7, 49.6, 61.1, 58.6], ['авг 2021', 46.5, 52.3, 50.1, 59.9, 61.4],
       ['июль 2021', 47.5, 55.3, 50.4, 59.5, 62.8], ['июнь 2021', 49.2, 48.1, 50.9, 60.6, 63.4],
       ['май 2021', 51.9, 50.8, 51.0, 61.2, 63.1], ['апр 2021', 50.4, 55.5, 51.1, 60.7, 62.9],
       ['мар 2021', 51.1, 55.4, 51.9, 64.7, 62.5], ['фев 2021', 51.5, 57.5, 50.6, 60.8, 57.9],
       ['янв 2021', 50.9, 57.7, 51.3, 58.7, 54.8]]
pmi_manufacturing_columns = ['Период', 'Факт_Россия', 'Факт_Индия', 'Факт_Китай', 'Факт_США', 'Факт_еврозона']
pmi_manufacturing = pd.DataFrame(pmi_manufacturing_values, columns=pmi_manufacturing_columns)

print(pmi_manufacturing.loc[:, 'Период':'Факт_Китай'])