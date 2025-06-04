all_my_contacts = []

def add_a_contact():
    """
    Adds one new contact.
    Each contact is a DICTIONARY.
    Phone number and address are TUPLES inside the dictionary.
    """
    print("\n--- Add a New Contact ---")

    name = input("What's the contact's name? ")
    phone_part1 = input("Phone - Part 1 (e.g., Country Code): ")
    phone_part2 = input("Phone - Part 2 (e.g., Area Code): ")
    phone_part3 = input("Phone - Part 3 (e.g., Local Number): ")
    my_phone_tuple = (phone_part1, phone_part2, phone_part3)
    address_part1 = input("Address - Part 1 (e.g., Street Name): ")
    address_part2 = input("Address - Part 2 (e.g., City): ")
    my_address_tuple = (address_part1, address_part2)

    new_contact_info = {
        'name': name,
        'phone': my_phone_tuple,     
        'address': my_address_tuple  
    }

    all_my_contacts.append(new_contact_info)
    print(f"'{name}' has been added!")

def show_all_contacts():
    """
    Displays every contact currently in our list.
    Shows how to get data from the LIST, then DICTIONARY, then TUPLE.
    """
    print("\n--- Your Contacts List ---")
    if not all_my_contacts: 
        print("No contacts to show yet. Add some first!")
        return
    for i, contact in enumerate(all_my_contacts):
        print(f"\nContact {i+1}:") 
        print(f"  Name: {contact['name']}")
        print(f"  Phone: {contact['phone'][0]} {contact['phone'][1]}-{contact['phone'][2]}")
        print(f"  Address: {contact['address'][0]}, {contact['address'][1]}")
    print("------------------------")


def start_contact_manager():
    """Runs the simple contact manager with a menu."""
    while True:
        print("\n--- Menu ---")
        print("1. Add a contact")
        print("2. Show all contacts")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            add_a_contact()
        elif choice == '2':
            show_all_contacts()
        elif choice == '3':
            print("Exiting. See you next time!")
            break
        else:
            print("That's not a valid option. Please try again.")
if __name__ == "__main__":
    start_contact_manager()