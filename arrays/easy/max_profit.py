#!/usr/bin/python3

class Solution:
    def max_profit(self, prices):
        max_profit, min_price = 0, float('inf')
        
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(profit, max_profit)
        return max_profit
