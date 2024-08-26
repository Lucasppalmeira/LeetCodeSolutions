def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        reversed = x[::-1]
        
        if(x == reversed):
            return True
        else:
            return False

print(isPalindrome(1221))