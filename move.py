import os
import pandas as pd
import shutil

def move_matching_files(source_dir, excel_file_path, column_name):
    # Step 1: Get all file names in the source directory without .pdf extension
    files_in_directory = [f for f in os.listdir(source_dir) if f.endswith('.pdf')]
    file_names = [os.path.splitext(f)[0].lower() for f in files_in_directory]  # Remove .pdf extension and convert to lowercase

    # Step 2: Read the Excel file using pandas and extract the relevant column
    df = pd.read_excel(excel_file_path)
    
    # Check if the column exists in the Excel file
    if column_name not in df.columns:
        print(f"Column '{column_name}' not found in the Excel file.")
        return

    # Get the data from the specified column, convert to string, and convert to lowercase
    excel_data = df[column_name].dropna().astype(str).str.lower().tolist()

    # Step 3: Compare file names with Excel column data
    matching_files = [f for f in file_names if f in excel_data]

    # Step 4: Create a new directory with the name of the Excel file (without extension)
    excel_file_name = os.path.splitext(os.path.basename(excel_file_path))[0]
    target_dir = os.path.join(source_dir, excel_file_name)

    # If the directory doesn't exist, create it
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Step 5: Move the matching files to the new directory
    for file_name in matching_files:
        source_file = os.path.join(source_dir, f"{file_name}.pdf")
        if os.path.exists(source_file):
            shutil.move(source_file, os.path.join(target_dir, f"{file_name}.pdf"))
            print(f"Moved: {file_name}.pdf")

# Main script to iterate over all Excel files in the "course" directory
source_directory = "./saved/"  # Replace with your source directory path
course_directory = "./course/"  # Directory containing Excel files
column_name = "JAMB REG. NO."  # Replace with the name of the column you want to search in

# Get all Excel files in the "course" directory
excel_files = [f for f in os.listdir(course_directory) if f.endswith('.xlsx') or f.endswith('.xls')]

for excel_file in excel_files:
    excel_file_path = os.path.join(course_directory, excel_file)
    print(f"Processing file: {excel_file_path}")
    move_matching_files(source_directory, excel_file_path, column_name)
