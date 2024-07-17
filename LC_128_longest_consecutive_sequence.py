"""
128. Longest Consecutive Sequence
Medium

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""


class Solution:
    def longestConsecutive(self, nums):
        # create a set to take only unique values
        numSet = set(nums)
        longest = 0  # sequence counter
        for n in numSet:
            # we will start the sequence only if that value does not have a before value
            if (n - 1) not in numSet:
                current_length = 0
                # check if current value (n) + currnet_length in numSet eg ( 3+2 = 5 should be in numset)
                while n + current_length in numSet:
                    current_length += 1
                    longest = max(longest, current_length)
        return longest


def main():
    sol = Solution()
    nums = [100,4,200,1,3,2]
    result = sol.longestConsecutive(nums)
    print(result)


if __name__ == "__main__":
    main()
