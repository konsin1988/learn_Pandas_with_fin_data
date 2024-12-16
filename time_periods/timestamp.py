import pandas as pd 
import numpy as np 

# print(
#     pd.date_range(start='2024-01-25', end='2024-10-30', freq='Q')
# )

# print(
#     pd.bdate_range(start='2024-02-13', end='2024-08-27', freq='C', weekmask='0000100')
# )

# alibaba_values = [[ 99.87, 101.16,  99.3 , 100.1 ], [ 97.72,  97.74,  94.56,  95.07],
#                   [ 96.71,  98.49,  96.58,  97.58], [ 97.74,  98.49,  96.69,  96.9 ],
#                   [ 97.78,  97.8 ,  95.03,  96.56], [ 93.51,  94.48,  92.92,  94.22],
#                   [ 96.03,  96.3 ,  94.08,  94.85], [ 98.31, 101.84,  97.12,  99.21],
#                   [ 97.34,  97.65,  94.34,  95.72], [ 94.24,  94.45,  92.53,  93.46],
#                   [ 93.  ,  93.01,  90.75,  91.59], [ 89.63,  90.5 ,  88.29,  89.12],
#                   [ 91.94,  91.95,  90.26,  90.65], [ 87.78,  88.36,  86.86,  88.03],
#                   [ 87.6 ,  88.82,  87.22,  88.57], [ 89.28,  89.49,  87.86,  88.08],
#                   [ 88.37,  90.59,  88.31,  89.84], [ 90.49,  90.92,  89.04,  89.11],
#                   [ 89.25,  90.04,  88.27,  89.82], [ 91.5 ,  92.77,  91.29,  92.24],
#                   [ 93.45,  94.1 ,  92.34,  94.03], [ 92.55,  94.25,  92.47,  93.65],
#                   [ 92.98,  93.36,  92.16,  92.9 ]]
# alibaba_columns = ['Open','High','Low','Close']
# alibaba = pd.DataFrame(alibaba_values, columns=alibaba_columns, 
#                        index=pd.date_range(start='2023-08-01', end='2023-08-31', freq='B'))
# print(alibaba)

dti = pd.to_datetime(['2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06',
               '2023-01-09', '2023-01-10', '2023-01-11', '2023-01-12',
               '2023-01-13', '2023-01-17', '2023-01-18', '2023-01-19',
               '2023-01-20', '2023-01-23', '2023-01-24', '2023-01-25',
               '2023-01-26', '2023-01-27', '2023-01-30', '2023-01-31',
               '2023-02-01', '2023-02-02', '2023-02-03', '2023-02-06',
               '2023-02-07', '2023-02-08', '2023-02-09', '2023-02-10',
               '2023-02-13', '2023-02-14', '2023-02-15', '2023-02-16',
               '2023-02-17', '2023-02-21', '2023-02-22', '2023-02-23',
               '2023-02-24', '2023-02-27', '2023-02-28', '2023-03-01',
               '2023-03-02', '2023-03-03', '2023-03-06', '2023-03-07',
               '2023-03-08', '2023-03-09', '2023-03-10', '2023-03-13',
               '2023-03-14', '2023-03-15', '2023-03-16', '2023-03-17',
               '2023-03-20', '2023-03-21', '2023-03-22', '2023-03-23',
               '2023-03-24', '2023-03-27', '2023-03-28', '2023-03-29',
               '2023-03-30', '2023-03-31'])

print(dti.day_name(locale='ru_RU.UTF-8') == 'Среда')

ser = pd.Series(dti.values)
months_series = ser.dt.month_name(locale='ru_RU.UTF-8')


# month_lya = ['Января', 'Февраля', 'Апреля','Июня', 'Июля', 'Сентября', 'Октября', 'Ноября', 'Декабря']
month_a = ['Марта', 'Августа']
month_may = 'Мая'
def months_names_changer(month):
    if(month in month_a):
        return month.rstrip('а')
    elif(month == month_may):
        return month.rstrip('я') + 'й'
    else:
        return month.rstrip('я') + 'ь'

print(
    months_series.map(months_names_changer)
)
print(ser.dt.weekday)

print(pd.period_range('2023', '2024', freq='M'))

s = '03/01/23 10:00:00'
s = pd.to_datetime(s, format='%m/%d/%y %H:%M:%S')
print(s)

print('# -----------------------------------------')
print(pd.to_datetime('30 june 2023, Friday', format='%d %B %Y, %A'))

