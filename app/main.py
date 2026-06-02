import data_loader
import data_cleaner

messy_file_path="/Users/bibashnepali/Desktop/AI_Data_Intelligence/ai_data_intelligence/data/messy_ecommerce_sales_data.csv"
messy_Data = data_loader.data_loader(messy_file_path)
cleaned_Data = data_cleaner.data_cleaner(messy_Data)