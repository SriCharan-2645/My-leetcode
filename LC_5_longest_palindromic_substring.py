"""
5. Longest Palindromic Substring
Medium

Given a string s, return the longest
palindromic

substring
 in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):
            for l, r in ((i,i), (i,i+1)): # odd and even lengths checked simultaneoulsy, 1st while runs for odd, then runs for even for same i, then i gets updated.
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    if (r - l + 1) > len(res):
                        res = s[l:r + 1]
                    l -= 1
                    r += 1

        return res

def main():
    sol = Solution()
    s = "cbbd"
    res = sol.longestPalindrome(s)
    print(res)

if __name__ == '__main__':
    main()