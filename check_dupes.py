import pandas as pd

# 1. Load the datasets
# Replace with your actual file paths
old_data = pd.read_excel('Data.xlsx')
fall_data = pd.read_excel('FallData.xlsx')

# --- PRELIMINARY INSPECTION ---
print("Old Data Columns:", old_data.columns.tolist())
print("Fall Data Columns:", fall_data.columns.tolist())

# --- DUPLICATE CHECKING ---

# Check for exact duplicates across all columns
print(f"Exact duplicates in Old Data: {old_data.duplicated().sum()}")
print(f"Exact duplicates in Fall Data: {fall_data.duplicated().sum()}")

# OPTIONAL: Check for duplicates in the specific 'ID' columns
# Replace 'Group Number' and 'ID' with the actual column headers from your inspection above
# print(f"ID duplicates in Old Data: {old_data['Group Number'].duplicated().sum()}")
# print(f"ID duplicates in Fall Data: {fall_data['ID'].duplicated().sum()}")

# --- CLEANING ---

# Drop exact duplicates if found
old_data = old_data.drop_duplicates()
fall_data = fall_data.drop_duplicates()

print("Data loaded and exact duplicates removed.")