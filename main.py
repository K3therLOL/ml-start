import pandas as pd

def main():
    df = pd.read_excel("./credit_data.xlsx")
    print(df.head())
    #print(df.tail())
    #print(df.info())

if __name__ == "__main__":
    main()
