"""
11. Container With Most Water
Medium

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.



Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1


Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

# Brute force O(n^2)
#solution O(n)
#solution memory O(1)
class Solution:
    def maxArea(self, height):
        max_area = 0 # we initialise with 0 because here, area cannot be negative in given case.
        l = 0
        r = len(height)-1
        while l < r:
            width = r - l
            hght = min(height[l],height[r])
            area = width * hght
            max_area = max(max_area,area)
            #update pointers
            #check edge case:
            if height[l] == height[r]: #edge case
                if height[l+1] > height[r-1]:
                    l += 1
                else:
                    r -= 1
            #regular case
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area

def main():
    sol = Solution()
    height = [1,1]
    result = sol.maxArea(height)
    print(result)

if __name__ == '__main__':
    main()

#%%