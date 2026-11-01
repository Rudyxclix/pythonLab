# Experiment 12: Electricity Bill and Exception Handling

## Aim
To calculate an electricity bill with a slab tariff and demonstrate exception handling.

## Example lab tariff
- First 100 units: ₹1.50 per unit
- Next 100 units: ₹2.50 per unit
- Units above 200: ₹4.00 per unit

This is an example tariff for the lab, not an official electricity tariff.

## Algorithm
1. Read units inside a `try` block and reject negative values.
2. Use `except` for invalid input, `else` to calculate a valid bill, and `finally` to print a completion message.

## Sample input
```text
150
```

## Sample output
```text
Bill amount: ₹275.00
Bill calculation finished.
```

## Explanation
The bill is calculated separately for the units in each slab. Invalid numbers and negative units are reported.
