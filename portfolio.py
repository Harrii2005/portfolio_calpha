print("=== Stock Portfolio Tracker ===")

stocks = {
    "TATA": 150,
    "RELIANCE": 280,
    "INFOSYS": 180,
    "WIPRO": 120
}

total = 0

while True:
    stock = input("Enter stock name (TATA, RELIANCE, INFOSYS, WIPRO) or DONE to finish: ").upper()

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