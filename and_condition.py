class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums.sort()
        k = len(nums)
        for i in range(k):
            
            if i >= len(nums):
                break
            elif i < len(nums)-1:
                # and 条件判断是短路机制，index溢出问题，可以在常规判断条件之前，and一个长度判断
                while i+1<len(nums) and nums[i] == nums[i+1]  :
                    del nums[i+1]
            else:
                break
        return len(nums)