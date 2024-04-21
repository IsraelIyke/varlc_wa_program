
from pdfminer.high_level import extract_pages, extract_text
import re
import sys
import json

text_body = extract_text("admission_list.pdf")
#print(text_body)

# JAMB regnumber regex
jamb_number_pattern = re.compile(r'\b\d{12}[A-Z]{2}\b')

jamb_numbers = jamb_number_pattern.findall(text_body)
print(jamb_numbers)



newdata = {'sum':jamb_numbers} 
print(json.dumps(newdata))