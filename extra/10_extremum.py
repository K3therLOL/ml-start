import pandas as pd
import numpy as np
from collections.abc import Callable


def values(math_operation: Callable[[float], float], start: float, end: float, step: float) -> pd.Series:
    math_range = np.arange(start, end + step, step)
    return pd.Series(
        index=math_range,
        data=[math_operation(x) for x in math_range],
        dtype="float64"
    )


def min_extremum(data: pd.Series) -> float:
    return data.idxmin()


def max_extremum(data: pd.Series) -> float:
    return data.idxmax()


data = values(lambda x: x ** 2 + 2 * x + 1, -1.5, 1.7, 0.1)
print(data)
print(min_extremum(data))
print(max_extremum(data))
