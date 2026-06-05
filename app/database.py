from sqlalchemy import create_engine, text
import pandas as pd


class DatabaseManager:
    def __init__(self, db_url='sqlite:///cleaned_data.db'):
        self.engine = create_engine(db_url)

    def save_to_database(self, df: pd.DataFrame, table_name='cleaned_netflix_data'):
        df.to_sql(table_name, con=self.engine, if_exists='replace', index=False)
        print(f"Data has been saved to the '{table_name}' table in the database.")

    def query_database(self, query):
        with self.engine.connect() as connection:
            result = connection.execute(text(query))
            return result.fetchall()

