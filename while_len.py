class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        # List remove之后，原来i+1的就到了i的位置，所以i的位置要重新判断一次，不能+1

        while i < len(nums):
            if nums[i]==val:
                nums.remove(val)
                
            else:
                i +=1
        return len(nums)