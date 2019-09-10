"""
题目三、123.买卖股票的最佳时机

给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
示例 2:

输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。  
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。  
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:

输入: [7,6,4,3,1]
输出: 0
解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。
"""
from heapq import nlargest
def maxProfitIII(prices):
    if  not prices or len(prices) < 2:
        return 0
    profile1 = [0 for i in range(len(prices))]
    profile2 = [0 for i in range(len(prices))]
    max_profile = 0
    min_price = prices[0]
    max_price = prices[len(prices) - 1]
    for i in range(len(prices)):
        min_price = min(min_price, prices[i])
        profile1[i] = max(profile1[i - 1], prices[i] - min_price)

    for j in range(len(prices)-1, -1, -1):
        max_price = max(max_price, prices[j])
        profile2[j] = max(profile2[j - 1], max_price - prices[j])

    for i in range(len(prices)):
        max_profile = max(max_profile, profile1[i] + profile2[i])

    return max_profile

import sys
def maxProfitIII_leetcode(prices):
    if not prices or len(prices) == 1:
        return 0
    sum = 0
    minPrice = sys.maxsize

    count = len(prices)
    profits = [0] * count

    for i, price in enumerate(prices):
        if price > minPrice:
            profit = price - minPrice
            sum = max(sum, profit)
        else:
            minPrice = price
        profits[i] = sum

    maxPrice = 0
    for i in range(count - 1, 0, -1):
        price = prices[i]
        if price < maxPrice:
            secProfit = maxPrice - price
            sum = max(sum, secProfit + profits[i - 1])
        else:
            maxPrice = price

    return sum



def main():
    p = [3,5,0,3,1,4]
    p2 = [7,6,4,3,1]
    p3 = [1,2,3,4,5]
    # print(maxProfitIII(p2))
    print(maxProfitIII_leetcode(p))

if __name__ == '__main__':
    main()