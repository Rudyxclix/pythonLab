print("Example lab tariff: first 100 units ₹1.50/unit, next 100 ₹2.50/unit, above 200 ₹4.00/unit.")

try:
    units = float(input("Enter electricity units consumed: "))
    if units < 0:
        raise ValueError("Units cannot be negative.")
except ValueError as error:
    print("Invalid input:", error)
else:
    if units <= 100:
        bill = units * 1.50
    elif units <= 200:
        bill = (100 * 1.50) + ((units - 100) * 2.50)
    else:
        bill = (100 * 1.50) + (100 * 2.50) + ((units - 200) * 4.00)
    print("Bill amount: ₹" + format(bill, ".2f"))
finally:
    print("Bill calculation finished.")
