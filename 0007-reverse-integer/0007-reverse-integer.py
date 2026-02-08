class Solution:
    def reverse(self, x: int) -> int:
        sign=-1 if x<0 else 1
        x *= sign
        rev=int(str(x)[::-1])
        return sign * rev if rev <= 2**31-1 else 0