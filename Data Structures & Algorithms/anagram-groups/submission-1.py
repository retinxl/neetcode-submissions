class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # return_list = []
        # anagrams = {}
        # for word in strs:
        #     single_dict = {}
        #     for letter in word:
        #         single_dict[letter] = single_dict.get(letter, 0) + 1
        #     dict_key = tuple(sorted(single_dict.items()))
        #     if dict_key in anagrams:
        #         anagrams[dict_key].append(word)
        #     else:
        #         anagrams[dict_key] = [word]
        # for letters, words in anagrams.items():
        #     return_list.append(words)
        # return return_list


        # make an array for each word that becomes asci number counter
        # make the array the key, and add the word to the list of values
        # return the list of value
        res = defaultdict(list)
        for word in strs:
            holder = [0] * 26

            for letter in word:
                # increment the index for each time letter occurs
                holder[ord(letter) - ord("a")] += 1
            res[tuple(holder)].append(word)
        return list(res.values())

