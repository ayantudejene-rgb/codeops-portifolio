# day03
def load_stock(filename="stock.txt"):
    """Load stock from a file into a dictionary.
       Returns empty dict if file not found."""
    stock = {}
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if line:  # skip empty lines
                    item, qty = line.split(",")
                    stock[item] = int(qty)
    except FileNotFoundError:
        print(f"Warning: {filename} not found. Starting with empty stock.")
    return stock
def save_stock(stock, filename="stock.txt"):
    """Write the stock dictionary back to the file."""
    with open(filename, "w") as f:
        for item, qty in stock.items():
            f.write(f"{item},{qty}\n")
def adjust(stock, item, amount):
    """Increase (positive) or decrease (negative) an item's quantity.
       New items are added with amount if they don't exist."""
    stock[item] = stock.get(item, 0) + amount
def display_low_stock(stock, threshold=10):
    """Print items with quantity below threshold."""
    low_items = [item for item, qty in stock.items() if qty < threshold]
    if low_items:
        print("\nLow stock items (below {}):".format(threshold))
        for item in low_items:
            print(f"  {item}: {stock[item]}")
    else:
        print("\nAll items are above the low-stock threshold.")
stock = load_stock()
print("Current stock:")
for item, qty in stock.items():
    print(f"  {item}: {qty}")
adjust(stock, "Paracetamol", 5)  
adjust(stock, "Bandages", -3)        
adjust(stock, "NewItem", 10)         

print("\nAfter adjustments:")
for item, qty in stock.items():
    print(f"  {item}: {qty}")
display_low_stock(stock)
save_stock(stock)
print("\nStock saved to stock.txt")