print("=== Stock Portfolio Tracker ===")

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 300
}

total = 0

while True:
    stock = input("Enter stock name (AAPL, TSLA, GOOGL, MSFT) or DONE to finish: ").upper()

    if stock == "DONE":
        break

    if stock in stocks:
        try:
            qty = int(input("Enter quantity: "))

            value = stocks[stock] * qty
            total += value

            print(f"Value of {stock} = {value}")

        except ValueError:
            print("Please enter a valid number!")
    else:
        print("Stock not found!")

print("\nTotal Investment Value =", total)