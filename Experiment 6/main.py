numbers = [12, 7, 18, 5, 10]
print("Original list:", numbers)

search_value = 18
if search_value in numbers:
    print(search_value, "is in the list.")
else:
    print(search_value, "is not in the list.")

numbers[1] = 8
print("After updating index 1:", numbers)

numbers.append(20)
print("After adding 20:", numbers)

numbers.remove(5)
print("After removing 5:", numbers)

even_numbers = [number for number in numbers if number % 2 == 0]
print("Even numbers:", even_numbers)

numbers.sort()
print("Sorted list:", numbers)
