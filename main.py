import pandas as pd

SEPARATOR = 120 * "="

def print_section(title: str, content: object) -> None:
    print(f"{title}:\n{content}")
    print(SEPARATOR)
    

def main():
    df = pd.read_excel("./credit_data.xlsx")

    print_section("DIMENSIONS", df.ndim)

    print_section("FIRST 5 LINES", df.head())

    print_section("LAST 5 LINES", df.tail())

    summary = pd.DataFrame({
        "non-null": df.notna().sum(),
        "dtype": df.dtypes,
    })
    print_section("INFO INCLUDING DATA TYPES AND NON-NULL VALUES", summary)

    df = df.drop(columns=["client_id"])
    print_section("DELETING CLIENT_ID FROM TABLE", df.head())

    print_section("GROUPED BY 'recent_salary' AND GOT NUMBER OF UNIQUE VALUES", df.groupby("recent_salary").nunique())

    print_section("GETTING ROWS WITH NO DATA IN 'recent_salary'", df[df["recent_salary"].isna()])

if __name__ == "__main__":
    main()
