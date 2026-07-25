"""
Author : Janarddan Sarkar
file_name : 4_best_time_to_buy_&_sell_stock.py 
date : 14-09-2025
description :
🔹 Problem Statement: Best Time to Buy and Sell Stock

You are given an array prices[] where:
prices[i] = stock price on day i.
You can: Choose one day to buy, Choose a later day to sell,

Maximize the profit.
⚠️ You can only make one transaction (buy once, sell once).
Return:
Maximum profit (or 0 if no profit is possible).
🔹 Example 1
prices = [7, 1, 5, 3, 6, 4]

Buy on day 1 (price = 1),
Sell on day 4 (price = 6),

Profit = 6 - 1 = 5 ✅

Answer = 5
"""

# Bruteforce - O(n**2)
def maxProfit1(prices):
    n = len(prices)
    max_profit = 0

    for i in range(n):
        for j in range(i+1, n):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)

    return max_profit

# Optimized - O(n)
def maxProfit2(prices):
    min_num = float('inf')
    max_profit = 0

    for price in prices:
        min_num = min(min_num, price)
        curr_profit = price - min_num
        max_profit = max(curr_profit, max_profit)

    return max_profit

if __name__ == "__main__":
    print(maxProfit1([7, 1, 5, 3, 6, 4]))
    print(maxProfit2([7, 1, 5, 3, 6, 4]))