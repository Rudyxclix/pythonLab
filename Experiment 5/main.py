text = input("Enter a string: ")

print("\n1. Replace a character")
print("2. Reverse the string")
print("3. Check palindrome")
print("4. Count a character")
print("5. Count words")
choice = input("Enter your choice: ")

if choice == "1":
    old_character = input("Character to replace: ")
    new_character = input("Replacement character: ")
    print("Result:", text.replace(old_character, new_character))
elif choice == "2":
    print("Reversed string:", text[::-1])
elif choice == "3":
    if text == text[::-1]:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
elif choice == "4":
    character = input("Character to count: ")
    print("Frequency:", text.count(character))
elif choice == "5":
    print("Number of words:", len(text.split()))
else:
    print("Invalid choice.")
