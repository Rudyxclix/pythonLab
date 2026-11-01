file_name = "books.txt"
open(file_name, "a", encoding="utf-8").close()

while True:
    print("\n1. Add a book")
    print("2. Search by title or author")
    print("3. Display all books")
    print("4. Count books")
    print("5. Display books by author")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter book title: ").strip()
        author = input("Enter author: ").strip()
        if title and author and "|" not in title and "|" not in author:
            with open(file_name, "a", encoding="utf-8") as file:
                file.write(title + "|" + author + "\n")
            print("Book added.")
        else:
            print("Title and author are required; do not use |.")

    elif choice == "2":
        search_text = input("Enter title or author to search: ").strip().lower()
        with open(file_name, "r", encoding="utf-8") as file:
            books = [line.strip() for line in file if line.strip()]
        matches = [
            book for book in books
            if search_text in book.lower()
        ]
        if matches:
            for book in matches:
                title, author = book.split("|", 1)
                print("Title:", title, "| Author:", author)
        else:
            print("No matching books found.")

    elif choice == "3":
        with open(file_name, "r", encoding="utf-8") as file:
            books = [line.strip() for line in file if line.strip()]
        if books:
            for book in books:
                title, author = book.split("|", 1)
                print("Title:", title, "| Author:", author)
        else:
            print("No books in the catalogue.")

    elif choice == "4":
        with open(file_name, "r", encoding="utf-8") as file:
            book_count = sum(1 for line in file if line.strip())
        print("Total number of books:", book_count)

    elif choice == "5":
        author_name = input("Enter author name: ").strip().lower()
        with open(file_name, "r", encoding="utf-8") as file:
            books = [line.strip() for line in file if line.strip()]
        matches = [
            book for book in books
            if book.split("|", 1)[1].strip().lower() == author_name
        ]
        if matches:
            for book in matches:
                title, author = book.split("|", 1)
                print("Title:", title, "| Author:", author)
        else:
            print("No books found for this author.")

    elif choice == "6":
        print("Goodbye.")
        break

    else:
        print("Invalid choice.")
