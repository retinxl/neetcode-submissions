class Solution:

    def encode(self, strs: List[str]) -> str:
        global shared_indeces
        text = "" 
        shared_indeces = [0] * len(strs)
        i = 0
        for i in range(len(strs)):
            shared_indeces[i] = len(strs[i])
            #print(shared_indeces[i])
            text += strs[i]
        #print(text)
        return(text)

    def decode(self, s: str) -> List[str]:
        res = []
        for i in shared_indeces:
            #print(i)
            current = 0
            word = ""
            while current < (i):
                #print(current)
                #print(s[current])
                word = word + s[current]
                current += 1
            # print("\n")
            # print(word)
            res.append(word)
            s = s[current:]
            
        return res
