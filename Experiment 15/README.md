# Experiment 15: Input Validation Using Regular Expressions

## Aim
To validate email and Indian mobile number examples and extract transaction IDs with regular expressions.

## Algorithm
1. Match email examples against a simple email pattern.
2. Match phone examples against exactly 10 digits, beginning with 6, 7, 8, or 9.
3. Use `re.findall()` to extract IDs in the `TXN` followed by four digits format.

## Sample output
```text
Email validation:
student@example.com - valid
student@.com - invalid
Phone validation (10 digits, starts with 6, 7, 8, or 9):
9876543210 - valid
5123456789 - invalid
Transaction IDs: ['TXN1234', 'TXN5678']
```

## Explanation
The examples are built into the program. The patterns use character ranges and repetition counts to check the required formats.
