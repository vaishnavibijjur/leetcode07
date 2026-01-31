class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sumN_num=(n*(n+1))//2
        sum_nums=sum(nums)
        missingnum=sumN_num-sum_nums
        return missingnum