import pandas as pd


def cheque(price_list: pd.Series, **products: int) -> pd.DataFrame:
    df = price_list.sort_index().rename_axis("product").to_frame(name="price")
    for name, number in products.items():
        df.loc[name, "number"] = number
        df.loc[name, "cost"] = number * df.loc[name, "price"]
    
    df = df.dropna()
    df[["number", "cost"]] = df[["number", "cost"]].astype("int64")
    return df.reset_index(drop=False)


products = ['bread', 'milk', 'soda', 'cream']
prices = [37, 58, 99, 72]
price_list = pd.Series(prices, products)
result = cheque(price_list, soda=3, milk=2, cream=1)
print(result)

