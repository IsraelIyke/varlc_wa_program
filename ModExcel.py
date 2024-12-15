import os
import glob
import pandas as pd
from PyPDF2 import PdfReader

# Function to extract text data from a PDF and convert it into arrays
def extract_pdf_to_array(pdf_path):
    reader = PdfReader(pdf_path)
    all_data = []  # To hold data arrays

    # Iterate through each page in the PDF
    for page in reader.pages:
        text = page.extract_text()

        # Split the text into words and add it to the array
        words = text.split()
        all_data.extend(words)

    return all_data

# Function to join data between specific words
def join_data_between_words(data_arrays, start_word, end_word):
    try:
        start_index = data_arrays.index(start_word) + 1
        end_index = data_arrays.index(end_word)
        data = data_arrays[start_index:end_index]
        result = ' '.join(data)
        return result
    except ValueError:
        return f"One or both of the words '{start_word}' and '{end_word}' not found in the list."

# Path to the main directory
main_dir = "./saved"

# Iterate over each subdirectory in the main directory
for subdir in os.listdir(main_dir):
    subdir_path = os.path.join(main_dir, subdir)
    
    if os.path.isdir(subdir_path):
        print(f"Processing directory: {subdir}")

        # Initialize a list to store the data for all PDFs in the current subdirectory
        all_data_for_subdir = []

        # Find all PDF files in the subdirectory
        pdf_files = glob.glob(os.path.join(subdir_path, "*.pdf"))
        
        for pdf_file in pdf_files:
            print(f"Processing file: {pdf_file}")

            # Extract data from the current PDF
            data_arrays = extract_pdf_to_array(pdf_file)
            
            # Extract relevant information
            Fullname = join_data_between_words(data_arrays, 'Fullname', 'Gender')
            Gender = join_data_between_words(data_arrays, 'Gender', 'Date')
            DOB = join_data_between_words(data_arrays, 'birth', 'State')
            Email = join_data_between_words(data_arrays, 'address', 'Mobile')
            Mobile = join_data_between_words(data_arrays, 'phone', 'Country')
            Faculty = join_data_between_words(data_arrays, 'Faculty', 'Department')
            Department = join_data_between_words(data_arrays, 'Department', 'Score')
            DepartmentTrimmed = Department[:-5]

            # Add the extracted data to the list
            all_data_for_subdir.append({
                'Fullname': Fullname,
                'Gender': Gender,
                'DOB': DOB,
                'Email': Email,
                'Mobile': Mobile,
                'Faculty': Faculty,
                'Department': DepartmentTrimmed
            })
        
        # Save the data for the current subdirectory into an Excel file
        if all_data_for_subdir:
            df = pd.DataFrame(all_data_for_subdir)
            excel_filename = f"{subdir}_data.xlsx"
            df.to_excel(excel_filename, index=False)
            print(f"Saved data for {subdir} to {excel_filename}")

print("Processing completed for all subdirectories.")
