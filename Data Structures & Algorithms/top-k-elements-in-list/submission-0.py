class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occur = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        #loop through array, add each ele to hasmap
        for num in nums:
            occur[num] = 1 + occur.get(num, 0)

        for a, b in occur.items():
            buckets[b].append(a)

        res = []
        for i in range(len(buckets)-1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res