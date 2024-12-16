import pandas as pd 
import numpy as np 

df_values = [['AMEZ', 'ПАО "Ашинский метзавод"', 'ао', 51480414016, 'металлургия'],
       ['BSPB', 'ПАО "Банк "Санкт-Петербург"', 'ао', 134333130048, 'банк'],
       ['BSPBP', 'ПАО "Банк "Санкт-Петербург"', 'ап', 1234140000, 'банк'],
       ['CHMF', 'ПАО "Северсталь"', 'ао', 1147004389272, 'металлургия'],
       ['CHMK', 'ПАО "ЧМК"', 'ао', 35398198175, 'металлургия'],
       ['GMKN', 'ПАО "ГМК "Норильский никель"', 'ао', 2474552670636, 'металлургия'],
       ['MAGN', 'ПАО "ММК"', 'ао', 583970485800, 'металлургия'],
       ['MTLR', 'ПАО "Мечел"', 'ао', 85098228400, 'металлургия'],
       ['MTLRP', 'ПАО "Мечел"', 'ап', 31456192630, 'металлургия'],
       ['NLMK', 'ПАО "НЛМК"', 'ао', 1255940700414, 'металлургия'],
       ['ROSB', 'ПАО РОСБАНК', 'ао', 158242989006, 'банк'],
       ['RUAL', 'МКПАО "ОК РУСАЛ"', 'ао', 626180107537, 'металлургия'],
       ['SBER', 'ПАО Сбербанк', 'ао', 5628796691000, 'банк'],
       ['SBERP', 'ПАО Сбербанк', 'ап', 260380000000, 'банк'],
       ['TRMK', 'ПАО "ТМК"', 'ао', 229500690203, 'металлургия'],
       ['USBN', 'ПАО "БАНК УРАЛСИБ"', 'ао', 71090589258, 'банк'],
       ['VTBR', 'Банк ВТБ (ПАО)', 'ао', 693929707327, 'банк']]
df_columns = ['Торговый код', 'Эмитент', 'Тип',
              'Капитализация, руб.', 'Отрасль']
df = pd.DataFrame(df_values, columns=df_columns)

print(
    df
    .query('Эмитент.duplicated(keep=False)')
    .reset_index(drop=True)
    [['Эмитент', 'Тип', 'Капитализация, руб.']] 
)

# ------------------------------------------------------
depo_values = [['New Energy Bank', 500_000_000, 8.15, 'П', 'O/N'],
               ['AgroFoodBank', 1_000_000_000, 8.20, 'П', 'O/N'],
               ['First Ecologic Bank', 400_000_000, 8.11, 'П', 'O/N'],
               ['Cryptocurrencybank', 700_000_000, 8.15, 'П', 'O/N'],
               ['Big Business Bank', 2_600_000_000, 8.30, 'Р', 'O/N'],
               ['SmallBusinessBank', 2_000_000_000, 8.20, 'П', 'O/N'],
               ['GreenEnergyBank', 1_000_000_000, 8.10, 'П', 'O/N'],
               ['Allmoneybank', 3_000_000_000, 8.27, 'Р', 'O/N'],
               ['ClearWaterBank', 300_000_000, 8.00, 'П', 'O/N'],
               ['First Ecologic Bank', 700_000_000, 8.15, 'П', 'O/N'],
               ['Cryptocurrencybank', 500_000_000, 8.15, 'П', 'O/N'],
               ['Allmoneybank', 1_500_000_000, 8.20, 'Р', 'O/N'],
               ['Golden Silver Bank', 800_000_000, 8.05, 'П', 'O/N'],
               ['New Energy Bank', 300_000_000, 8.00, 'П', 'O/N'],
               ['AgroFoodBank', 400_000_000, 8.00, 'П', 'O/N'],
               ['Golden Silver Bank', 500_000_000, 8.03, 'П', 'O/N'],
               ['SmallBusinessBank', 400_000_000, 8.00, 'П', 'O/N'],
               ['New Energy Bank', 500_000_000, 7.90, 'П', 'O/N'],
               ['Big Business Bank', 2_900_000_000, 8.15, 'Р', 'O/N']]
depo_columns = ['Банк', 'Сумма, руб.', 'Ставка', 'Направление', 'Срок']
depo = pd.DataFrame(depo_values, columns=depo_columns)

