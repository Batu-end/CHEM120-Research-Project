import pandas as pd

old_data = pd.read_excel('Old_Data.xlsx')
fall_data = pd.read_excel('Fall_Data.xlsx')

def add_term():
    # Will add a term column to distinguish the source
    old_data['Term'] = 'Pre-Fall'
    fall_data['Term'] = 'Fall_2025'

    print(old_data[['Group Number', 'Term']].head())
    print(fall_data[['ID', 'Term']].head())


def match_columns():
    mapping = {
        'What was the A-site element in compound X\nFor example, in\xa0La2CoO4 the A-site element is La': '1A'

    }

    return mapping


mapping = match_columns()

fall_data = fall_data.rename(columns=mapping)

print(fall_data['1A'].head())
print(fall_data.columns)