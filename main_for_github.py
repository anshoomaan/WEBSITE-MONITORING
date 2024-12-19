# pip install plyer
# pip install pillow
# pip install playwright
# playwright install

# -----------------------------------------------------------------------------------------------------------------------------------

from playwright.sync_api import sync_playwright
import os
from plyer import notification
import time
# from PIL import Image

# -----------------------------------------------------------------------------------------------------------------------------------

def show_notification():
    notification.notify(
        title="SOMEONE DID THE WORK",
        message="U HAVE TO DO FAST.",
        timeout=10  # The notification will stay for 10 seconds
    )

# -----------------------------------------------------------------------------------------------------------------------------------

def capture_screenshot(url, output_file):
    # Get the current directory and save the file there
    output_path = os.path.join(os.getcwd(), output_file)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Launch headless browser
        page = browser.new_page()
        page.goto(url)  # Navigate to the URL
        page.wait_for_load_state("networkidle")  # Wait until the network is idle (all requests complete)
        page.screenshot(path=output_path, full_page=True)  # Capture the full page
        browser.close()
    compare_pic_data()

# -----------------------------------------------------------------------------------------------------------------------------------

def compare_pic_data():
    # Get the current directory and construct the file paths for the screenshot and text file
    screenshot_path = os.path.join(os.getcwd(), "screenshot.png")
    text_file_path = os.path.join(os.getcwd(), "binary_data.txt")
    
    # Read the binary data from the screenshot image
    with open(screenshot_path, "rb") as file:
        screenshot_data = file.read()
    
    # Convert the binary data of the screenshot to binary string representation
    binary_data2 = ''.join(format(byte, '08b') for byte in screenshot_data)
    
    # Read the binary data from the text file "binary_data.txt"
    try:
        with open(text_file_path, "r") as file:
            binary_data1 = file.read()
    except FileNotFoundError:
        # If the file doesn't exist, initialize binary_data1 as empty string
        binary_data1 = ""
    
    # Compare the binary data
    if binary_data1 == binary_data2:
        print("Data matches")
        # If the data matches, delete the screenshot file
        if os.path.exists(screenshot_path):
            os.remove(screenshot_path)
            print("Screenshot file deleted")
    else:
        print("Data doesn't match")
        # Clear the binary file and write the new data (binary data from the image)
        with open(text_file_path, "w") as file:
            file.write(binary_data2)  # Write the new binary data to the file
        if os.path.exists(screenshot_path):
            os.remove(screenshot_path)
            print("Screenshot file deleted")
            show_notification()

# -----------------------------------------------------------------------------------------------------------------------------------

# # Taking input from the user for url
# user_input_url = input("Enter url to be monitored : ")
# # Displaying the entered string
# print("You entered:", user_input_url)

# # Taking input from the user for time in minutes
# user_input_time = input("Enter time in minutes for which url is to be monitored : ")
# # Displaying the entered string
# print("You entered:", user_input_time)

while True:
    capture_screenshot("paste url here plss first before use ", "screenshot.png")
    print("Doing something...")
    time.sleep(10)  # Sleep for 60 seconds (1 minute)