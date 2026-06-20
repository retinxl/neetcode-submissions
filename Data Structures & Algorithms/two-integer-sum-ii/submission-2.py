class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # ptr1 = len(numbers)-1
        # ptr2 = 0

        #move ptr1 to target
        # for i in range(len(numbers)-1,-1,-1):
        #     complament = target - numbers[i]
        #     while (ptr2 <= complament):
        #         if numbers[ptr2] == complament:
        #             return [ptr2+1, i+1]
        #         ptr2 += 1
        l, r = 0, len(numbers)-1
        while l != r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            if numbers[l] + numbers[r] < target:
                l += 1
            if numbers[l] + numbers[r] == target:
                return[l+1,r+1]
        return []
            