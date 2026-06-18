class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # turn array into a set
        # if the length of the set > len list then there were duplicates
        # unique = set(nums)
        # if len(unique) < len(nums):
        #     return True
        # return False
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
