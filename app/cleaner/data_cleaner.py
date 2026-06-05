import pandas as pd

class DataCleaner:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def remove_duplicates(self):
        # Checking for duplicates
        duplicate_count = self.df.duplicated().sum()
        if duplicate_count > 0:
            self.df = self.df.drop_duplicates()
            print(f"Duplicates removed. New number of rows: {len(self.df)}")
        return self.df
    def remove_null_values(self):
        # Checking for null values
        null_count = self.df.isnull().sum()
        if null_count.sum() > 0:
            self.df = self.df.dropna()
            print(f"Null values removed. New number of rows: {len(self.df)}")
        return self.df
    # def replace_null_values(self, value):
    #     # Replacing null values with a specified value
    #     null_count = self.df.isnull().sum()
    #     if null_count.sum() > 0:
    #         self.df = self.df.fillna(value)
    #         print(f"Null values replaced with '{value}'.")
    #     return self.df

        

    