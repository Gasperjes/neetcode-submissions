class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i in range(len(nums)):
            diff = target - nums[i]
            if hashmap.get(diff,-1) != -1:
                return [hashmap[diff], i]
            hashmap[nums[i]] = i
        return [0,0]