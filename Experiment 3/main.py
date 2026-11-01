terms = int(input("Enter the number of terms: "))

if terms <= 0:
    print("Enter a positive number of terms.")
else:
    first = 0
    second = 1
    print("Fibonacci series:")
    for count in range(terms):
        print(first, end=" ")
        first, second = second, first + second
    print()
