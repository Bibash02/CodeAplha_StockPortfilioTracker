# predefined stock prices
stock_prices = {
    'AAPL': 180,
    'TSLA': 250,
    'GOOGL': 140,
    'AMZN': 130
}

portfolio = {}
total_investment = 0

print("Welcome to Stock Portfolio Tracker")
print("Available Stocks:", list(stock_prices.keys()))

while True:
    stock = input("Enter stock name: ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter the quantity of stock: "))
        portfolio[stock] = quantity
    else:
        print("Stock not available.")

# calculate total investment
print("Investment summary: ")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment
    print(f"{stock} - {quantity} shares x Rs.{price} = Rs.{investment}")

print("\nTotal Investment values: Rs.", total_investment)

save = input("Do you want to save the result to a file (yes/no): ").lower()

if save == "yes":
    with open("portfolio_summery.txt", "w") as file:
        file.write("Stock Portfolio Summery\n")

        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            investment = price * quantity
            file.write(f"{stock} - {quantity} shares x Rs.{price} = Rs.{investment}\n")
        file.write(f"\n Total investment: Rs.{total_investment}")
    
    print("portfolio saved to portfolio_summery.txt")

