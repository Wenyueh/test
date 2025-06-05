from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Find the smallest positive integer that is not present in nums.
        
        Algorithm:
        1. First pass: Replace all non-positive numbers and numbers > n with a placeholder
        2. Second pass: For each number x in range [1, n], mark nums[x-1] as negative
        3. Third pass: Find the first positive number, its index + 1 is the answer
        
        Time: O(n), Space: O(1)
        """
        n = len(nums)
        
        # Step 1: Replace all numbers <= 0 or > n with n+1
        # We use n+1 as a placeholder because it's out of our range of interest [1, n]
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
        
        # Step 2: Use the sign of nums[i] to mark presence of number i+1
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                # Mark nums[num-1] as negative to indicate that 'num' is present
                if nums[num - 1] > 0:
                    nums[num - 1] = -nums[num - 1]
        
        # Step 3: Find the first positive number
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        # If all numbers from 1 to n are present, return n+1
        return n + 1
