import pandas as pd
items = {'Bea' : pd.Series([250, 35, 60], index=['bike', 'pants', 'watch' ]),
         'Anders' : pd.Series([350, 75, 20, 10], index=['bike', 'pants', 'watch', 'icecream'])}

type(items)