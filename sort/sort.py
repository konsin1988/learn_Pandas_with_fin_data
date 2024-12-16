import pandas as pd 
import numpy as np 

exchanges_values = [['Нью-Йоркская биржа New York Stock Exchange(NYSE)', 'США', '1817', 
             'Dow Jones, NYSE Composite, S&P500', 'доллар США', 'фондовый, срочный, товарный'],
             ['Чикагская биржа (CME)', 'США', '1874', np.nan, 'доллар США', 
              'товарный, валютный, рынок драгоценных металлов, срочный'],
             ['NASDAQ (National Association of Securities Dealers Automated Quotation)', 'США',
              '1971', 'NASDAQ Composite, NASDAQ-100, S&P500', 'доллар США', 'фондовый, срочный'],
             ['Лондонская биржа London Stock Exchange (LSE)', 'Великобритания', '1698', 
              'FTSE 100', 'английский фунт', 'фондовый, срочный'], 
             ['Japan Exchange Group (JPX)', 'Япония', '1878', 'NIKKEI 225', 
              'японская йена', 'фондовый, срочный'],
             ['Гонконгская биржа Hong Kong Stock Exchange (HKEX)', 'Китай', '1891', 
              'Hang Seng', 'гонконгский доллар', 'фондовый, срочный'],
             ['Deutsche Börse', 'Германия', '1585', 'DAX', 'евро', 'фондовый, срочный'],
             ['Euronext', 'Европейский союз', '2000', 'Euronext 100, CAC 40', 'евро', 
              'фондовый, срочный'],
             ['Шанхайская биржа Shanghai Stock Exchange (SSE)', 'Китай', '1860', 
              'SSE Composite', 'китайский юань', 'фондовый, срочный'],
             ['Шэньчжэньская фондовая биржа Shenzhen Stock Exchange (SZSE)', 'Китай', '1990', 
              'SZSE Component', 'китайский юань', 'фондовый, срочный'],
             ['Национальная фондовая биржа Индии National Stock Exchange of India (NSE)', 
              'Индия', '1992', 'NIFTY 50', 'индийская рупия', 'фондовый, срочный'],
             ['Бомбейская фондовая биржа Bombay Stock Exchange (BSE)', 'Индия', '1875', 
              'BSE SENSEX', 'индийская рупия', 'фондовый, срочный']]
exchanges_columns = ['Наименование биржи', 'Страна', 'Год основания', 'Индексы', 'Валюта', 'Рынки']
exchanges = pd.DataFrame(exchanges_values, columns=exchanges_columns)

print(exchanges.sort_values(['Страна', 'Год основания'])[['Наименование биржи', 'Год основания']])

# ---------------------------------------------------
rates_values = [['Япония', -0.1, 3.3], ['Швейцария', 1.75, 1.6],
                ['Южная Корея', 3.5, 2.3], ['Сингапур', 3.51, 4.5],
                ['Китай', 3.55, 0.0], ['Австралия', 4.1, 6.0],
                ['еврозона', 4.25, 5.3], ['Канада', 5.0, 2.8],
                ['Великобритания', 5.25, 7.9], ['Соединенные Штаты', 5.5, 3.3],
                ['Индонезия', 5.75, 3.08], ['Саудовская Аравия', 6.0, 2.7],
                ['Индия', 6.5, 4.81], ['ЮАР', 8.25, 5.4], ['Россия', 8.5, 3.2],
                ['Мексика', 11.25, 5.06], ['Бразилия', 13.25, 3.16], ['Турция', 17.5, 47.83]]
rates_columns = ['Страна', 'Процентная ставка ЦБ', 'Инфляция']
rates = pd.DataFrame(rates_values, columns=rates_columns)

print(
    rates
    .sort_values(['Инфляция', 'Процентная ставка ЦБ'], ascending=False, ignore_index=True)
)

