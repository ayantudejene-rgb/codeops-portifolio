# Exercise 1:
cities = ["Addis Ababa", "Nairobi", "Addis Ababa", "Kigali", "Nairobi", "Lagos"]
unique_cities = set(cities)
print("Distinct cities:", unique_cities)
print("Number of distinct cities:", len(unique_cities))

# Exercise 2:
groceries = {
    "Bread": 50,
    "Milk": 80,
    "Eggs": 120,
    "Butter": 200,
    "Cheese": 350
}
print("\nGrocery prices:")
for item, price in groceries.items():
    print(f"{item}: {price} ETB")

# Exercise 3:
prices = [100, 250, 400, 80]
with_tax = [p * 1.15 for p in prices]
print("\nPrices with 15% tax:", with_tax)

# Exercise 4:
cheap = [p for p in prices if p < 200]
print("Items under 200 ETB:", cheap)

# Exercise 5:
with open("names.txt", "w") as f:
    f.write("Almaz\nDawit\nTigist\n")
print("\nNames from file:")
with open("names.txt", "r") as f:
    for line in f:
        print(line.strip())

# Exercise 6:
try:
    num = float(input("\nEnter a number to divide 1000 by: "))
    result = 1000 / num
    print(f"1000 / {num} = {result}")
except ValueError:
    print("Error: Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")