print(pd.bdate_range('1990-01-01', '1990-12-31', freq='C', weekmask='1000000'))

print(pd.bdate_range('2023-03-01', '2023-03-31', freq='C', holidays=['2023-03-08']))


# -----------------------------------------------------------------
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
    .assign(**{'Срок обращения': lambda x: pd.to_datetime(x['Дата погашения'], dayfirst=True) - pd.to_datetime(x['Дата размещения'], dayfirst=True)})
    [['Серия', 'Объем выпуска', 'Ставка купона', 'Срок обращения']]
)

# ---------------------------------------------------------
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
    .assign(**{'Срок обращения, дни': lambda x: pd.to_datetime(x['Дата погашения'], dayfirst=True) - pd.to_datetime(x['Дата размещения'], dayfirst=True)})
    .assign(**{'Срок обращения, дни': lambda x: x['Срок обращения, дни'].astype('string').apply(lambda x: x.rstrip('days')).astype('int64')})
    [['Серия', 'Эмитент','Срок обращения, дни']]
)

# -------------------------------------------------------
usd_jpy = [145.47, 146.06, 146.54, 147.47, 147.71, 147.33, 147.11, 146.68,
           147.16, 147.35, 147.48, 147.87, 147.6 , 147.74, 148.32, 147.64,
           148.43, 148.81, 149.04, 149.5 , 149.34]

indexes = pd.bdate_range('2023-09-01', '2023-09-30', freq='B')
print(pd.Series(data=usd_jpy, index=indexes))

# ----------------------------------------------------------
alibaba = [[84.87, 84.07], [83.98, 84.3 ], [83.12, 83.84], [86.76, 90.55],
           [90.05, 90.56], [91.02, 91.79], [94.11, 94.00], [95.03, 96.61],
           [95.22, 94.56], [92.25, 93.41], [91.54, 91.20], [93.57, 92.09],
           [91.69, 91.90], [92.89, 92.17], [92.07, 96.35], [98.17, 94.98],
           [94.95, 97.14], [97.75, 95.44], [98.07,100.55], [99.79,102.16]]

indexes_alibaba = pd.bdate_range('2023-07-01', '2023-07-31', freq='C', holidays=['2023-07-04'])
print(
    pd.DataFrame(alibaba, index=indexes_alibaba, columns=['Open', 'Close'])
)

print(
    pd.DataFrame(indexes_alibaba.strftime('%d.%m.%Y'), columns=['Date'])
    .join(pd.DataFrame(alibaba, columns=['Open', 'Close']))
)

# --------------------------------------------------------------
alibaba_values = [['03.07.2023', 84.87, 84.07], ['05.07.2023', 83.98, 84.30],
                  ['06.07.2023', 83.12, 83.84], ['07.07.2023', 86.76, 90.55],
                  ['10.07.2023', 90.05, 90.56], ['11.07.2023', 91.02, 91.79],
                  ['12.07.2023', 94.11, 94.00], ['13.07.2023', 95.03, 96.61],
                  ['14.07.2023', 95.22, 94.56], ['17.07.2023', 92.25, 93.41],
                  ['18.07.2023', 91.54, 91.20], ['19.07.2023', 93.57, 92.09],
                  ['20.07.2023', 91.69, 91.90], ['21.07.2023', 92.89, 92.17],
                  ['24.07.2023', 92.07, 96.35], ['25.07.2023', 98.17, 94.98],
                  ['26.07.2023', 94.95, 97.14], ['27.07.2023', 97.75, 95.44],
                  ['28.07.2023', 98.07,100.55], ['31.07.2023', 99.79,102.16]]
alibaba_columns = ['Date', 'Open', 'Close']
alibaba = pd.DataFrame(alibaba_values, columns=alibaba_columns)

alibaba = (
    alibaba
    .assign(Date = lambda x: pd.to_datetime(x['Date'], dayfirst=True))
    .assign(Day_of_week = lambda x: x['Date'].dt.day_name())
    .set_index('Date')
)
print(alibaba)
print()
print(
    alibaba
    .query('Day_of_week == "Friday"')
)

