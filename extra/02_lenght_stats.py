import string
import pandas as pd


def length_stats(text: str) -> tuple[pd.Series, pd.Series]:
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = text.translate(str.maketrans("", "", string.digits))
    text = text.lower()

    words = sorted(set(text.split()))
    s = pd.Series(map(len, words), index=words)
    return s.loc[s % 2 != 0], s.loc[s % 2 == 0]

even, odd = length_stats('Мама мыла раму')
print(even)
print(odd)
even, odd = length_stats('Лес, опушка, странный домик. Лес, опушка и зверушка.')
print(even)
print(odd)
