class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n ^ 2)
        # i = 0 
        # while i in range(len(nums)):
        #     j = i + 1
        #     while j in range(len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        #         j += 1
        #     i += 1
        seen = {}
        for index, item in enumerate(nums):
            complament = target - item
            if complament in seen:
                return [seen[complament], index]
            else:
                seen[item] = index