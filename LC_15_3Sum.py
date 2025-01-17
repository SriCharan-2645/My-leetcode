"""
15. 3Sum
Medium
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""


class Solution:
    def threeSum(self, nums):
        # first we need to sort the list
        nums.sort()
        # this is o(nlogn)
        result = []
        # next we need to perform two sum on rest of the list target = 0 - first number in list
        for i in range(0, len(nums) - 1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = 0 - nums[i]
            #we need to start l from next number of the selected starting number.
            l, r = i+1, len(nums) - 1
            # for j in range(i+1, len(nums)):
            while l < r:
                currentSum = nums[l] + nums[r]
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    currentList = [nums[i], nums[l], nums[r]]
                    result.append(currentList)
                    l += 1
                    # we just update left pointer, and check if next number is also same, then we again update left
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return result

# class Solution: # neetcode
#     def threeSum(self, nums):
#         res = []
#         nums.sort()
#
#         for i, a in enumerate(nums):
#             # Skip positive integers
#             if a > 0:
#                 break
#
#             if i > 0 and a == nums[i - 1]:
#                 continue
#
#             l, r = i + 1, len(nums) - 1
#             while l < r:
#                 threeSum = a + nums[l] + nums[r]
#                 if threeSum > 0:
#                     r -= 1
#                 elif threeSum < 0:
#                     l += 1
#                 else:
#                     res.append([a, nums[l], nums[r]])
#                     l += 1
#                     r -= 1
#                     while nums[l] == nums[l - 1] and l < r:
#                         l += 1
#
#         return res


def main():
    sol = Solution()
    # Input: nums = [-1,0,1,2,-1,-4]
    # Output: [[-1,-1,2],[-1,0,1]]
    nums = [0,0,0]
    result = sol.threeSum(nums)
    print(result)


if __name__ == '__main__':
    main()

#%%
