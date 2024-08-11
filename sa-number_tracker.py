```python
import os

def display_numbers():
    if not os.path.exists("numbers.txt"):
        print("No numbers found.")
        return
    with open("numbers.txt", "r") as file:
        numbers = file.readlines()
        print("Tracked Numbers:")
        for line in numbers:
            print(line.strip())

def add_number():
    new_number = input("Enter the phone number to track: ")
    with open("numbers.txt", "a") as file:
        file.write(new_number + "\n")
    print(f"Number {new_number} added.")

def main():
    while True:
        print("\nNumber Tracking Tool")
        print("1. Add a number")
        print("2. Display numbers")
        print("3. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            add_number()
        elif choice == '2':
            display_numbers()
        elif choice == '3':
            print("Exiting the tool...")
            break
        else:
            print("Invalid option, please choose again.")

if __name__ == "__main__":
    main()
```