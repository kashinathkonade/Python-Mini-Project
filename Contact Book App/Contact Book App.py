# Dictionary to store contact information
contacts = {}

# Infinite loop to continuously run the Contact Book App
while True:
    # Display the menu
    print('\n========== Contact Book App ==========')
    print('1. Create a new contact')
    print('2. View a contact')
    print('3. Update an existing contact')
    print('4. Delete a contact')
    print('5. Search for a contact')
    print('6. Count total contacts')
    print('7. Exit')
    print('======================================')

    # Prompt the user to choose an action
    choice = input("Enter your choice (1-7): ")

    # Option 1: Create a new contact
    if choice == '1':
        name = input("Enter the contact name: ").strip()
        # Check if the contact already exists
        if name in contacts:
            print(f'Contact with the name "{name}" already exists! Please try a different name.')
        else:
            age = input('Enter age: ')
            email = input('Enter email: ')
            mobile = input('Enter mobile number: ')
            # Add the new contact to the dictionary
            contacts[name] = {'age': int(age), 'email': email, 'mobile': mobile}
            print(f'Success! Contact "{name}" has been created.')

    # Option 2: View a specific contact
    elif choice == '2':
        name = input('Enter the contact name you want to view: ').strip()
        # Check if the contact exists
        if name in contacts:
            contact = contacts[name]
            print(f'\nContact Details:\nName: {name}\nAge: {contact["age"]}\nEmail: {contact["email"]}\nMobile: {contact["mobile"]}')
        else:
            print(f'No contact found with the name "{name}".')

    # Option 3: Update an existing contact
    elif choice == '3':
        name = input("Enter the name of the contact you want to update: ").strip()
        # Check if the contact exists
        if name in contacts:
            age = input('Enter the updated age: ')
            email = input('Enter the updated email: ')
            mobile = input('Enter the updated mobile number: ')
            # Update the contact details
            contacts[name] = {'age': int(age), 'email': email, 'mobile': mobile}
            print(f'Success! Contact "{name}" has been updated.')
        else:
            print(f'No contact found with the name "{name}".')

    # Option 4: Delete a contact
    elif choice == '4':
        name = input('Enter the name of the contact you want to delete: ').strip()
        # Check if the contact exists
        if name in contacts:
            del contacts[name]
            print(f'Contact "{name}" has been successfully deleted!')
        else:
            print(f'No contact found with the name "{name}".')

    # Option 5: Search for a contact by name
    elif choice == '5':
        search_name = input('Enter the contact name to search: ').strip()
        found = False
        # Search for matching contacts
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f'\nFound Contact:\nName: {name}\nAge: {contact["age"]}\nMobile: {contact["mobile"]}\nEmail: {contact["email"]}')
                found = True
        if not found:
            print(f'No contacts found matching "{search_name}".')

    # Option 6: Count total contacts
    elif choice == '6':
        total_contacts = len(contacts)
        if total_contacts == 0:
            print('Your contact book is empty. Start by adding some contacts!')
        else:
            print(f'Total contacts in your book: {total_contacts}')

    # Option 7: Exit the application
    elif choice == '7':
        print('Thank you for using the Contact Book App! Goodbye...')
        break  # Exit the loop to close the app

    # Invalid input handling
    else:
        print('Invalid choice! Please enter a number between 1 and 7.')

    # Extra spacing for readability in the CLI
    print('--------------------------------------')
