class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return_list = []
        anagrams = {}
        for word in strs:
            single_dict = {}
            for letter in word:
                single_dict[letter] = single_dict.get(letter, 0) + 1
            dict_key = tuple(sorted(single_dict.items()))
            if dict_key in anagrams:
                anagrams[dict_key].append(word)
            else:
                anagrams[dict_key] = [word]
        for letters, words in anagrams.items():
            return_list.append(words)
        return return_list