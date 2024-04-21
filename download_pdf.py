import pyautogui
from pdfminer.high_level import extract_pages, extract_text
import re
import sys 

text_body = extract_text("admission_list.pdf")
#print(text_body)

# JAMB regnumber regex
jamb_number_pattern = re.compile(r'\b\d{12}[A-Z]{2}\b')

jamb_numbers = jamb_number_pattern.findall(text_body)
# Array of values to iterate over
values = jamb_numbers

# navigate to your browser with the UNN portal already opened to avoid writing excessive code to achieve that.

# Iterate over each value
for value in values:
    pyautogui.sleep(20)
# These coordinates are based on my PC resolution. Please adjust to your own system
# use this to get coordinates print(pyautogui.position())

    pyautogui.click(1216, 1026, duration=1)
    pyautogui.sleep(5)
    pyautogui.write(value)
    pyautogui.sleep(5)
    pyautogui.click(1665, 1170, duration=1)
    # You can reduce every other sleep but this line require more time because of internet speed variation
    pyautogui.sleep(30)
    pyautogui.click(828, 1366, duration=1)
    pyautogui.sleep(10)
    pyautogui.click(2003, 1318, duration=1)
    # remember to set the print option to "print to pdf" before running this script
    # Also remember to set the destination of the download if you want
    pyautogui.sleep(10)
    pyautogui.write(value)
    pyautogui.sleep(4)
    pyautogui.click(905, 909, duration=1)
    pyautogui.sleep(4)
    pyautogui.click(39, 186, duration=1)
