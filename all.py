import pandas as pd
import os

def merge_excel_files(directory_path):
    """Merges all Excel files in a specified directory into a single Excel file,
    ensuring the "Mobile" field is a phone number starting with 0.

    Args:
        directory_path (str): The path to the directory containing the Excel files.

    Returns:
        None
    """

    all_dataframes = []
    for file in os.listdir(directory_path):
        if file.endswith('.xlsx') or file.endswith('.xls'):
            file_path = os.path.join(directory_path, file)
            df = pd.read_excel(file_path)

            # Ensure "Mobile" field is a string and starts with 0
            df['Mobile'] = df['Mobile'].astype(str)
            df['Mobile'] = df['Mobile'].apply(lambda x: '0' + x if not x.startswith('0') else x)

            all_dataframes.append(df)

    merged_df = pd.concat(all_dataframes, ignore_index=True)
    merged_df.to_excel('merged_data2.xlsx', index=False)

if __name__ == '__main__':
    directory_path = './excel_files'  # Replace with your directory path
    merge_excel_files(directory_path)