print(
    depo
    .query('Направление == "П"')
    .query('~Банк.duplicated()')
    .sort_values('Банк')
    ['Банк']
    .tolist()
)
print(
    depo
    .query('Направление == "Р"')
    .query('~Банк.duplicated()')
    .sort_values('Банк')
    ['Банк']
    .tolist()
)
# -----------------------------------------------------------
df_values = [['БО-002Р-03', 'ПАО «Магнит»', '22.05.2020', '19.05.2023', '15 млрд. руб.', '5,90%'],
             ['БО-002Р-02', 'ПАО «Магнит»', '29.04.2020', '26.04.2023', '10 млрд. руб.', '6,70%'],
             ['БО-002Р-01', 'ПАО «Магнит»', '05.03.2020', '02.03.2023', '15 млрд. руб.', '6,20%'],
             ['БО-003Р-05', 'ПАО «Магнит»', '26.12.2019', '22.12.2022', '10 млрд. руб.', '6,60%'],
             ['БО-003Р-04', 'ПАО «Магнит»', '05.11.2019', '03.05.2022', '10 млрд. руб.', '6,90%'],
             ['БО-003Р-01', 'ПАО «Магнит»', '05.02.2019', '01.02.2022', '10 млрд. руб.', '8,70%'],
             ['БО-003Р-02', 'ПАО «Магнит»', '26.02.2019', '23.02.2021', '10 млрд. руб.', '8,50%'],
             ['БО-003Р-03', 'ПАО «Магнит»', '27.06.2019', '24.12.2020', '10 млрд. руб.', '7,85%'],
             ['БО-001Р-04', 'ПАО «Магнит»', '05.07.2016', '28.12.2017', '10 млрд. руб.', '10,00%'],
             ['БО-001Р-03', 'ПАО «Магнит»', '12.04.2016', '10.04.2018', '10 млрд. руб.', '10,60%'],
             ['БО-001Р-02', 'ПАО «Магнит»', '29.02.2016', '26.02.2018', '10 млрд. руб.', '11,20%'],
             ['БО-001Р-01', 'ПАО «Магнит»', '11.11.2015', '10.05.2017', '10 млрд. руб.', '11,20%'],
             ['БO-11', 'ПАО «Магнит»', '20.10.2015', '18.04.2017', '10 млрд. руб.', '11,70%'],
             ['БO-10', 'ПАО «Магнит»', '23.07.2015', '21.07.2016', '10 млрд. руб.', '11,60%'],
             ['03', 'ПАО «Магнит»', '15.05.2015', '13.05.2016', '5 млрд. руб.', '12,10%'],
             ['02', 'ПАО «Магнит»', '15.05.2015', '13.05.2016', '5 млрд. руб.', '12,10%'],
             ['БO-09', 'ПАО «Магнит»', '02.04.2013', '29.03.2016', '5 млрд. руб.', '8,40%'],
             ['БO-08', 'ПАО «Магнит»', '02.04.2013', '29.03.2016', '5 млрд. руб.', '8,40%'],
             ['01', 'ПАО «Магнит»', '26.02.2013', '23.02.2016', '5 млрд. руб.', '8,50%'],
             ['БO-07', 'ПАО «Магнит»', '24.09.2012', '21.09.2015', '5 млрд. руб.', '8,90%'],
             ['БO-06', 'ПАО «Магнит»', '26.04.2011', '22.04.2014', '5 млрд. руб.', '7,75%'],
             ['БO-05', 'ПАО «Магнит»', '04.03.2011', '28.02.2014', '5 млрд. руб.', '8,00%'],
             ['БO-04', 'ПАО «Магнит»', '13.09.2010', '09.09.2013', '2 млрд. руб.', '8,25%'],
             ['БO-03', 'ПАО «Магнит»', '13.09.2010', '09.09.2013', '1,5 млрд. руб.', '8,25%'],
             ['БO-02', 'ПАО «Магнит»', '13.09.2010', '09.09.2013', '1 млрд. руб.', '8,25%'],
             ['БO-01', 'ПАО «Магнит»', '13.09.2010', '09.09.2013', '1 млрд. руб.', '8,25%'],
             ['02', 'ООО «Магнит Финанс»', '30.03.2007', '23.03.2012', '5 млрд. руб.', '8,20%'],
             ['01', 'ООО «Магнит Финанс»', '23.11.2005', '19.11.2008', '2 млрд. руб.', '9,34%']]
df_columns = ['Серия', 'Эмитент', 'Дата размещения', 'Дата погашения',
              'Объем выпуска', 'Ставка купона']
df = pd.DataFrame(df_values, columns=df_columns)

