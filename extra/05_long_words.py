import pandas as pd


def get_long(data: pd.Series, min_length: int = 5) -> pd.Series:
   return data.loc[data >= min_length] 

data = pd.Series([3, 5, 6, 6], ['мир', 'питон', 'привет', 'яндекс'])
filtered = get_long(data)
print(data)
print(filtered)
