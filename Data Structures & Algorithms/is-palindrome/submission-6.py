# import sortedcontainers
class Solution:
    def isPalindrome(self, s: str) -> bool:

        def isvalid(c):
            return c.isalnum() 
        def comp(i,j,s):
            return s[i].lower() == s[j].lower()

        n = len(s)

        if n == 1: 
            return True
        elif n < 1:
            return False

        i, j = 0, n - 1
        
        while i <= j and not isvalid(s[i]):
            i += 1
        while j >= i and not isvalid(s[j]):
            j -= 1
        
        if i < n and j >= 0 and i <= j and not comp(i,j,s):
            return False
        
        # print(i, j, s[i], s[j])

        while i <= j and comp(i,j,s):

            i += 1
            j -= 1
           
            while i <= j and not isvalid(s[i]):
                i += 1
         
            while j >= i and not isvalid(s[j]):
                j -= 1

            # print(i, j, s[i], s[j])
            if i < n and j >= 0 and i <= j and not comp(i,j,s):
                # print('came here', i, j, s[i], s[j])
                return False
        
        return True
        