# Stock Portfolio Tracker - CodeAlpha Internship
# Author: NARA SAI PRAKASH NAIDU

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "MSFT": 310,
    "AMZN": 145
}

# Store user's portfolio
portfolio = {}

print("Welcome to the Stock Portfolio Tracker")
print("Available stocks:", ', '.join(stock_prices.keys()))

while True:
    stock = input("Enter stock symbol (or type 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    elif stock in stock_prices:
        try:
            quantity = int(input(f"Enter quantity for {stock}: "))
            portfolio[stock] = portfolio.get(stock, 0) + quantity
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("Stock not found. Please enter a valid symbol.")

# Calculate total investment
total_investment = 0
print("\nYour Portfolio Summary:")
for stock, qty in portfolio.items():
    value = qty * stock_prices[stock]
    print(f"- {stock}: {qty} shares x ₹{stock_prices[stock]} = ₹{value}")
    total_investment += value

print(f"\nTotal Investment Value: ₹{total_investment}")

# Save result to file (optional)
save_choice = input("\nDo you want to save this to a file? (yes/no): ").lower()
if save_choice == 'yes':
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary:\n")
        for stock, qty in portfolio.items():
            value = qty * stock_prices[stock]
            file.write(f"{stock}: {qty} shares x ₹{stock_prices[stock]} = ₹{value}\n")
        file.write(f"\nTotal Investment Value: ₹{total_investment}")
    print("Portfolio saved to 'portfolio_summary.txt'.")

print("Thank you for using the Stock Portfolio Tracker!")
