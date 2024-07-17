"""
3. Longest Substring Without Repeating Characters
Medium

Given a string s, find the length of the longest
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        charSet = set()
        maxCount = 0 # here count cannot be negative because input string has a min length of 0
        l = 0
        #here our main goal is to check if ther are any duplicates present in the substring r-l and get the len(r-l).
        for r in range(len(s)):
            while s[r] in charSet: # here for each index/char we check if it is already present in the charSet. #while runs until there is not duplicate char in the set
                charSet.remove(s[l]) # we remove the first pointer variable.
                l += 1 # we move forward, if ther is a duplicate.
            charSet.add(s[r])
            #r += 1
            maxCount = max(maxCount,r-l+1) #here the range of r starts from 0 so we take +1 to include right most value
        return maxCount

def main():
    sol = Solution()
    s = "pwwkew"
    result = sol.lengthOfLongestSubstring(s)
    print(result)


if __name__ == "__main__":
    main()



