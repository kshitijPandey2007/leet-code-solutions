class Solution(object):
    def isPalindrome(self,x):
        rev=0;
        original=x;
        if x<0:
            return False
        
        while (x!=0):
            rev=rev*10+x%10;
            x=x//10;
        if rev==original:
            return True
        else:
            return False
        
        
if __name__ == "__main__":
    sol = Solution()
    test_cases = [121, -121, 10, 0, 12321, 123]
    
    for num in test_cases:
        print(f"isPalindrome({num}): {sol.isPalindrome(num)}")
      
        
        
