import os
from calculate_time import  display_times, get_last_modified_time
from get_save_time import retrieve_paris_legal_time

def main():
    # Display a menu to the user
    while True:
        print("\n=======================================")
        print("  Choose an option:")
        print("  1. Update the legal time in the file (Observatoire_de_Paris.txt)")
        print("  2. Show the current time and time difference since the last file modification")
        print("  3. Exit")
        print("=======================================")
        
        # Get user input
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            # Option 1: Update the legal time in the file
            print("\nUpdating the legal time in the file...")
            retrieve_paris_legal_time()  # Calls the function to update the file
        elif choice == "2":
            # Option 2: Show the current time and time difference
            file_path = "Observatoire_de_Paris.txt"
            if os.path.exists(file_path):
                # Get the last modified time from the file
                last_modified_time = get_last_modified_time(file_path)
                
                # Display the time difference and other details
                display_times(last_modified_time)
            else:
                print(f"Error: The file '{file_path}' does not exist.")
        elif choice == "3":
            # Exit the program
            print("Exiting the program...")
            break
        else:
            print("Invalid choice, please select again.")

if __name__ == "__main__":
    main()