print(
    df
    .query('~`Объем выпуска`.duplicated()')
    ['Объем выпуска']
    .tolist()
)
# --------------------------------------------------------
df_values = [['БО-002Р-03', 'ПАО «Магнит»', '22.05.2020', '19.05.2023', '15 млрд. руб.', '5,90%'],
             ['БО-002Р-02', 'ПАО «Магнит»', '29.04.2020', '26.04.2023', '10 млрд. руб.', '6,70%'],
             ['БО-002Р-01', 'ПАО «Магнит»', '05.03.2020', '02.03.2023', '15 млрд. руб.', '6,20%'],
             ['БО-003Р-05', 'ПАО «Магнит»', '26.12.2019', '22.12.2022', '10 млрд. руб.', '6,60%'],
             ['БО-003Р-04', 'ПАО «Магнит»', '05.11.2019', '03.05.2022', '10 млрд. руб.', '6,90%'],
             ['БО-003Р-01', 'ПАО «Магнит»', '05.02.2019', '01.02.2022', '10 млрд. руб.', '8,70%'],
             ['БО-003Р-02', 'ПАО «Магнит»', '26.02.2019', '23.02.2021', '10 млрд. руб.', '8,50%'],
             ['БО-003Р-03', 'ПАО «Магнит»', '27.06.2019', '24.12.2020', '10 млрд. руб.', '7,85%'],
             ['БО-001Р-04', 'ПАО «Магнит»', '05.07.2016', '28.12.2017', '10 млрд. руб.', '10,00%'],
             ['БО-001Р-03', 'ПАО «Магнит»', '12.04.2016', '10.04.2018', '10 млрд. руб.', '10,60%'],
             ['БО-001Р-02', 'ПАО «Магнит»', '29.02.2016', '26.02.2018', '10 млрд. руб.', '11,20%'],
             ['БО-001Р-01', 'ПАО «Магнит»', '11.11.2015', '10.05.2017', '10 млрд. руб.', '11,20%'],
             ['БO-11', 'ПАО «Магнит»', '20.10.2015', '18.04.2017', '10 млрд. руб.', '11,70%'],
             ['БO-10', 'ПАО «Магнит»', '23.07.2015', '21.07.2016', '10 млрд. руб.', '11,60%'],
             ['03', 'ПАО «Магнит»', '15.05.2015', '13.05.2016', '5 млрд. руб.', '12,10%'],
             ['02', 'ПАО «Магнит»', '15.05.2015', '13.05.2016', '5 млрд. руб.', '12,10%'],
             ['БO-09', 'ПАО «Магнит»', '02.04.2013', '29.03.2016', '5 млрд. руб.', '8,40%'],
             ['БO-08', 'ПАО «Магнит»', '02.04.2013', '29.03.2016', '5 млрд. руб.', '8,40%'],
             ['01', 'ПАО «Магнит»', '26.02.2013', '23.02.2016', '5 млрд. руб.', '8,50%'],
             ['БO-07', 'ПАО «Магнит»', '24.09.2012', '21.09.2015', '5 млрд. руб.', '8,90%'],
             ['БO-06', 'ПАО «Магнит»', '26.04.2011', '22.04.2014', '5 млрд. руб.', '7,75%'],
             ['БO-05', 'ПАО «Магнит»', '04.03.2011', '28.02.2014', '5 млрд. руб.', '8,00%'],
             ['БO-04', 'ПАО «Магнит»', '13.09.2010', '09.09.2013', '2 млрд. руб.', '8,25%'],
             ['БO-03', 'ПАО «Магнит»', '13.09.2010', '09.09.2013', '1,5 млрд. руб.', '8,25%'],
             ['БO-02', 'ПАО «Магнит»', '13.09.2010', '09.09.2013', '1 млрд. руб.', '8,25%'],
             ['БO-01', 'ПАО «Магнит»', '13.09.2010', '09.09.2013', '1 млрд. руб.', '8,25%'],
             ['02', 'ООО «Магнит Финанс»', '30.03.2007', '23.03.2012', '5 млрд. руб.', '8,20%'],
             ['01', 'ООО «Магнит Финанс»', '23.11.2005', '19.11.2008', '2 млрд. руб.', '9,34%']]
df_columns = ['Серия', 'Эмитент', 'Дата размещения', 'Дата погашения',
              'Объем выпуска', 'Ставка купона']
df = pd.DataFrame(df_values, columns=df_columns)

