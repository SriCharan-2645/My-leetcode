"""
20. Valid Parentheses
Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {')': '(', ']': '[', '}': '{'}
        for i in s:
            # check if our char is a closing bracket.
            if i in close_to_open:
                # check if stack is not empty and last element is this value.
                if stack and stack[-1] == close_to_open[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return True if not stack else False # we only return True if the stack is emtpy, else false


def main():
    sol = Solution()
    s = "[["
    result = sol.isValid(s)
    print(result)


if __name__ == '__main__':
    main()

