def stockprofit(prices):
    # Initialize min_price to a large number and max_profit to 0
    min_price = float('inf')
    max_profit = 0
    
    # Loop through each price in the list
    for price in prices:
        # Update min_price if the current price is lower than min_price
        if price < min_price:
            min_price = price
        # Calculate profit if we were to sell at the current price
        profit = price - min_price
        # Update max_profit if the current profit is greater than max_profit
        if profit > max_profit:
            max_profit = profit
    
    return max_profit

# Example usage
print(stockprofit([1, 9, 2, 3, 4, 5]))  # Expected output: 8