# ----------------------------------------------------------
depo_values = [['New Energy Bank', 1_000_000_000, 8.30, 'O/N'],
               ['AgroFoodBank', 5_000_000_000, 8.50, '1W'],
               ['First Ecologic Bank', 4_500_000_000, 8.60, '1M'],
               ['Cryptocurrencybank', 2_700_000_000, 8.30, 'O/N'],
               ['GreenEnergyBank', 1_800_000_000, 8.35, 'O/N'],
               ['ClearWaterBank', 3_000_000_000, 8.40, 'O/N'],
               ['First Ecologic Bank', 3_000_000_000, 8.41, 'O/N'],
               ['Cryptocurrencybank', 7_500_000_000, 8.50, 'O/N'],
               ['Golden Silver Bank', 2_500_000_000, 8.65, '1M'],
               ['New Energy Bank', 2_000_000_000, 8.45, '1W'],
               ['AgroFoodBank', 700_000_000, 8.25, 'O/N'],
               ['Golden Silver Bank', 4_300_000_000, 8.40, 'O/N'],
               ['New Energy Bank', 4_000_000_000, 8.80, '3M']]
depo_columns = ['Банк', 'Сумма, руб.', 'Ставка', 'Срок']
depo = pd.DataFrame(depo_values, columns=depo_columns)

print(
    depo
    .sort_values('Сумма, руб.', ascending=False)
)

# ------------------------------------------------------------
depo_values = [['New Energy Bank', 1_000_000_000, 8.30, 'O/N'],
               ['AgroFoodBank', 5_000_000_000, 8.50, '1W'],
               ['First Ecologic Bank', 4_500_000_000, 8.60, '1M'],
               ['Cryptocurrencybank', 2_700_000_000, 8.30, 'O/N'],
               ['Big Business Bank', 1_500_000_000, 8.27, 'O/N'],
               ['GreenEnergyBank', 1_800_000_000, 8.35, 'O/N'],
               ['Allmoneybank', 5_900_000_000, 8.45, 'O/N'],
               ['ClearWaterBank', 3_000_000_000, 8.40, 'O/N'],
               ['First Ecologic Bank', 3_000_000_000, 8.41, 'O/N'],
               ['Cryptocurrencybank', 7_500_000_000, 8.50, 'O/N'],
               ['Allmoneybank', 2_400_000_000, 9.00, '3M'],
               ['Big Business Bank', 2_500_000_000, 8.30, 'O/N'],
               ['Golden Silver Bank', 2_500_000_000, 8.65, '1M'],
               ['New Energy Bank', 2_000_000_000, 8.45, '1W'],
               ['AgroFoodBank', 700_000_000, 8.25, 'O/N'],
               ['Golden Silver Bank', 4_300_000_000, 8.40, 'O/N'],
               ['SmallBusinessBank', 2_000_000_000, 8.31, 'O/N'],
               ['SmallBusinessBank', 8_000_000_000, 8.70, '1M'],
               ['New Energy Bank', 4_000_000_000, 8.80, '3M']]
depo_columns = ['Банк', 'Сумма, руб.', 'Ставка', 'Срок']
depo = pd.DataFrame(depo_values, columns=depo_columns)

print(
    depo
    .sort_values(['Банк', 'Ставка'], ascending=[True, False])
)

# ------------------------------------------------------
depo_values = [['New Energy Bank', 1_000_000_000, 8.30, 'O/N'],
               ['AgroFoodBank', 5_000_000_000, 8.50, '1W'],
               ['First Ecologic Bank', 4_500_000_000, 8.60, '1M'],
               ['Cryptocurrencybank', 2_700_000_000, 8.30, 'O/N'],
               ['GreenEnergyBank', 1_800_000_000, 8.35, 'O/N'],
               ['ClearWaterBank', 3_000_000_000, 8.40, 'O/N'],
               ['First Ecologic Bank', 3_000_000_000, 8.41, 'O/N'],
               ['Cryptocurrencybank', 7_500_000_000, 8.50, 'O/N'],
               ['Golden Silver Bank', 2_500_000_000, 8.65, '1M'],
               ['New Energy Bank', 2_000_000_000, 8.45, '1W'],
               ['AgroFoodBank', 700_000_000, 8.25, 'O/N'],
               ['Golden Silver Bank', 4_300_000_000, 8.40, 'O/N'],
               ['New Energy Bank', 4_000_000_000, 8.80, '3M']]
depo_columns = ['Банк', 'Сумма, руб.', 'Ставка', 'Срок']
depo = pd.DataFrame(depo_values, columns=depo_columns)

print(
    depo
    .sort_values(['Срок', 'Сумма, руб.'], ignore_index=True)
)