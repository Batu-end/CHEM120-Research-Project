import pandas as pd

old_data = pd.read_excel('Old_Data.xlsx')
fall_data = pd.read_excel('Fall_Data.xlsx')


# Print the columns as sorted lists to make them easier to read
print("--- OLD DATA COLUMNS ---")
print(sorted(old_data.columns.tolist()))

print("\n--- FALL DATA COLUMNS ---")
print(sorted(fall_data.columns.tolist()))

# To see how many columns each has
print(f"\nOld Data has {len(old_data.columns)} columns.")
print(f"Fall Data has {len(fall_data.columns)} columns.")