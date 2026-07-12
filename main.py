import pandas as pd

SEPARATOR = 120 * "="

def main():
    df = pd.read_excel("./credit_data.xlsx")

    print(f"Dimensions:\n{df.ndim}")
    print(SEPARATOR)
    print(f"First 5 lines:\n\n{df.head()}")
    print(SEPARATOR)
    print(f"Last 5 lines:\n\n{df.tail()}")
    print(SEPARATOR)
    summary = pd.DataFrame({
        "non-null": df.notna().sum(),
        "dtype": df.dtypes,
    })
    print(f"Info including data types and non-null values:\n\n{summary}")
    print(SEPARATOR)
    df = df.drop(columns=["client_id"])
    print(f"Deleting client_id from table:\n\n{df.head()}")
    print(SEPARATOR)
    print(f"Grouped by 'recent_salary' and got number of unique values:\n\n{df.groupby("recent_salary").nunique()}")
    print(SEPARATOR)
    print(f"Getting rows with no data in 'recent_salary':\n\n{df[df["recent_salary"].isna()]}")

if __name__ == "__main__":
    main()
