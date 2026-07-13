import pandas as pd


def cheque(price_list: pd.Series, **products: int) -> pd.DataFrame:
    quantities = pd.Series(products, name="number")

    df = (
        price_list.rename("price")
        .to_frame()
        .join(quantities, how="inner")
        .sort_index()
    )

    df["cost"] = df["price"] * df["number"]
    return df.rename_axis("product").reset_index()


def discount(cheque: pd.DataFrame) -> pd.DataFrame:
    discount = cheque.copy()
    discount["cost"] = discount["cost"].astype("float64")
    discount.loc[discount["number"] > 2, "cost"] /= 2
    return discount

products = ['bread', 'milk', 'soda', 'cream']
prices = [37, 58, 99, 72]
price_list = pd.Series(prices, products)
result = cheque(price_list, soda=3, milk=2, cream=1)
with_discount = discount(result)
print(result)
print(with_discount)
