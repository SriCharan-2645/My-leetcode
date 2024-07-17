"""
121. Best Time to Buy and Sell Stock
Easy
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

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""

#use two pointers
#time O(n)
#memory O(1)

class Solution:
    def maxProfit(self, prices):
        max_profit = 0 # because it is given if no profit return 0
        buy = 0
        sell = 1 # because we can only do one transaction a day
        while sell < len(prices):
            current_profit = prices[sell] - prices[buy]
            max_profit = max(max_profit,current_profit)
            if current_profit <= 0:
                buy += 1
                if buy == sell:
                    sell += 1
            else:
                sell += 1
        return max_profit

def main():
    sol = Solution()
    prices = [1,2,4,2,5,7,2,4,9,0,9]
    result = sol.maxProfit(prices)
    print(result)

if __name__ == "__main__":
    main()