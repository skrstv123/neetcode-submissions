# import sortedcontainers
class Solution:
    def isPalindrome(self, s: str) -> bool:

        def isvalid(c):
            return c.isalnum() 

        def comp(i,j,s):
            return s[i].lower() == s[j].lower()

        def moveij(i,j,s):
            while i <= j and not isvalid(s[i]):
                i += 1
            while j >= i and not isvalid(s[j]):
                j -= 1
            return i,j

        n = len(s)

        if n == 1: 
            return True
        elif n < 1:
            return False

        i, j = 0, n - 1
        
        i, j = moveij(i,j,s)
    
        if i < n and j >= 0 and i <= j and not comp(i,j,s):
            return False
        
        while i <= j and comp(i,j,s):
            i += 1
            j -= 1
            i, j = moveij(i,j,s) 
            if i < n and j >= 0 and i <= j and not comp(i,j,s):
                return False
        
        return True
        