import pyautogui
import time
import random

# Define coordinates (Update these based on your screen resolution)
group_info_coord = (1372, 279)  # Position of the "Group Info" button
add_member_coord = (1759, 1331)  # Position of "Add member" button
first_contact_coord = (1241, 544)  # Position of the first contact in the list
checkmark_coord = (1447, 1289)  # Position of the checkmark button (confirmation)
final_coord = (1428, 878)  # Position of the final confirmation

invite_coord = (1428, 878)  # Position of the final confirmation
message_coord = (1304, 817)  # Position of the message input field
send_message_coord = (1466, 928)  # Position of the send message button

# List of contacts to add (This is just the static contact for testing)
contacts = ["Israel 2", "Ezy_SPP"]

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
        time.sleep(2)

        # Type Contact Name
        pyautogui.write(contact_name, interval=0.1)
        time.sleep(2)

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

        # Invite link for when the contact restricted people not saved in
        # their contact from adding their number to any group
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

        pyautogui.write("Varlc group")  # Type new text
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
for contact in contacts:
    add_contact_to_group(contact)
    sleep_time = random.randint(10, 30)  # Random wait time between actions
    print(f"Sleeping for {sleep_time} seconds before adding the next contact...")
    time.sleep(sleep_time)

print("Finished adding all contacts!")