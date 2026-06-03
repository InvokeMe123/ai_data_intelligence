from data_loader import DataLoader
import cleaner.data_cleaner as data_cleaner
from validators.base_validator import BaseValidator

messy_file_path="/Users/bibashnepali/Desktop/AI_Data_Intelligence/ai_data_intelligence/data/Netflix Dataset.csv"
messy_Data = DataLoader(messy_file_path).load_data()
validator = BaseValidator(messy_Data)
validator.base_validator()
user_input = input("Do you want to remove null values? (yes/no): ").strip().lower()
remove_null = user_input == "yes"
cleaned_Data = data_cleaner.DataCleaner(messy_Data)
cleaned_Data = cleaned_Data.clean_data(remove_null=remove_null)

