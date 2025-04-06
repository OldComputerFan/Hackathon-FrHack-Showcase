import os
import time
from datetime import datetime

# Function to calculate time difference
def time_difference(last_modified_time):
    # Get the current time
    current_time = time.time()
    
    # Calculate the time passed since last modification (in seconds)
    time_passed = current_time - last_modified_time
    
    # Convert seconds into a more readable format (hours, minutes, seconds, and milliseconds)
    hours = time_passed // 3600
    minutes = (time_passed % 3600) // 60
    seconds = int(time_passed) % 60
    milliseconds = int((time_passed - int(time_passed)) * 1000)
    
    return int(hours), int(minutes), int(seconds), milliseconds

# Function to read the last modified time from the file
def get_last_modified_time(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            # Extract the last modified time from the file
            last_modified_time_line = lines[-1]  # Last line contains modification time
            if "Last Modified Time (Epoch)" in last_modified_time_line:
                last_modified_time = float(last_modified_time_line.split(":")[-1].strip())
                return last_modified_time
            else:
                print("Modification time not found in the file.")
                exit()
    except FileNotFoundError:
        print(f"File not found. Please ensure '{file_path}' exists.")
        exit()

# Function to format the current time and calculated time for better output
def display_times(last_modified_time):
    # Calculate and display the time difference since the last modification
    hours, minutes, seconds, milliseconds = time_difference(last_modified_time)
    
    print("\n=========================================")
    print("  Time since last modification:")
    print(f"    {hours} hours, {minutes} minutes, {seconds} seconds, {milliseconds} milliseconds")
    print("--------------------------------------------------------")
    
    # Get the current time from the PC
    current_pc_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]  # Truncate to milliseconds
    print(f"  Current PC time: {current_pc_time}")
    
    # Calculate the actual time based on the last modified time
    actual_time_epoch = last_modified_time + (hours * 3600 + minutes * 60 + seconds) + (milliseconds / 1000)
    actual_time = datetime.fromtimestamp(actual_time_epoch).strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]  # Truncate to milliseconds
    
    # Compare and show the difference between the current PC time and the calculated time
    print(f"  Calculated actual time from file: {actual_time}")
    
    # Calculate the time difference between the current time and the calculated time
    actual_time_obj = datetime.strptime(actual_time, "%Y-%m-%d %H:%M:%S.%f")
    current_time_obj = datetime.strptime(current_pc_time, "%Y-%m-%d %H:%M:%S.%f")
    
    # Calculate the difference
    time_diff = current_time_obj - actual_time_obj
    
    # Display the time difference
    print(f"  Difference between current time and calculated time: {time_diff}")
    print("\n=========================================\n")

# Main function to tie everything together
def main(file_path="Observatoire_de_Paris.txt"):
    # Get the last modified time from the file
    last_modified_time = get_last_modified_time(file_path)
    
    # Display the initial times and differences
    display_times(last_modified_time)
    
    # Infinite loop for continuous update every second
    while True:
        # Get the time difference from the last modification
        hours, minutes, seconds, milliseconds = time_difference(last_modified_time)

        # Calculate the actual current time by adding the time difference to the last modified time
        actual_time_epoch = last_modified_time + (hours * 3600 + minutes * 60 + seconds) + (milliseconds / 1000)

        # Convert to a more readable format
        actual_time = datetime.fromtimestamp(actual_time_epoch).strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]  # Truncate to milliseconds

        # Display the updated time
        print(f"  Calculated actual time: {actual_time}")
        print("\n--------------------------------------------------------")

        # Wait for 1 second before recalculating
        time.sleep(1)

# Call the main function if this is the script being executed directly
if __name__ == "__main__":
    main()
