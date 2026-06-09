import json

print("📒 Contact Book")

try:
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
        
except FileNotFoundError:
    contacts = []

while True:
    
    print("\nWhat would you like to do?")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    
    choice = input("Choose 1-5: ").strip()
    
    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        
        contacts.append({
            "name": name,
            "phone": phone
        })
        
        with open("contacts.json", "w") as file:
            json.dump(contacts, file, indent=4)
        
        print("✅ Contact added!")
        
    elif choice == "2":
        print("\n📋 Contacts:")
        
        if len(contacts) == 0:
            print("No contacts yet.")
        else:
            for i in range(len(contacts)):
                print(f"{i + 1}. {contacts[i]['name']} - {contacts[i]['phone']}")
                
    elif choice == "3":
        
        search_name = input("Enter name to search: ").strip().lower()
        
        found = False
        
        for contact in contacts:
            
            if search_name in contact["name"].lower():
                print(f"📞 {contact['name']} - {contact['phone']}")
                found = True
                
        if not found:
            print("❌ Contact not found.")
            
    elif choice == "4":
        
        if not contacts:
            print("❌ No contacts to delete.")
            
        else:
            print("\n📋 Select a contact to delete:")
            
            for i in range(len(contacts)):
                print(f"{i + 1}. {contacts[i]['name']} - {contacts[i]['phone']}")
                
            try:
                contact_number = int(input("Enter contact number: "))
                
                if 1 <= contact_number <= len(contacts):
                    removed = contacts.pop(contact_number - 1)
                    print(f"🗑 Contact deleted: {removed['name']}")
                    
                    with open("contacts.json", "w") as file:
                        json.dump(contacts, file, indent=4)
                    
                else:
                    print("❌ Invalid contact number.")
                    
            except:
                print("❌ Please enter a valid number.")           
            
    
    elif choice == "5":
        print("👋 Goodbye!")
        break
    
    else:
        print("❌ Invalid choice.")
    
