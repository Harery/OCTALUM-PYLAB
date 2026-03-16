"""
LeetCode #118: Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly
above it as shown:

        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1

Example 1:
    Input: numRows = 5
    Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
    Input: numRows = 1
    Output: [[1]]

Constraints:
    - 1 <= numRows <= 30
"""

from typing import List


class Solution:
    """
    Solution class for Pascal's Triangle.

    Time Complexity: O(numRows^2) - total number of elements generated
    Space Complexity: O(numRows^2) - storing all rows
    """

    def solve(self, numRows: int) -> List[List[int]]:
        """
        Generate Pascal's Triangle with numRows rows.

        Args:
            numRows: Number of rows to generate

        Returns:
            List of lists representing Pascal's Triangle
        """
        if numRows == 0:
            return []

        result: List[List[int]] = [[1]]

        for i in range(1, numRows):
            prev_row = result[i - 1]
            current_row = [1]  # First element is always 1

            # Calculate middle elements
            for j in range(1, i):
                current_row.append(prev_row[j - 1] + prev_row[j])

            current_row.append(1)  # Last element is always 1
            result.append(current_row)

        return result


if __name__ == "__main__":
    solution = Solution()

    # Test case 1: 5 rows
    result1 = solution.solve(5)
    expected1 = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    print(f"Test 1: numRows=5")
    for row in result1:
        print(f"  {row}")
    assert result1 == expected1

    # Test case 2: Single row
    result2 = solution.solve(1)
    print(f"Test 2: numRows=1 -> {result2}")
    assert result2 == [[1]]

    # Test case 3: Two rows
    result3 = solution.solve(2)
    print(f"Test 3: numRows=2 -> {result3}")
    assert result3 == [[1], [1, 1]]

    # Test case 4: Three rows
    result4 = solution.solve(3)
    print(f"Test 4: numRows=3 -> {result4}")
    assert result4 == [[1], [1, 1], [1, 2, 1]]

    # Test case 5: Seven rows (verify larger values)
    result5 = solution.solve(7)
    print(f"Test 5: numRows=7")
    for row in result5:
        print(f"  {row}")
    assert result5[6] == [1, 6, 15, 20, 15, 6, 1]

    # Test case 6: Verify symmetry
    result6 = solution.solve(6)
    for i, row in enumerate(result6):
        assert row == row[::-1], f"Row {i} is not symmetric: {row}"
    print("Test 6: All rows are symmetric")

    print("\nAll tests passed!")
