"""
LeetCode #121: Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock
on the ith day.

You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you
cannot achieve any profit, return 0.

Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 1 (price = 1) and sell on day 4 (price = 6),
                 profit = 6-1 = 5.

Example 2:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: No transactions are done and the max profit = 0.

Constraints:
    - 1 <= prices.length <= 10^5
    - 0 <= prices[i] <= 10^4
"""

from typing import List


class Solution:
    """
    Solution class for Best Time to Buy and Sell Stock.

    Time Complexity: O(n) - single pass through prices
    Space Complexity: O(1) - only tracking min price and max profit
    """

    def solve(self, prices: List[int]) -> int:
        """
        Calculate maximum profit from one buy and one sell transaction.

        Args:
            prices: List of stock prices for each day

        Returns:
            Maximum profit achievable (0 if no profit possible)
        """
        if not prices:
            return 0

        min_price = float("inf")
        max_profit = 0

        for price in prices:
            # Update minimum price seen so far
            if price < min_price:
                min_price = price

            # Calculate profit if selling today and update max
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit

        return max_profit


if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Standard case with profit
    prices1 = [7, 1, 5, 3, 6, 4]
    result1 = solution.solve(prices1)
    print(f"Test 1: prices={prices1} -> profit={result1}")
    assert result1 == 5

    # Test case 2: Decreasing prices, no profit
    prices2 = [7, 6, 4, 3, 1]
    result2 = solution.solve(prices2)
    print(f"Test 2: prices={prices2} -> profit={result2}")
    assert result2 == 0

    # Test case 3: Single day
    prices3 = [5]
    result3 = solution.solve(prices3)
    print(f"Test 3: prices={prices3} -> profit={result3}")
    assert result3 == 0

    # Test case 4: Two days with profit
    prices4 = [1, 5]
    result4 = solution.solve(prices4)
    print(f"Test 4: prices={prices4} -> profit={result4}")
    assert result4 == 4

    # Test case 5: Two days no profit
    prices5 = [5, 1]
    result5 = solution.solve(prices5)
    print(f"Test 5: prices={prices5} -> profit={result5}")
    assert result5 == 0

    # Test case 6: All same prices
    prices6 = [3, 3, 3, 3]
    result6 = solution.solve(prices6)
    print(f"Test 6: prices={prices6} -> profit={result6}")
    assert result6 == 0

    # Test case 7: Profit at the end
    prices7 = [3, 2, 1, 4]
    result7 = solution.solve(prices7)
    print(f"Test 7: prices={prices7} -> profit={result7}")
    assert result7 == 3

    # Test case 8: Buy at minimum, sell at maximum
    prices8 = [2, 4, 1, 5, 3, 6]
    result8 = solution.solve(prices8)
    print(f"Test 8: prices={prices8} -> profit={result8}")
    assert result8 == 5

    print("\nAll tests passed!")
