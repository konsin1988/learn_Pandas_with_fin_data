import pandas as pd 

input_data = "31837000000 руб. за 2018 год\n643000000 руб. за 2019 год\n46607000000 руб. за 2020 год\n42078000000 руб. за 2021 год\n19325000000 руб. за 2022 год"

print(pd.Series(dict(map(lambda x: (int(x.split()[-2]), int(x.split()[0])), input_data.split('\n')))))
