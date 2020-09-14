"""
Given an array of i.th elements, whihc is the price of the stockon day i.

Design an algorithm to return the maximun profit.
Note.  cannot sell a stock before buy one.
Return None if no profit.

example:
    Input: [7, 1, 4, 3, 6, 5]  Output: 5
    Buy on day 1 (array index) and sell on day 5, profit = 6 - 1: 5
"""

def max_profit(stocks):
    if not stocks:
        return None

    res = 0
    min = stocks[0]

    for price in stocks:
        if min > price:
            min = price

        res = max(res, (price - min))
    return res

stocks = [7, 1, 4, 3, 6, 5]
print(str(stocks) + ' profit: ' + str(max_profit(stocks)))

stocks = [123, 110, 40, 32, 66, 57]
print(str(stocks) + ' profit: ' + str(max_profit(stocks)))
