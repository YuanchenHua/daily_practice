class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:


        length = len(nums)
        if not nums or length == 0: return 0
        p = 0
        q = 1
        # while循环有时候比 for 好用，相当于回归java
        while (q < length):
            if nums[p] != nums[q]:
                nums[p+1] = nums[q]
                p += 1
            q += 1
        return p+1