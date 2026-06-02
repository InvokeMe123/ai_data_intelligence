

def data_cleaner(df):
   
    # Checking for missing values
    if (df.isnull().sum().sum() == 0):
        print("No missing values in the dataset.")
    else:
        print("There are missing values in the dataset.")

    # Checking for duplicates
    duplicate_count = df.duplicated().sum()
    print(f"Number of duplicate rows: {duplicate_count}")
    if duplicate_count > 0:
        df = df.drop_duplicates()
        print(f"Duplicates removed. New number of rows: {len(df)}")

    # Removing the null values
    df = df.dropna()
    print(f"Null values removed. New number of rows: {len(df)}")

    df.info()
    df.describe(include="all")