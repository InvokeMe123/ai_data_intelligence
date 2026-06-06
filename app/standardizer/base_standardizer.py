from standardizer.rules import COLUMN_RULES


class BaseStandardizer:
    def __init__(self, df):
        self.df = df

    def standardize_column_names(self):
        self.df.columns = (
            self.df.columns
            .str.lower()
            .str.strip()
            .str.replace(" ", "_")
        )

    def apply_rules(self):
        for column in self.df.columns:

            if column in COLUMN_RULES:

                rules = COLUMN_RULES[column]

                for rule in rules:
                    self.df[column] = rule(self.df[column])

        return self.df

    def standardize(self):
        self.standardize_column_names()
        self.apply_rules()

        print("Data standardization completed.")

        return self.df