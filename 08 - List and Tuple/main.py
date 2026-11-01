input_text = input("Enter comma-separated values: ")
values = [value.strip() for value in input_text.split(",")]

if len(values) == 1 and values[0] == "":
    values = []

value_tuple = tuple(values)
print("List:", values)
print("Tuple:", value_tuple)
print("Number of elements:", len(values))

if values:
    print("First element:", values[0])
    print("Last element:", values[-1])
    print("Reverse order:", values[::-1])
else:
    print("No values were entered.")
