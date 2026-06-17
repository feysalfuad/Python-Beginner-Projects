import json

# ---------------- SAVE FUNCTION ----------------
def save_books():
    with open("books.json", "w") as file:
        json.dump(books, file)

# ---------------- LOAD DATA ----------------
try:
    with open("books.json", "r") as file:
        books = json.load(file)
except:
    books = []

# ---------------- MAIN PROGRAM ----------------
print("📚 Library Management System")

while True:

    print("\nWhat would you like to do?")
    print("1. Add Book")
    print("2. View Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Exit")

    choice = input("Choose 1-6: ").strip()

    # ---------------- ADD BOOK ----------------
    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author: ")

        books.append({
            "title": title,
            "author": author,
            "available": True
        })

        save_books()
        print("✅ Book added!")

    # ---------------- VIEW BOOKS ----------------
    elif choice == "2":
        print("\n📖 Books:")

        if len(books) == 0:
            print("No books in library.")
        else:
            for i in range(len(books)):
                status = "Available" if books[i]["available"] else "Borrowed"
                print(f"{i + 1}. {books[i]['title']} by {books[i]['author']} - {status}")

    # ---------------- BORROW BOOK ----------------
    elif choice == "3":

        if not books:
            print("❌ No books available.")

        else:
            print("\n📖 Select a book to borrow:")

            for i in range(len(books)):
                status = "Available" if books[i]["available"] else "Borrowed"
                print(f"{i + 1}. {books[i]['title']} - {status}")

            try:
                book_number = int(input("Enter book number: "))

                if 1 <= book_number <= len(books):

                    if books[book_number - 1]["available"]:
                        books[book_number - 1]["available"] = False
                        save_books()
                        print("✅ Book borrowed!")
                    else:
                        print("❌ Book is already borrowed.")

                else:
                    print("❌ Invalid book number.")

            except:
                print("❌ Please enter a valid number.")

    # ---------------- RETURN BOOK ----------------
    elif choice == "4":

        if not books:
            print("❌ No books in library.")

        else:
            print("\n📖 Select a book to return:")

            for i in range(len(books)):
                status = "Available" if books[i]["available"] else "Borrowed"
                print(f"{i + 1}. {books[i]['title']} - {status}")

            try:
                book_number = int(input("Enter book number: "))

                if 1 <= book_number <= len(books):

                    if not books[book_number - 1]["available"]:
                        books[book_number - 1]["available"] = True
                        save_books()
                        print("✅ Book returned!")
                    else:
                        print("❌ Book is already available.")

                else:
                    print("❌ Invalid book number.")

            except:
                print("❌ Please enter a valid number.")

    # ---------------- SEARCH BOOK ----------------
    elif choice == "5":

        if not books:
            print("❌ No books in library.")

        else:
            search = input("Enter book title or author: ").lower()

            found = False

            print("\n🔍 Search Results:")

            for i in range(len(books)):

                if search in books[i]["title"].lower() or search in books[i]["author"].lower():

                    status = "Available" if books[i]["available"] else "Borrowed"

                    print(f"{i + 1}. {books[i]['title']} by {books[i]['author']} - {status}")

                    found = True

            if not found:
                print("❌ No matching books found.")

    # ---------------- EXIT ----------------
    elif choice == "6":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid choice.")