# ----------------------------------------------------------
usd_jpy_values = [['2023-07-03', 144.4], ['2023-07-04', 144.58], ['2023-07-05', 144.41],
                  ['2023-07-06', 144.49], ['2023-07-07', 143.95], ['2023-07-10', 142.21],
                  ['2023-07-11', 141.3], ['2023-07-12', 140.12], ['2023-07-13', 138.32],
                  ['2023-07-14', 138.07], ['2023-07-17', 138.68], ['2023-07-18', 138.73],
                  ['2023-07-19', 139.03], ['2023-07-20', 139.6], ['2023-07-21', 139.86],
                  ['2023-07-24', 141.75], ['2023-07-25', 141.52], ['2023-07-26', 140.91],
                  ['2023-07-27', 140.37], ['2023-07-28', 138.86], ['2023-07-31', 140.76],
                  ['2023-08-01', 142.32], ['2023-08-02', 142.97], ['2023-08-03', 143.34],
                  ['2023-08-04', 142.6], ['2023-08-07', 141.88], ['2023-08-08', 142.52],
                  ['2023-08-09', 143.28], ['2023-08-10', 143.73], ['2023-08-11', 144.85],
                  ['2023-08-14', 144.82], ['2023-08-15', 145.44], ['2023-08-16', 145.61],
                  ['2023-08-17', 146.33], ['2023-08-18', 145.71], ['2023-08-21', 145.3],
                  ['2023-08-22', 146.24], ['2023-08-23', 145.76], ['2023-08-24', 144.67],
                  ['2023-08-25', 146.07], ['2023-08-28', 146.53], ['2023-08-29', 146.46],
                  ['2023-08-30', 145.99], ['2023-08-31', 146.1], ['2023-09-01', 145.47],
                  ['2023-09-04', 146.06], ['2023-09-05', 146.54], ['2023-09-06', 147.47],
                  ['2023-09-07', 147.71], ['2023-09-08', 147.33], ['2023-09-11', 147.11],
                  ['2023-09-12', 146.68], ['2023-09-13', 147.16], ['2023-09-14', 147.35],
                  ['2023-09-15', 147.48], ['2023-09-18', 147.87], ['2023-09-19', 147.6],
                  ['2023-09-20', 147.74], ['2023-09-21', 148.32], ['2023-09-22', 147.64],
                  ['2023-09-25', 148.43], ['2023-09-26', 148.81], ['2023-09-27', 149.04],
                  ['2023-09-28', 149.5], ['2023-09-29', 149.34]]
usd_jpy_columns = ['Date', 'Open']
usd_jpy = pd.DataFrame(usd_jpy_values, columns=usd_jpy_columns)

print(
    usd_jpy
    .assign(Date = lambda x: pd.to_datetime(x['Date']))
    .set_index('Date')
    .query('Date.dt.day <= 10')
)

# ----------------------------------------------------------
period = pd.Period(freq='Q', year=2023)
print(period)
print(type(period))

period = pd.Period(freq='M', year=2022, month=6)
print(period)
print(type(period))

p_index = pd.PeriodIndex(['2019-07', '2019-08', '2019-09'], freq='M')
print(p_index)

p_index = pd.PeriodIndex(pd.bdate_range(start = '2023-04-01', end = '2023-04-10', freq='D'))
print(p_index)
print(type(p_index))

# ------------------------------------------------------------------------
gdp_china = ['4,8%', '0,4%', '3,9%', '2,9%', '4,5%', '6,3%']

p_index = pd.period_range('1Q2022', '2Q2023', freq='Q')
print(
    pd.Series(gdp_china, index=p_index)
)

# ---------------------------------------------------------
print('#--------------------------------------------------------')
silver_values = [[23.21, 23.32, 23.18, 23.28], [23.28, 23.32, 23.26, 23.27],
                 [23.27, 23.28, 23.22, 23.25], [23.25, 23.29, 23.22, 23.29],
                 [23.28, 23.35, 23.25, 23.34], [23.34, 23.35, 23.26, 23.34],
                 [23.34, 23.56, 23.26, 23.56], [23.55, 23.81, 23.44, 23.45],
                 [23.45, 23.46, 22.84, 22.9 ], [22.9 , 22.91, 22.5 , 22.56],
                 [22.56, 22.62, 22.52, 22.54]]
silver_columns = ['OPEN', 'HIGH', 'LOW', 'CLOSE']

indexes = pd.period_range('2023-09-29 10:00', '2023-09-29 20:00', freq='H')
df = pd.DataFrame(silver_values, columns=silver_columns, index=indexes)
print(
    df
    .query('index.dt.hour >= 12 and index.dt.hour <= 16')
)

print('# -------------------------------------------------------------')
import datetime
td = datetime.timedelta(days=28)
print(td)
print(type(td))

td = datetime.timedelta(days=150, hours=12)
