import os
import pandas as pd
from PyPDF2 import PdfReader

# Function to extract personal information from a PDF file
def extract_information(pdf_path):
    reader = PdfReader(pdf_path)
    extracted_data = {
        "Full Name": None,
        "Email": None,
        "Phone/Mobile": None,
        "Department": None,
        "Faculty": None,
        "Gender": None,
        "Date of Birth": None
    }

    # Iterate through pages to find the required data
    for page in reader.pages:
        text = page.extract_text()

        if "Fullname" in text:
            extracted_data["Full Name"] = text.split("Fullname")[-1].split("\n")[0].strip()

        if "Email address" in text:
            extracted_data["Email"] = text.split("Email address")[-1].split("\n")[0].strip()

        if "Mobile phone" in text:
            extracted_data["Phone/Mobile"] = text.split("Mobile phone")[-1].split("\n")[0].strip()

        if "Department" in text:
            extracted_data["Department"] = text.split("Department")[-1].split("\n")[0].strip()

        if "Faculty" in text:
            extracted_data["Faculty"] = text.split("Faculty")[-1].split("\n")[0].strip()

        if "Gender" in text:
            extracted_data["Gender"] = text.split("Gender")[-1].split("\n")[0].strip()

        if "Date of birth" in text:
            extracted_data["Date of Birth"] = text.split("Date of birth")[-1].split("\n")[0].strip()

    return extracted_data

# Function to process all PDF files in subdirectories of ./saved
def process_saved_directory(base_directory):
    output_dir = "./excel_files"
    os.makedirs(output_dir, exist_ok=True)

    for sub_dir in os.listdir(base_directory):
        sub_dir_path = os.path.join(base_directory, sub_dir)

        if os.path.isdir(sub_dir_path):
            extracted_data_list = []

            for file_name in os.listdir(sub_dir_path):
                if file_name.endswith('.pdf'):
                    pdf_path = os.path.join(sub_dir_path, file_name)
                    print(f"Processing file: {pdf_path}")
                    extracted_data = extract_information(pdf_path)
                    extracted_data_list.append(extracted_data)

            # Save all extracted data for this subdirectory to an Excel file
            if extracted_data_list:
                df = pd.DataFrame(extracted_data_list)
                output_path = os.path.join(output_dir, f"{sub_dir}.xlsx")
                df.to_excel(output_path, index=False)
                print(f"Data for directory {sub_dir} saved to {output_path}")

# Main script
base_directory = "./saved"
process_saved_directory(base_directory)
