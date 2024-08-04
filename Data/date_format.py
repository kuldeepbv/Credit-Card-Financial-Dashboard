import pandas as pd
from datetime import datetime

# Read CSV file
df = pd.read_csv('cc_add.csv')

# Function to convert different date formats to 'YYYY-MM-DD'
def convert_date(date_str):
    try:
        # Try parsing as '1/1/2023' format
        return datetime.strptime(date_str, '%d/%m/%Y').strftime('%m-%d-%Y')
    except ValueError:
        # If fails, try parsing as '15-01-2023' format
        return datetime.strptime(date_str, '%d-%m-%Y').strftime('%m-%d-%Y')

# Apply conversion to the date column
df['Week_Start_Date'] = df['Week_Start_Date'].apply(convert_date)

# Save the modified DataFrame back to the original CSV file
df.to_csv('updated_cc_add.csv', index=False)