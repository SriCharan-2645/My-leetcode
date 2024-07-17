#solve this problem using two pointers method.
#time complexity : O(N) bcoz we have to iter thourgh all the characters in worst case.
#space comp: O(1) bcoz we only used constant space for each operation.
# even though we have l,r new variables, they used constant space for each iteration through out

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #pointer
        l = 0 #start
        r = len(s)-1 #end

        #we will only run until the point where these two pointers cross each other.
        while l<r:
            while l<r and self.alphaNumeric(s[l]) == False: #if not alphanumeric we increase pointer
                l += 1
            while r>l and self.alphaNumeric(s[r]) == False:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l,r = l+1, r-1
        return True



    #helper function to check the ascii values of the character
    def alphaNumeric(self,c):
        return(ord('A') <= ord(c) <= ord('Z') or
               ord('a') <= ord(c) <= ord('z') or
               ord('0') <= ord(c) <= ord('9'))

#main
def main():
    solutionOBJ = Solution()
    test = '0P'
    result = solutionOBJ.isPalindrome(test)
    print(result)
if __name__ == '__main__':
    main()
