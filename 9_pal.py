class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        length = len(x)
        print(f"x = {x} with length of {length}")
        if length == 1:
            return True
        elif length == 2:
            if x[0] == x[1]:
                return True
            else:
                return False
        elif x[0] == x[length - 1]:
            short = ""
            for c in range(1, length - 1):
                short += x[c]
            print(short)
            return self.isPalindrome(short)
        else:
            return False


solution = Solution()
result = solution.isPalindrome(x=1000021)
print(result)