print(
    df
    .duplicated(subset=['Ставка купона'])
    .__invert__()
    .sum()
)
# -----------------------------------------------------
df_values = [['БО-002Р-03', 'ПАО «Магнит»', '22.05.2020', '19.05.2023', '15 млрд. руб.', '5,90%'],
             ['БО-002Р-02', 'ПАО «Магнит»', '29.04.2020', '26.04.2023', '10 млрд. руб.', '6,70%'],
             ['БО-002Р-01', 'ПАО «Магнит»', '05.03.2020', '02.03.2023', '15 млрд. руб.', '6,20%'],
             ['БО-003Р-05', 'ПАО «Магнит»', '26.12.2019', '22.12.2022', '10 млрд. руб.', '6,60%'],
             ['БО-003Р-04', 'ПАО «Магнит»', '05.11.2019', '03.05.2022', '10 млрд. руб.', '6,90%'],
             ['БО-003Р-01', 'ПАО «Магнит»', '05.02.2019', '01.02.2022', '10 млрд. руб.', '8,70%'],
             ['БО-003Р-02', 'ПАО «Магнит»', '26.02.2019', '23.02.2021', '10 млрд. руб.', '8,50%'],
             ['БО-003Р-03', 'ПАО «Магнит»', '27.06.2019', '24.12.2020', '10 млрд. руб.', '7,85%'],
             ['БО-001Р-04', 'ПАО «Магнит»', '05.07.2016', '28.12.2017', '10 млрд. руб.', '10,00%'],
             ['БО-001Р-03', 'ПАО «Магнит»', '12.04.2016', '10.04.2018', '10 млрд. руб.', '10,60%'],
             ['БО-001Р-02', 'ПАО «Магнит»', '29.02.2016', '26.02.2018', '10 млрд. руб.', '11,20%'],
             ['БО-001Р-01', 'ПАО «Магнит»', '11.11.2015', '10.05.2017', '10 млрд. руб.', '11,20%'],
             ['БO-11', 'ПАО «Магнит»', '20.10.2015', '18.04.2017', '10 млрд. руб.', '11,70%'],
             ['БO-10', 'ПАО «Магнит»', '23.07.2015', '21.07.2016', '10 млрд. руб.', '11,60%'],
             ['03', 'ПАО «Магнит»', '15.05.2015', '13.05.2016', '5 млрд. руб.', '12,10%'],
             ['02', 'ПАО «Магнит»', '15.05.2015', '13.05.2016', '5 млрд. руб.', '12,10%'],
             ['БO-09', 'ПАО «Магнит»', '02.04.2013', '29.03.2016', '5 млрд. руб.', '8,40%'],
             ['БO-08', 'ПАО «Магнит»', '02.04.2013', '29.03.2016', '5 млрд. руб.', '8,40%'],
             ['01', 'ПАО «Магнит»', '26.02.2013', '23.02.2016', '5 млрд. руб.', '8,50%'],
             ['БO-07', 'ПАО «Магнит»', '24.09.2012', '21.09.2015', '5 млрд. руб.', '8,90%'],
             ['БO-06', 'ПАО «Магнит»', '26.04.2011', '22.04.2014', '5 млрд. руб.', '7,75%'],
             ['БO-05', 'ПАО «Магнит»', '04.03.2011', '28.02.2014', '5 млрд. руб.', '8,00%'],
             ['БO-04', 'ПАО «Магнит»', '13.09.2010', '09.09.2013', '2 млрд. руб.', '8,25%'],
             ['БO-03', 'ПАО «Магнит»', '13.09.2010', '09.09.2013', '1,5 млрд. руб.', '8,25%'],
             ['БO-02', 'ПАО «Магнит»', '13.09.2010', '09.09.2013', '1 млрд. руб.', '8,25%'],
             ['БO-01', 'ПАО «Магнит»', '13.09.2010', '09.09.2013', '1 млрд. руб.', '8,25%'],
             ['02', 'ООО «Магнит Финанс»', '30.03.2007', '23.03.2012', '5 млрд. руб.', '8,20%'],
             ['01', 'ООО «Магнит Финанс»', '23.11.2005', '19.11.2008', '2 млрд. руб.', '9,34%']]
df_columns = ['Серия', 'Эмитент', 'Дата размещения', 'Дата погашения',
              'Объем выпуска', 'Ставка купона']
df = pd.DataFrame(df_values, columns=df_columns)

print(
    df
    .nunique()
    .sum()
)

