import pyautogui

# After opening web whatsapp using https://web.whatsapp.com
# clear the chat in that group before starting any other program (optional)

# place your cursor to where you want the action to take place 
# without moving the curser, navigate back to your vscode with keyboard only 
# and run this code
# this will give you th x,y coordinates to be used in the varlc_WA_bot.py

# Note: Before getting your coordinates, make sure you resize the browser 
# (I resized mine to 50%) so that the "Add Member" option will be showing 
# as in varlc_image1.png (check in the image folder)

#
print(pyautogui.position())
