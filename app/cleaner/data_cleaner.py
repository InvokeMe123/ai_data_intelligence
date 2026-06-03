import pandas as pd

class DataCleaner:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def clean_data(self, remove_null=False):
        # Checking for missing values
        if (self.df.isnull().sum().sum() == 0):
            print("No missing values in the dataset.")
        else:
            print("There are missing values in the dataset.")

        # Checking for duplicates
        duplicate_count = self.df.duplicated().sum()
        print(f"Number of duplicate rows: {duplicate_count}")
        if duplicate_count > 0:
            self.df = self.df.drop_duplicates()
            print(f"Duplicates removed. New number of rows: {len(self.df)}")

        # Removing the all null values
        if remove_null:
            self.df = self.df.dropna()
            print(f"Null values removed. New number of rows: {len(self.df)}")
        else:
            print("Null values not removed. Use remove_null=True to remove them.")

        return self.df

    