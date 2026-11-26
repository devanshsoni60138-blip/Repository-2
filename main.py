stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

print("===== DEVANSH'S STOCK PORTFOLIO TRACKER =====")
print("Available Stocks:", stock_prices)

while True:
    stock = input("\nEnter stock name (or DONE to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not available!")
        continue

    try:
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue
    except ValueError:
        print("Please enter a valid quantity.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity

print("\n===== DEVANSH'S PORTFOLIO =====")
for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total_investment += value
    print(stock, "-", quantity, "shares =", value)

print("\nTotal Investment Value:", total_investment)
save = input("\nSave result to file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("DEVANSH'S STOCK PORTFOLIO TRACKER\n")
        for stock, quantity in portfolio.items():
            value = stock_prices[stock] * quantity
            file.write(f"{stock} - {quantity} shares = {value}\n")
        file.write(f"Total Investment = {total_investment}\n")
    print("Portfolio saved successfully!")
