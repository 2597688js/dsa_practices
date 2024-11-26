"""
Author : Janarddan Sarkar
file_name : 22.best_time_to_buy_and_sell_stocks.py 
date : 27-11-2024
description : Leetcode 121: Best time to buy and sell stocks

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:

1 <= prices.length <= 10**5
0 <= prices[i] <= 10**4
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            min_price = min(price, min_price)
            curr_profit = price - min_price
            max_profit = max(max_profit, curr_profit)

        return max_profit


# Testing the function
if __name__ == "__main__":
    # Test case 1
    prices1 = [7, 1, 5, 3, 6, 4]
    solution = Solution()
    print("Test Case 1 Output:", solution.maxProfit(prices1))  # Expected output: 5

    # Test case 2
    prices2 = [7, 6, 4, 3, 1]
    print("Test Case 2 Output:", solution.maxProfit(prices2))  # Expected output: 0