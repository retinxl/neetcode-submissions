class Solution:
    def isPalindrome(self, s: str) -> bool:
        # loop through string
        cleaned = ""
        for i in s:
            if i.isalnum(): # add every alphanum char to a str
                cleaned += i.lower()
        print(cleaned)
        print(len(cleaned))
        midpoint = len(cleaned)//2  # get the midpoint
        
        i = 0
        # loop from index 0 -> midpoint
        # check if index i == index len - i
        while i < midpoint:
            if cleaned[i] != cleaned[len(cleaned)-1-i]:
                return False
            i += 1
        return True
