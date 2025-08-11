import csv

FILENAME = "contacts.csv"

def create_new_file():
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone", "Email"])
    print("Contact file created successfully!\n")


def add_contact():
    name = input("Enter the contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email address: ")
    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email])
    print("Contact added successfully!\n")


def view_contacts():
    try:
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            header = next(reader) 
            print("Contacts Information:")
            print(f"{'Name':<20}  {'Phone':<15}  {'Email':<25}")
            for row in reader:
                print(f"{row[0]:<20}  {row[1]:<15}  {row[2]:<25}")
            print()
    except FileNotFoundError:
        print("No contacts found. Please create the file first.\n")


def modify_contact():
    try:
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            contacts = list(reader)
    except FileNotFoundError:
        print("No contacts file found. Please create the file first.\n")
        return

    if len(contacts) <= 1:
        print("No contacts available to modify.\n")
        return

    print("Contacts Information")
    print(f"{'Name':<20}  {'Phone':<15}  {'Email':<25}")
    for contact in contacts[1:]: 
        print(f"{contact[0]:<20}  {contact[1]:<15}  {contact[2]:<25}")
    print()

    name_to_modify = input("Enter the name of the contact to modify: ").strip().lower()
    
    for i in range(1, len(contacts)):
        if contacts[i][0].strip().lower() == name_to_modify:
            current_name = contacts[i][0]
            current_phone = contacts[i][1]
            current_email = contacts[i][2]

            print(f"\nCurrent details for '{current_name}':")
            print(f"Phone: {current_phone}")
            print(f"Email: {current_email}")

            new_phone = input("Enter new phone number (leave blank to keep current): ").strip()
            new_email = input("Enter new email address (leave blank to keep current): ").strip()

            if new_phone:
                contacts[i][1] = new_phone
            if new_email:
                contacts[i][2] = new_email

            with open(FILENAME, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(contacts)

            print(f"\nContact '{current_name}' updated successfully!\n")
            return

    print(f"\nContact with name '{name_to_modify}' not found.\n")


def main():
    print("Welcome to the Contact Manager App")
    print("-" * 30)

    while True:
        print("Push the following options to perform the corresponding action:")
        print("1 - Create new contact file")
        print("2 - Add new contact")
        print("3 - View all contacts")
        print("4 - Modify an existing contact")
        print("5 - Save and exit")
        choice = input("Enter your selection: ")
        print("-" * 30)

        if choice == "1":
            create_new_file()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            view_contacts()
        elif choice == "4":
            modify_contact()
        elif choice == "5":
            break
        else:
            print("Invalid option. Please try again.\n")

    print("Completed by, Jonathan Jewell") 


if __name__ == "__main__":
    main()