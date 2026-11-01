import re

email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
phone_pattern = r"^[6-9][0-9]{9}$"

emails = ["student@example.com", "student@.com"]
print("Email validation:")
for email in emails:
    if re.fullmatch(email_pattern, email):
        print(email, "- valid")
    else:
        print(email, "- invalid")

phone_numbers = ["9876543210", "5123456789"]
print("Phone validation (10 digits, starts with 6, 7, 8, or 9):")
for phone in phone_numbers:
    if re.fullmatch(phone_pattern, phone):
        print(phone, "- valid")
    else:
        print(phone, "- invalid")

log_text = "Payment TXN1234 completed; refund TXN5678 pending."
transaction_ids = re.findall(r"TXN[0-9]{4}", log_text)
print("Transaction IDs:", transaction_ids)
