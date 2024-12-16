import pandas as pd 

# ---------------------------------------------------------------------
baker_values_april = [['28.04.2023', 591], ['21.04.2023', 591], ['14.04.2023', 588],
                      ['06.04.2023', 590]]
baker_values_may = [['26.05.2023', 570], ['19.05.2023', 575], ['12.05.2023', 586], 
                    ['05.05.2023', 588]]
baker_values_june = [['30.06.2023', 545], ['23.06.2023', 546], ['16.06.2023', 552],
                     ['09.06.2023', 556], ['02.06.2023', 555]]
baker_columns = ['Дата выпуска', 'Факт.']
baker_april = pd.DataFrame(baker_values_april, columns=baker_columns)
baker_may = pd.DataFrame(baker_values_may, columns=baker_columns)
baker_june = pd.DataFrame(baker_values_june, columns=baker_columns)


df_s = [baker_april, baker_may, baker_june]

def month_ru(x):
    # return ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь'][x]
    m_1 = ['Мая']
    m_2 = ['Марта', 'Августа']
    if(x in m_1):
        return x.replace('я', 'й')
    elif(x in m_2):
        return x.rstrip('а')
    else:
        return x.rstrip('я') + 'ь'

def get_month(df):
    return (df
    .assign(Date = lambda x: pd.to_datetime(x['Дата выпуска'], dayfirst=True))
    .assign(Month_str = lambda x: x['Date'].dt.month_name(locale='ru_RU.UTF-8').apply(month_ru).str.lower() + ' ' + x['Date'].dt.year.astype('str'))
    ['Month_str'][0]
    )

def get_month_names(df_s):
    months = [get_month(x) for x in df_s]
    return months

# print(
#     pd.concat(df_s, keys=get_month_names(df_s))
# )

# print(pd.concat([baker_april, baker_may, baker_june], keys=['апрель 2023', 'май 2023', 'июнь 2023'])
#     .set_axis(['Дата выпуска', 'Факт.'])
# )

# -------------------------------------------------------------
baker_values_april = [['28.04.2023', 591], ['21.04.2023', 591], ['14.04.2023', 588],
                      ['06.04.2023', 590]]
baker_values_may = [['26.05.2023', 570], ['19.05.2023', 575], ['12.05.2023', 586], 
                    ['05.05.2023', 588]]
baker_values_june = [['30.06.2023', 545], ['23.06.2023', 546], ['16.06.2023', 552],
                     ['09.06.2023', 556], ['02.06.2023', 555]]
baker_columns = ['Дата выпуска', 'Факт.']
baker_april = pd.DataFrame(baker_values_april, columns=baker_columns)
baker_may = pd.DataFrame(baker_values_may, columns=baker_columns)
baker_june = pd.DataFrame(baker_values_june, columns=baker_columns)

def get_sorted_by_date(x):
        x = (
            x
            .assign(**{'Дата выпуска': lambda x: pd.to_datetime(x['Дата выпуска'], dayfirst=True)})
            .sort_values('Дата выпуска', ignore_index=True)
        )
        return x


# print(
#     pd
#     .concat([get_sorted_by_date(x) for x in [baker_april, baker_may, baker_june]], keys=get_month_names(df_s))
# )

def set_data_index(x):
    return x.set_index('Дата выпуска')

df = (
    pd.concat([set_data_index(x) for x in [baker_june, baker_may,  baker_april]], keys=get_month_names(df_s[::-1]))
)
print(df.loc['июнь 2023', :])