import pandas as pd
from data_loader import DataLoader as dl


class BaseValidator:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def base_validator(self):
        #check to see if the dataframe is empty
        if self.df.empty:
            print("The dataframe is empty.")
        else:
            null_count = self.df.isnull().sum()
            dup_count = self.df.duplicated().sum()
            if dup_count > 0:
                print(f"Number of duplicate rows: {dup_count}")
            else:
                print("No duplicate rows found.")

        if null_count.sum() == 0:
            print("No missing values in the dataset.")
        else:
            print(f"Percentage of null values in each column:\n{(null_count / len(self.df)) * 100}")
