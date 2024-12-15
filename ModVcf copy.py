import os
import glob
import vobject
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
        return None  # Return None if the words are not found

# Path to the main directory
main_dir = "./saved"
vcf_dir = "./vcf_files"

# Create the vcf_files directory if it doesn't exist
if not os.path.exists(vcf_dir):
    os.makedirs(vcf_dir)

# Iterate over each subdirectory in the main directory
for subdir in os.listdir(main_dir):
    subdir_path = os.path.join(main_dir, subdir)
    
    if os.path.isdir(subdir_path):
        print(f"Processing directory: {subdir}")

        # Create the VCF file for the directory, open in write mode
        vcf_filename = os.path.join(vcf_dir, f"{subdir}.vcf")
        with open(vcf_filename, 'w') as vcf_file:

            # Iterate over all PDFs in the subdirectory
            pdf_files = glob.glob(os.path.join(subdir_path, "*.pdf"))
            
            for pdf_file in pdf_files:
                print(f"Processing file: {pdf_file}")

                # Extract data from the current PDF
                data_arrays = extract_pdf_to_array(pdf_file)
                
                # Extract relevant information
                Fullname = join_data_between_words(data_arrays, 'Fullname', 'Gender')
                Department = join_data_between_words(data_arrays, 'Department', 'Score')
                DepartmentTrimmed = Department[:-5] if Department else ""  # Trim the department as required

                # Extract phone or mobile information
                Mobile = join_data_between_words(data_arrays, 'phone', 'Country')
                if Mobile is None:
                    Mobile = join_data_between_words(data_arrays, 'Mobile', 'Country')

                # Ensure that Fullname is not empty
                if not Fullname:
                    print(f"Skipping file {pdf_file} because Fullname is empty.")
                    continue  # Skip this file if Fullname is empty

                # Create the modified Fullname with DepartmentTrimmed and "2425"
                modified_name = f"{Fullname} {DepartmentTrimmed} _2425"

                # Create a new VCard object for each contact
                vcard = vobject.vCard()

                # Add the contact information to the VCard
                vcard.add('fn').value = modified_name  # Full name with DepartmentTrimmed and "2425"
                
                # Add phone/mobile number if available
                if Mobile:
                    vcard.add('tel').value = Mobile  # Add phone/mobile number

                # Write the VCard for the current contact to the file
                vcf_file.write(vcard.serialize())

        print(f"Saved VCF for directory {subdir} to {vcf_filename}")

print("Processing completed for all subdirectories.")
