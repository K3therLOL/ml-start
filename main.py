import pandas as pd

def main():
    df = pd.read_excel("./credit_data.xlsx")
    print(f"Dimensions:\n\n{df.ndim}")
    print("-------------------------")
    print(f"First 5 lines:\n\n{df.head()}")
    print("-------------------------")
    print(f"Last 5 lines:\n\n{df.tail()}")
    print("-------------------------")
    summary = pd.DataFrame({
        "non-null": df.notna().sum(),
        "dtype": df.dtypes,
    })
    print(f"Info including data types and non-null values:\n\n{summary}")


if __name__ == "__main__":
    main()
