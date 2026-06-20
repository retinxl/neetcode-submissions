class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # sort input
        #use each number in the array as a possible first value
        # i, a = index, current value at that index
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]: 
                #if we're not at the beginnging and this value is equal to the last one
                #then skip it so we don't use this value twice in the same position in the result
                continue
            # use two sum 2 solution for the remained
            l, r = i + 1, len(nums)-1 # initialize at one index over and the end
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0 :
                    r -= 1
                elif threeSum < 0:
                    l +=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums [l-1] and l < r:
                        l += 1

        return res
