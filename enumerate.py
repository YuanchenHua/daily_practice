class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        # enumerate 可以转换为迭代器
        for ind,num in enumerate(nums):
            hashmap[num] = ind
        for i,num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i!=j:
                return [i,j]