# -------------------------------------------------------------------
df_values = [['БО-002Р-03', 'ПАО «Магнит»', '22.05.2020', '19.05.2023', '15 млрд. руб.', '5,90%'],
             ['БО-002Р-02', 'ПАО «Магнит»', '29.04.2020', '26.04.2023', '10 млрд. руб.', '6,70%'],
             ['БО-002Р-01', 'ПАО «Магнит»', '05.03.2020', '02.03.2023', '15 млрд. руб.', '6,20%'],
             ['БО-003Р-05', 'ПАО «Магнит»', '26.12.2019', '22.12.2022', '10 млрд. руб.', '6,60%'],
             ['БО-003Р-04', 'ПАО «Магнит»', '05.11.2019', '03.05.2022', '10 млрд. руб.', '6,90%'],
             ['БО-003Р-01', 'ПАО «Магнит»', '05.02.2019', '01.02.2022', '10 млрд. руб.', '8,70%'],
             ['БО-003Р-02', 'ПАО «Магнит»', '26.02.2019', '23.02.2021', '10 млрд. руб.', '8,50%'],
             ['БО-003Р-03', 'ПАО «Магнит»', '27.06.2019', '24.12.2020', '10 млрд. руб.', '7,85%'],
             ['БО-001Р-04', 'ПАО «Магнит»', '05.07.2016', '28.12.2017', '10 млрд. руб.', '10,00%'],
             ['БО-001Р-03', 'ПАО «Магнит»', '12.04.2016', '10.04.2018', '10 млрд. руб.', '10,60%'],
             ['БО-001Р-02', 'ПАО «Магнит»', '29.02.2016', '26.02.2018', '10 млрд. руб.', '11,20%'],
             ['БО-001Р-01', 'ПАО «Магнит»', '11.11.2015', '10.05.2017', '10 млрд. руб.', '11,20%'],
             ['БO-11', 'ПАО «Магнит»', '20.10.2015', '18.04.2017', '10 млрд. руб.', '11,70%'],
             ['БO-10', 'ПАО «Магнит»', '23.07.2015', '21.07.2016', '10 млрд. руб.', '11,60%'],
             ['03', 'ПАО «Магнит»', '15.05.2015', '13.05.2016', '5 млрд. руб.', '12,10%'],
             ['02', 'ПАО «Магнит»', '15.05.2015', '13.05.2016', '5 млрд. руб.', '12,10%'],
             ['БO-09', 'ПАО «Магнит»', '02.04.2013', '29.03.2016', '5 млрд. руб.', '8,40%'],
             ['БO-08', 'ПАО «Магнит»', '02.04.2013', '29.03.2016', '5 млрд. руб.', '8,40%'],
             ['01', 'ПАО «Магнит»', '26.02.2013', '23.02.2016', '5 млрд. руб.', '8,50%'],
             ['БO-07', 'ПАО «Магнит»', '24.09.2012', '21.09.2015', '5 млрд. руб.', '8,90%'],
             ['БO-06', 'ПАО «Магнит»', '26.04.2011', '22.04.2014', '5 млрд. руб.', '7,75%'],
             ['БO-05', 'ПАО «Магнит»', '04.03.2011', '28.02.2014', '5 млрд. руб.', '8,00%'],
             ['БO-04', 'ПАО «Магнит»', '13.09.2010', '09.09.2013', '2 млрд. руб.', '8,25%'],
             ['БO-03', 'ПАО «Магнит»', '13.09.2010', '09.09.2013', '1,5 млрд. руб.', '8,25%'],
             ['БO-02', 'ПАО «Магнит»', '13.09.2010', '09.09.2013', '1 млрд. руб.', '8,25%'],
             ['БO-01', 'ПАО «Магнит»', '13.09.2010', '09.09.2013', '1 млрд. руб.', '8,25%'],
             ['02', 'ООО «Магнит Финанс»', '30.03.2007', '23.03.2012', '5 млрд. руб.', '8,20%'],
             ['01', 'ООО «Магнит Финанс»', '23.11.2005', '19.11.2008', '2 млрд. руб.', '9,34%']]
df_columns = ['Серия', 'Эмитент', 'Дата размещения', 'Дата погашения',
              'Объем выпуска', 'Ставка купона']
df = pd.DataFrame(df_values, columns=df_columns)

print(
    df
    .value_counts(subset='Объем выпуска', ascending=True)
)

# ------------------------------------------------------
# df['Ставка купона'] = df['Ставка купона'].apply(lambda x: x.rstrip('%').replace(',', '.')).astype('float64')

print(
    df
    .assign(Ставка = lambda x: x['Ставка купона'].apply(lambda x: x.rstrip('%').replace(',', '.')).astype('float64'))
    .drop(['Ставка купона'], axis=1)
)