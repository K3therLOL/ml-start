import string
import pandas as pd


def length_stats(text: str) -> pd.Series:
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = text.translate(str.maketrans("", "", string.digits))
    text = text.lower()

    words = sorted(set(text.split()))
    return pd.Series(map(len, words), index=words)

print(length_stats('Мама мыла раму'))
print(length_stats('Лес, опушка, странный домик. Лес, опушка и зверушка.'))
