"""
424. Longest Repeating Character Replacement
Medium
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.



Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achive this answer too.


Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""

from datetime import datetime
class Solution:
    def characterReplacement(self, s: str, k: int):
        # taking O(n) time but not efficient for long strings because if performs for loop on every single substring.
        # res = 0  # because max length of the string cannot be negative.
        # l, r = 0, 0
        # while r <= len(s):  # O(n)
        #     dict1 = {}  # initialise dict
        #     subStr = s[l:r]
        #     for i in subStr:  # O(n)
        #         if i in dict1:
        #             dict1[i] = dict1.get(i) + 1
        #         else:
        #             dict1[i] = 1
        #     maxK = 0
        #     for key, value in dict1.items():  # constant time any substring there are only 26 alphabets.
        #         currentMax = value
        #         maxK = max(maxK, currentMax)
        #     if len(subStr) - maxK <= k:
        #         cur = r-l
        #         res = max(res,cur)
        #         r += 1
        #     else:
        #         l += 1
        # return res

        # same O(n) time but little efficient because we are not looping in every substring.
        dict1 = {}
        res = 0
        l = 0
        for r in range(len(s)):
            dict1[s[r]] = dict1.get(s[r], 0) + 1  # we are adding r index character to dict

            while (r-l+1) - max(dict1.values()) > k:  # here if our numer of variables to change is grater than K we need to increment l window
                dict1[s[l]] = dict1.get(s[l]) - 1
                l += 1

            res = max(res, r-l+1)
        return res




def main():
    sol = Solution()
    s = "AABABBA"
    k = 1
    start = datetime.now()
    result = sol.characterReplacement(s, k)
    end = datetime.now()
    print(result)
    print(end - start)


if __name__ == "__main__":
    main()

