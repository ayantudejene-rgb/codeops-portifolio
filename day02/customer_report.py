# TeleBirr Customer Tier Report
customers = [
    ("Almaz", 1500),
    ("Dawit", 700),
    ("Tigist", 200),
    ("Hanna", 1200),
    ("Samuel", 450),
    ("Bontu", 980),
]
def tier(balance):
    """Return tier based on TeleBirr balance."""
    if balance >= 1000:
        return "Premium"
    elif balance >= 500:
        return "Standard"
    else:
        return "Basic"
premium_count = 0
standard_count = 0
basic_count = 0
print("=== TeleBirr Customer Report ===\n")
for name, balance in customers:
    t = tier(balance)
    print(f"{name}: {t} ({balance} ETB)")

    # Update counters
    if t == "Premium":
        premium_count += 1
    elif t == "Standard":
        standard_count += 1
    else:
        basic_count += 1
print("\n--- Summary ---")
print(f"Premium customers:  {premium_count}")
print(f"Standard customers: {standard_count}")
print(f"Basic customers:    {basic_count}")