class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # make hashmap to hold the occurence
        seen = {}
        # add everything from s1 into hash
        for i in s1:
            seen[i] = 1 + seen.get(i,0)
        
        # for key, val in seen.items():
        #     print(key,val)
        
        # go through s2 in windows
        l, r = 0, len(s1)-1
        while r < len(s2):       
        # if we encounter a sinle letter in that window that is not in hash
            seen_copy = seen.copy()
            for window in range (l, r+1 , 1):
                print(s2[window])
                if s2[window] in seen_copy:
                    seen_copy[s2[window]] -= 1
                else:
                    l = window
                    r = l + len(s1)-1
                    break
                


            count = 0
            for i in seen_copy.values():
                if i == 0:
                    count += 1
            
            if count == len(seen_copy):
                return True

            r += 1
            l += 1



        # increment to that index + 1 and start again
        # return True if when looping through window we reach right ptr and it was in hash
        # return False otherwise
        return False

