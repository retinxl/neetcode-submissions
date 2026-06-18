class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        pairs = {}
        for letter in s:
            pairs[letter] = pairs.get(letter, 0) + 1
        
        for letter in t:
            if letter in pairs:
                pairs[letter] -= 1
            else:
                return False
        
        for letter, count in pairs.items():
            if count != 0:
                return False
        return True
