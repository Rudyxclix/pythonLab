number = int(input("Enter an integer: "))

if number < 2:
    is_prime = False
else:
    is_prime = True
    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break

if is_prime:
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")
