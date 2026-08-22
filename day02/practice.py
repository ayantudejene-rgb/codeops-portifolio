# Exercise 1:
temp = float(input("Enter temperature in °C: "))
if temp < 15:
    print("cold")
elif temp <= 28:
    print("warm")
else:
    print("hot")

# Exercise 2:
print("\nReceipts:")
for i in range(1, 11):
    print(f"Receipt #{i}")

# Exercise 3:
print("\nEven numbers 1–20:")
for num in range(1, 21):
    if num % 2 == 0:
        print(num)

# Exercise 4:
def apply_discount(price, percent=10):
    """Return price after applying a discount percentage."""
    return price * (1 - percent / 100)
print(f"\n1000 ETB with 10% discount: {apply_discount(1000):.2f} ETB")
print(f"1000 ETB with 20% discount: {apply_discount(1000, 20):.2f} ETB")

# Exercise 5:
print("\nCountdown:")
count = 5
while count > 0:
    print(count)
    count -= 1
print("Liftoff")