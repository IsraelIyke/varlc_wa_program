import pyautogui
import time
import random
import re
import os

def human_like_move(target_x, target_y, duration=0.05):
    """Moves the cursor in a more human-like way."""
    start_x, start_y = pyautogui.position()
    steps = random.randint(1, 5)
    for i in range(steps):
        intermediate_x = start_x + (target_x - start_x) * (i / steps)
        intermediate_y = start_y + (target_y - start_y) * (i / steps)
        pyautogui.moveTo(intermediate_x, intermediate_y, duration=random.uniform(0.002, 0.005))
    pyautogui.moveTo(target_x, target_y, duration=random.uniform(0.1, duration))

def human_like_type(text):
    """Types text with variable delays to simulate human typing."""
    for char in text:
        pyautogui.write(char)
        time.sleep(random.uniform(0.001, 0.005))

group_info_coord = (1372, 279)
add_member_coord = (1832, 1282)
first_contact_coord = (1241, 544)
checkmark_coord = (1447, 1289)
final_coord = (1428, 878)
invite_coord = (1428, 878)
message_coord = (1304, 817)
send_message_coord = (1466, 928)

def extract_contacts_from_vcf(vcf_files):
    all_contacts = []
    for vcf_file in vcf_files:
        try:
            if not os.path.exists(vcf_file):
                print(f"File not found: {vcf_file}")
                continue

            with open(vcf_file, "r", encoding="utf-8") as file:
                vcf_data = file.read()

            file_contacts = re.findall(r'FN:(.+)', vcf_data)
            if file_contacts:
                original_positions = list(range(len(file_contacts)))  # Track original positions
                all_contacts.extend(zip(file_contacts, original_positions))  # Store name with index
                print(f"Extracted {len(file_contacts)} contacts from {vcf_file}.")
            else:
                print(f"No contacts found in {vcf_file}.")
        except Exception as e:
            print(f"Error reading {vcf_file}: {e}")

    return all_contacts[70:]  # Skip first 10 contacts but keep index positions

vcf_files = [
    "vcf_files/ZOOLOGY.vcf",
    "vcf_files/ECONOMICS.vcf",
]

contacts = extract_contacts_from_vcf(vcf_files)

def add_contact_to_group(contact_name, original_index):
    try:
        # time.sleep(random.uniform(3, 4))
        # human_like_move(720, 372)
        # pyautogui.click()

        # time.sleep(random.uniform(3, 4))
        # human_like_move(760, 441)
        # pyautogui.click()

        time.sleep(random.uniform(3, 4))
        human_like_move(*group_info_coord)
        pyautogui.click()
        time.sleep(random.uniform(1, 2))
        human_like_move(*add_member_coord)
        pyautogui.click()
        time.sleep(random.uniform(3, 4))
        human_like_type(contact_name)
        time.sleep(random.uniform(3, 4))
        human_like_move(*first_contact_coord)
        pyautogui.click()
        time.sleep(random.uniform(1, 2))
        human_like_move(*checkmark_coord)
        pyautogui.click()
        time.sleep(random.uniform(1, 2))
        human_like_move(*final_coord)
        pyautogui.click()

        # time.sleep(random.uniform(1, 2))
        # human_like_move(*invite_coord)
        # pyautogui.click()
        # time.sleep(random.uniform(1, 2))
        # human_like_move(*message_coord)
        # pyautogui.click()
        # time.sleep(1)

        # pyautogui.hotkey('ctrl', 'a')
        # time.sleep(random.uniform(1, 2))
        # pyautogui.press('backspace')
        # time.sleep(random.uniform(1, 2))
        # human_like_type("Congratulations on your admission to UNN. Join this group to connect with your classmates and get all information you need about lectures and settling down.")
        # time.sleep(random.uniform(1, 2))
        # human_like_move(*send_message_coord)
        # pyautogui.click()

        time.sleep(random.uniform(1, 2))
        pyautogui.press('esc')
        print(f"Added contact at original position {original_index}: {contact_name} successfully!")
    except Exception as e:
        print(f"Error adding contact at original position {original_index}: {contact_name}: {e}")

if contacts:
    for contact_name, original_index in contacts:
        add_contact_to_group(contact_name, original_index)
        sleep_time = random.randint(5, 10)
        print(f"Sleeping for {sleep_time} seconds before adding the next contact...")
        time.sleep(sleep_time)
else:
    print("No contacts to add.")

print("Finished adding all contacts!")
