import csv
import keyboard
import time

with open("input.csv", mode='w', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['name', 'age', 'city'])
    print("Press 'Esc' to exit the program at any time.")
    while True:
        if keyboard.is_pressed('esc'):  # Check for Esc key press
            print("\nExiting the program.")
            break
        else:
            try:
                # Use a timeout to allow checking for the 'Esc' key in between inputs
                name = input("Enter name: ")
                if keyboard.is_pressed('esc'):
                    print("\nExiting the program.")
                    break
                age = int(input("Enter age: "))
                if keyboard.is_pressed('esc'):
                    print("\nExiting the program.")
                    break
                city = input("Enter city: ")
                if keyboard.is_pressed('esc'):
                    print("\nExiting the program.")
                    break

                # Write the collected data to the CSV file
                ra = [name, age, city]
                csv_writer.writerow(ra)
            except ValueError:
                print("Invalid input. Please enter valid data.")
        time.sleep(0.1)  # Small delay to avoid excessive CPU usage
