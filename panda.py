import pandas as pd
import re  # For sanitizing file names
import os  # For directory management

# File path and column to group by
file_path = "2024-2025-ADVERT-SHOPPING-ADMISSION-LIST-FOR-UPLOAD.xlsx"
column_to_group_by = "DEPARTMENT"

# Define the output directory
output_directory = "C:/Users/USER/Desktop/v-data/course/"

# Ensure the output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Load the Excel file
df = pd.read_excel(file_path)

# Iterate over groups and save each as a separate Excel file
for group_value, group_df in df.groupby(column_to_group_by):
    # Replace invalid characters and remove newline characters
    sanitized_value = re.sub(r'[<>:"/\\|?*\n]', '-', str(group_value))
    output_file = f"{output_directory}{sanitized_value}.xlsx"
    group_df.to_excel(output_file, index=False)
    print(f"Saved: {output_file}")
