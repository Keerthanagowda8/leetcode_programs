class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str=str(x)
        y=x_str[::-1]
        if x_str==y:
            return True
        else:
            return False