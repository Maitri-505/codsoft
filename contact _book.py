contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        contacts[name] = phone
        print("Contact Added!")

    elif choice == "2":
        if contacts:
            for name, phone in contacts.items():
                print(name, ":", phone)
        else:
            print("No Contacts.")

    elif choice == "3":
        name = input("Enter Name: ")
        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Contact Not Found")

    elif choice == "4":
        name = input("Enter Name: ")
        if name in contacts:
            del contacts[name]
            print("Contact Deleted")
        else:
            print("Contact Not Found")

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid Choice")