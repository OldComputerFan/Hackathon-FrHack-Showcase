import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time

def retrieve_paris_legal_time(driver_path="msedgedriver.exe", output_file="Observatoire_de_Paris.txt"):
    # Set up Edge options
    edge_options = Options()
    edge_options.add_argument("--headless")  # Run Edge in headless mode (no UI)

    # Set up the service for Edge WebDriver
    service = Service(driver_path)

    # Start Edge with the specified options
    driver = webdriver.Edge(service=service, options=edge_options)

    # URL of the Observatoire de Paris French legal time page
    url = "https://www.timeanddate.com/worldclock/france/paris"

    # Open the webpage
    driver.get(url)

    # Wait until the time elements are present (adjust the time if necessary)
    wait = WebDriverWait(driver, 10)
    try:
        # Extract the time in the format "11:30:19"
        time_str = wait.until(EC.presence_of_element_located((By.ID, 'ct'))).text
        # Extract synchronization status and UTC offset
        sync_status = wait.until(EC.presence_of_element_located((By.ID, 'cta'))).text.strip()
    except Exception as e:
        print(f"An error occurred while retrieving the data: {e}")
        driver.quit()
        return

    # Print the raw time string to see if it matches the expected format
    print(f"Raw Time String: {time_str}")

    # Check the format of the time string and split it by the colon (":")
    time_parts = time_str.split(':')
    print(f"Time Parts: {time_parts}")  # Print the split parts for debugging

    # Ensure that the expected number of parts is present
    if len(time_parts) == 3:
        hours, minutes, seconds = time_parts[0], time_parts[1], time_parts[2]
    else:
        print("Time format unexpected or missing components.")
        driver.quit()
        return

    # Format the legal time
    legal_time = f"{hours}:{minutes}:{seconds}"

    # Extract the current date and time for when the data was retrieved
    current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Prepare the output string
    output = f"French Legal Time: {legal_time}\n"
    output += f"Synchronization Status: {sync_status}\n"
    output += f"UTC Offset: {sync_status}\n"  # Use the extracted UTC offset
    output += f"Retrieved at: {current_timestamp}\n"

    # Save the time and other information to a text file
    with open(output_file, "w") as file:
        file.write(output)

    # Get the current modification time and save it
    last_modified_time = os.path.getmtime(output_file)

    # Save the modification time to the same file for future reference
    with open(output_file, "a") as file:
        file.write(f"\nLast Modified Time (Epoch): {last_modified_time}\n")

    print("Heure écrite dans Observatoire_de_Paris.txt")

    # Close the browser
    driver.quit()

# Example of calling the function:
if __name__ == "__main__":
    retrieve_paris_legal_time()
