class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n=len(nums)
        for i in range(n):
            if i+1<n and nums[i]==nums[i+1]:
                return True
        return False        