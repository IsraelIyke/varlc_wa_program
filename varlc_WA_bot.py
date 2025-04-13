import pyautogui
import time
import random
import re

# So this is where you define the coordinates based on your screen resolution
# You get these coordinates by placing your mouse cursor to the points
# you want the actions to take place and then run the coordinate.py program

group_info_coord = (1372, 270)  # Position of the "Group Info" button
add_member_coord = (1676, 1181)  # Position of "Add member" button
first_contact_coord = (1256, 480)  # Position of the first contact in the list
checkmark_coord = (1415, 1318)  # Position of the checkmark button (confirmation)
final_coord = (1405, 856)  # Position of the final confirmation

# This last 3 coordinates are for when the contact restricted people not saved in
# their contact from adding their number to any group

invite_coord = (1405, 856)  # Position of the "invite" button 
message_coord = (1294, 820)  # Position of the message input field
send_message_coord = (1430, 899)  # Position of the send message button

# Function to extract names from VCF file
def extract_contacts_from_vcf(vcf_file):
    contacts = []
    try:
        with open(vcf_file, "r", encoding="utf-8") as file:
            vcf_data = file.read()

        # Extract contact names (search for "FN:" which means Full Name)
        contacts = re.findall(r'FN:(.+)', vcf_data)

        if not contacts:
            print("No contacts found in the VCF file.")
        else:
            print(f"Extracted {len(contacts)} contacts from VCF.")
    
    except Exception as e:
        print(f"Error reading VCF file: {e}")

    return contacts

# Provide the path to your VCF file
# The vcf files in the vcf_files directory is from the supplementary list 3
vcf_path = "vcf_files/METALLURGICAL AND MATERIALS ENGINEERING.vcf"  
# Change this to your actual file path

# Get contacts from VCF file
contacts = extract_contacts_from_vcf(vcf_path)

# Function to add a member
def add_contact_to_group(contact_name):
    try:
        time.sleep(5)

        # Open Group Info
        pyautogui.moveTo(*group_info_coord)
        pyautogui.click()
        time.sleep(2)

        # Click "Add Member"
        pyautogui.moveTo(*add_member_coord)
        pyautogui.click()
        time.sleep(5)

        # Type Contact Name
        pyautogui.write(contact_name)
        time.sleep(5)

# I commented the codes below to ensure testing without actually adding the members

        # Select First Contact
        pyautogui.moveTo(*first_contact_coord)
        pyautogui.click()
        time.sleep(2)

        # Click Checkmark Button to Confirm
        pyautogui.moveTo(*checkmark_coord)
        pyautogui.click()
        time.sleep(3)

        # Final Confirmation
        pyautogui.moveTo(*final_coord)
        pyautogui.click()
        time.sleep(3)

        # Invite
        pyautogui.moveTo(*invite_coord)
        pyautogui.click()
        time.sleep(3)

        # Edit the message before final confirmation
        pyautogui.moveTo(*message_coord)
        pyautogui.click()
        time.sleep(1)

        pyautogui.hotkey('ctrl', 'a')  # Select all text
        time.sleep(1)

        pyautogui.press('backspace')  # Delete selected text
        time.sleep(1)

        pyautogui.write("Congratulations on your admission to UNN.  Join this group to connect with your classmates  and get all information you need about lectures and settling down.", interval=0.1)  # Type new text
        time.sleep(1)

        # Send Message
        pyautogui.moveTo(*send_message_coord)
        pyautogui.click()
        time.sleep(3)

        pyautogui.press('esc')

        print(f"Added {contact_name} successfully!")
    except Exception as e:
        print(f"Error adding {contact_name}: {e}")

# Add members with random intervals to mimic human actions
if contacts:
    for contact in contacts:
        add_contact_to_group(contact)
        sleep_time = random.randint(20, 50)  # Random wait time between actions
        print(f"Sleeping for {sleep_time} seconds before adding the next contact...")
        time.sleep(sleep_time)
else:
    print("No contacts to add.")

print("Finished adding all contacts!")
