# Experiment 8: Comma-Separated Numbers

## Aim
To read comma-separated values and display them as a list and tuple of strings.

## Algorithm
1. Read one line and split it at each comma.
2. Remove surrounding spaces from each value without converting it to a number.
3. Create a tuple and display the count, first and last values, and reversed list.

## Sample input
```text
34, 67, 55, 33, 12, 98
```

## Sample output
```text
List: ['34', '67', '55', '33', '12', '98']
Tuple: ('34', '67', '55', '33', '12', '98')
Number of elements: 6
First element: 34
Last element: 98
Reverse order: ['98', '12', '33', '55', '67', '34']
```

## Explanation
The values remain strings, as shown by their quotes in the list and tuple output.
