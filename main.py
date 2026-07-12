import pandas as pd

def main():
    df = pd.read_excel("./credit_data.xlsx")
    print(f"Dimensions:\n\n{df.ndim}")
    print("-------------------------")
    print(f"First 5 lines:\n\n{df.head()}")
    print("-------------------------")
    print(f"First 5 lines:\n\n{df.tail()}")

if __name__ == "__main__":
    main()
