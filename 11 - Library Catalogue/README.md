# Experiment 11: Library Catalogue Using Text Files

## Aim
To add, search, list, and count books in a text-file catalogue.

## Algorithm
1. Open `books.txt` in append mode to create it if it is missing.
2. Show a menu for adding books, searching, listing, counting, author lookup, or exit.
3. Store each book as `title|author`, one book per line, and read the file for queries.

## Sample interaction
```text
Enter your choice: 1
Enter book title: Python Basics
Enter author: A. Kumar
Book added.
Enter your choice: 4
Total number of books: 1
Enter your choice: 6
Goodbye.
```

## Explanation
The program uses relative file path `books.txt` in the experiment folder. New books are appended so existing entries are preserved.
