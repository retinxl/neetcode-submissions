class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #brute force
        # res = nums.copy()
        # current = 0
        # for i in range(0, len(nums)):
        #     product = 1
        #     for j in range(0,len(nums)):
        #         #print(i, j, nums[j])
        #         if j != i:
        #             product *= nums[j]
        #     res[i] = product
        # return res
        left, right, result = ([1] * len(nums) for i in range(3))
        for i in range(1,len(nums)):
            left[i] = nums[i-1]*left[i-1]

        for i in range(len(nums)-2,-1,-1):
            right[i] = nums[i+1] * right[i+1]

        for i in range(0,len(result)):
            result[i] = left[i] * right[i]
            
        return result
