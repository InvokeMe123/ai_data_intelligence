from data_loader import DataLoader
from cleaner.data_cleaner import DataCleaner
from validators.base_validator import BaseValidator
from database import DatabaseManager
from standardizer.base_standardizer import BaseStandardizer

messy_file_path="/Users/bibashnepali/Desktop/AI_Data_Intelligence/ai_data_intelligence/data/Netflix Dataset.csv"
#loading data in a dataframe
messy_Data = DataLoader(messy_file_path).load_data()

#checking for duplicates and null values
validator = BaseValidator(messy_Data)
print(validator.base_validator())

#asking user if they want to remove duplicates
user_duplicate_input = input("Do you want to remove duplicates from the data? (yes/no): ").strip().lower()
#initializateing the variable to hold the data after duplicates are removed, if user chooses to remove duplicates
current_data = messy_Data
if user_duplicate_input == 'yes':
    cleaner = DataCleaner(messy_Data)
    current_data = cleaner.remove_duplicates()
    print("Duplicates have been removed.")
else:
    print("Duplicates cleaning skipped.")

#asking user if they want to remove null values
user_null_value_input = input("Do you want to remove null values in the data? (yes/no): ").strip().lower()
if user_null_value_input == 'yes':
    cleaner = DataCleaner(current_data)
    current_data = cleaner.remove_null_values()
else:
    print("Null values removal skipped.")

#standardizing the data
standardizer = BaseStandardizer(current_data)
standardized_data = standardizer.standardize()

#saving cleaned data to the database
db_manager = DatabaseManager()
db_manager.save_to_database(standardized_data)

#querying the database to check if the data has been saved correctly
query_res = db_manager.query_database("SELECT * FROM cleaned_netflix_data LIMIT 5")
print(query_res)

