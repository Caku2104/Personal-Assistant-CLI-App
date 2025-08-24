import datetime
import os
import json
import random
import requests

notes_file = "notes_assistant.json"

def load_notes():
    if os.path.exists(notes_file):
        with open(notes_file, "r") as file:
            return json.load(file)
    return []

def save_notes(notes):
    with open(notes_file, "w") as f:
        json.dump(notes, f, indent=4)

def show_time():
    right_now = datetime.datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
    date = datetime.date.today()
    print("-----------------------")
    print(f"Today's date: {date}")
    print(f"Right now: {right_now}")
    print("-----------------------")

def notes_menu():
    notes = load_notes()

    while True:
        print("\n\t=== Note Manager Menu ===")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("0. Back to Main Menu")

        choice = input("What would you like to do?: ")

        if choice == "1":
            note_text = input("Enter your note: ")
            if note_text.strip():
                note = {"text": note_text,
                        "timestamp": datetime.date.today().strftime("%Y/%m/%d")}
                notes.append(note)
                save_notes(notes)
                print(f"✅ Note added: {note_text}")
            else:
                print("❌ Note cannot be empty.")
        
        elif choice == "2":
                if notes:
                    print("\n\tYour notes:")
                    for i, note in enumerate(notes, 1):
                        print(f"{i}. {note['text'].capitalize()} ({note['timestamp']})")
                else:
                    print("No notes exist yet.")
        
        elif choice == "3":
            if notes:
                for i, note in enumerate(notes, 1):
                    print(f"{i}. {note['text'].capitalize()} ({note['timestamp']})")
                try:
                    number = int(input("Enter the number of the note to delete: "))
                    if 1 <= number <= len(notes):
                        deleted = notes.pop(number-1)
                        save_notes(notes)
                        print(f"✅ Deleted note: {deleted['text']}")
                    else:
                        print(f"❌ Invalid number. Choose between 1 and {len(notes)}")
                except ValueError:
                    print("❌ Please enter a valid number.")
            else:
                print("No notes to delete.")

        elif choice == "0":
            print("Returning to main menu...\n")
            break
            
        else:
            print("❌ Invalid input. Please enter a number between 0-3.")


def calculator():
    try:
        print("\n\t### Operations ### ")
        print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Power\n6. Root")
        decision = int(input("Please enter your desired operation: "))

        match(decision):
            case 1:
                first = float(input("Enter the first number: "))
                second = float(input("Enter the second number: "))

                result = first + second

            case 2:
                first = float(input("Enter the first number: "))
                second = float(input("Enter the second number: "))

                result = first - second

            case 3:
                first = float(input("Enter the first number: "))
                second = float(input("Enter the second number: "))

                result = first * second
            
            case 4:
                try:
                    first = float(input("Enter the first number: "))
                    second = float(input("Enter the second number: "))

                    result = first / second

                except ZeroDivisionError:
                    print("You cannot divide a number by zero.")
            
            case 5:
                first = float(input("Enter the base number: "))
                second = float(input("Enter the power: "))

                result = first ** second
            
            case 6:
                first = float(input("Enter the base number: "))
                second = float(input("Enter the root: "))

                result = first ** (1/second)
            
            case _:
                print("You have entered an invalid option.")
        
        return f"The result is {result}"

    except ValueError:
        print("Please enter only a valid integer.")            
    

def fun_stuff(): 
    joke_url = "https://api.api-ninjas.com/v1/jokes"
    quote_url = "https://api.api-ninjas.com/v1/quotes"
    
    while True:
        print("\n\t=== Fun Stuff Menu ===")
        print("1. Random number\n2. Random Joke\n3. Random Quote\n0. Back to Main Menu")
        answer = input("What would you like to do? (Enter an integer): ")

        if answer == '1':
            print("Generating a random number in between 1-100.")
            number = random.randint(1,100)
            print(f"Generated number: {number}")

        elif answer == '2':
            joke_response = requests.get(joke_url, headers = {'X-Api-Key': 'pG1oR81HHyL9wHPMwPx9pg==sMoXxst4QO835JRE'})
            if joke_response.status_code == 200:
                random_joke = joke_response.json()[0]
                print(f" --> {random_joke['joke']}")
            else:
                print("Failed to fetch joke: ", joke_response.status_code)

        elif answer == '3':
            quote_response = requests.get(quote_url, headers={'X-Api-Key': 'pG1oR81HHyL9wHPMwPx9pg==sMoXxst4QO835JRE'})
            if quote_response.status_code == 200:
                random_quote = quote_response.json()[0]
                print(f"\tQuote -> {random_quote['quote']}\n\tAuthor -> {random_quote['author']}")
            else:
                print("Failed to fetch quote:", quote_response.status_code)

        elif answer == '0':
            print("Returning to main menu.")
            break

        else:
            print("Please enter one of the available integers.")


def system_tools():
    while True:
        print("\n\t=== System Tools Menu ===")
        print("1. Show current directory")
        print("2. List files")
        print("3. Open a file")
        print("0. Back to Main Menu")
        
        choice = input("What would you like to do? (Enter the preceded integers): ")

        if choice == "1":
            cwd = os.getcwd()
            print("Current working directory is -> ", cwd)
        
        elif choice == "2":
            path = input("Enter directory path (leave empty for current folder): ").strip()
            if not path:
                path = os.getcwd()
            
            try:
                files = os.listdir(path)
                if files:
                    print("Files and folders in ", path)
                    for f in files:
                        print(f)
                else:
                    print("This folder is empty.")

            except FileNotFoundError:
                print("Directory not found!")
            except PermissionError:
                print("You don't have permission to access this folder.")
        
        elif choice == "3":
            file_path = input("Enter the full path of the file to open: ").strip()
            try:
                os.startfile(file_path)
                print("File opened successfully!")
            except FileNotFoundError:
                print("File not found!")
            except Exception as e:
                print("Error:", e)

        elif choice == "0":
            print("Returning to main menu.")
            break
        
        else:
            print("Please enter a valid integer.")


def show_help():
    print("\n\n\t=== Operation Descriptions ===")
    print("1. Date & Time -> Shows current date and time.")
    print("2. Note Manager -> Allows you to create, view or delete your notes and saves them to a file.")
    print("3. Calculator -> Does basic operation + roots and powers by desire.")
    print("4. Fun Stuff -> Displays random numbers, jokes, and quotes using APIs.")
    print("5. System Tools -> Inspects files and directories.")
    print("6. Operation Descriptions -> Shows this menu.")
    print("0. Exit -> Ends the program.\n")


def option_menu():
    print("\n\t=== Personal Assistant ===")
    print("1. Date & Time")
    print("2. Note Manager")
    print("3. Calculator")
    print("4. Fun Stuff")
    print("5. System Tools")
    print("6. Help/Operation Descriptions")
    print("0. Exit")

def main():
    while True:
        
        option_menu()

        choice = input("What would you like to do? (Enter the preceded integers): ")

        if choice == "1":
            show_time()
        
        elif choice == "2":
            notes_menu()
        
        elif choice == "3":
            print(calculator())

        elif choice == "4":
            fun_stuff()
        
        elif choice == "5":
            system_tools()
        
        elif choice == "6":
            show_help()
        
        elif choice == "0":
            print("Goodbye 👋")
            break
        
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
