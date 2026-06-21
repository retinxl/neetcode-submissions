class Solution:
    def trap(self, height: List[int]) -> int:
        #take the min of (max left, max right)
        #that min - current height = how much water is there
        #how to track max on left
        lmax, rmax =  height[0], height[len(height)-1]
        l, r = 0, len(height)-1 # index at 1 bc ind 0 always 0
        water = 0
        # for i in range(1,len(height)):
            
        #     w = min(l_max,r_max)-height[l]
        #     l_max = max(l_max, height[l])
        #     r_max = max(r_max, height[r])
        if not height: return 0
        # initialize left and right pts, index 0 and end

        #initialize left and right max, height of respective indeces
        # result to hold water total
        while l < r:
            if lmax < rmax:
                l += 1
                #order matters here, bc computation comes first
                #we dont have to worry about negatives
                lmax = max(lmax,height[l])
                water += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax,height[r])
                water += rmax - height[r]
        return water