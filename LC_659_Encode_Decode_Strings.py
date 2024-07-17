"""
Premium Question:
Description
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

our idea:
    # input = ["Hi", "this","is","an","example"]
    # encoded: 2#Hi4#this2#is2#an7#example
    # output = ["Hi", "this","is","an","example"]
to write length of each word before word followed by a symbol for ease of recognition.
 Note: we cannot simply store the length of these words outside because the question says stateless. ( we cannot store)
Example1

Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"

Example2

Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"

Tags
Google
"""


# solution
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        # write your code here
        # to hold result strings
        res = ""
        for i in strs:
            new_string = str(len(i)) + '#' + i
            res = res + new_string
        return res

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, str):
        # write your code here
        i = 0
        res = []
        while i < len(str):
            j = i
            length = 0
            if str[j + 1] == '#':
                length = int(str[i])
            new_string = str[i + 2:i + 2 + length]
            res.append(new_string)
            i = i + 2 + length
        return res


def main():
    sol = Solution()
    inputS = ["Hi", "this", "is", "an", "example"]
    encoded = sol.encode(inputS)
    decoded = sol.decode(encoded)
    print(encoded)
    print(decoded)
    print(inputS == decoded)


if __name__ == '__main__':
    main()
