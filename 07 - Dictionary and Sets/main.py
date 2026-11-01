first_dictionary = {"banana": 3, "apple": 5, "cherry": 2}
print("Items sorted by key:", sorted(first_dictionary.items()))

second_dictionary = {"orange": 4, "grape": 6}
merged_dictionary = first_dictionary.copy()
merged_dictionary.update(second_dictionary)
print("Merged dictionary:", merged_dictionary)

values = ["red", "blue", "red", "green", "blue", "red"]
frequency = {}
for value in values:
    if value in frequency:
        frequency[value] = frequency[value] + 1
    else:
        frequency[value] = 1
print("Element frequencies:", frequency)

first_set = {1, 2, 3, 4}
second_set = {3, 4, 5, 6}
print("Common elements:", sorted(first_set & second_set))
print("Unique to first set:", sorted(first_set - second_set))
print("Unique to second set:", sorted(second_set - first_set))
