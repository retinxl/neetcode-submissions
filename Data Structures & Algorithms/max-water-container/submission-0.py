class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # just brute force it 
        # largest_area = min(heights[len(heights)-1],heights[0])*(len(heights)-1)
        # for i in range(len(heights)-1):
        #     for j in range(i+1, len(heights)):
        #         area = min(heights[i], heights[j]) * (j - i)
        #         largest_area = max(largest_area, area)

        # return(largest_area)
        # res area initialize
        # left ptr loops throuh each val
            #right ptr does the same but starting one step ahead
            #calculate area: w(r-l) * h(min of the 2 pts)
            #compute max of original area and current
        #return
        #this was brute force i did above

        # start l and r ptr at opposite ends for larget height
        # shift ptr that is smaller, bc you can potentially increase is
        # update area as you go
        # shift smaller ptr and check if area is larger
        # if the ptrs are equal, shift the one with a greater potential
        # shift smaller, check area
        # shift smaller, check area
        # terminating condition, l == r
        l, r = 0, len(heights)-1
        greatest_area = 0
        while l < r:
            area = (r-l) * min(heights[l],heights[r])
            greatest_area = max(greatest_area, area)
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                if heights[l+1] < heights[r-1]:
                    l += 1
                else:
                    r -= 1
        return greatest_area



