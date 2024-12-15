import pandas as pd
import pyautogui
import os
import re

# Load data from Excel file and extract the specified column as a list
excel_file_path = "./2024-2025-PRIMARY-ADMISSION-LIST(1).xlsx"
column_name = "JAMB REG. NO."  # Replace with the actual column name in your Excel file
df = pd.read_excel(excel_file_path)

# Extract the column data into a list
jamb_numbers = df[column_name].dropna().astype(str).tolist()

# Get the list of files in the 'saved/' directory
files = os.listdir("./saved")
trimmed_list = [s[:-4] for s in files]  # Remove file extensions

# Convert trimmed_list to lowercase for case-insensitive comparison
trimmed_list_lower = [s.lower() for s in trimmed_list]

# Filter out already-processed numbers (case-insensitive)

filtered_list = [
    item for item in jamb_numbers
    if item.lower() not in trimmed_list_lower and item.lower() != "jamb reg. no."
]

# filtered_list = filtered_list[50:]
# print(len(filtered_list))


# Process each value in the filtered list
for value in filtered_list:
    pyautogui.sleep(5)
    # These coordinates are based on my PC resolution. Please adjust to your own system
    pyautogui.click(1216, 1026)
    pyautogui.sleep(1)
    pyautogui.write(value)
    pyautogui.click(1665, 1170)
    pyautogui.sleep(30)
    
    pyautogui.click(828, 1366)
    pyautogui.sleep(4)
    pyautogui.click(2003, 1318)
    pyautogui.sleep(2)
    pyautogui.write(value)
    pyautogui.sleep(3)
    pyautogui.click(905, 909)
    pyautogui.sleep(2)

    pyautogui.press('enter')
    pyautogui.press('esc')
    pyautogui.press('esc')

    pyautogui.sleep(2)
    pyautogui.click(1000, 186)
    pyautogui.write("https://unnportal.unn.edu.ng/putme_login")
    pyautogui.press('enter')
