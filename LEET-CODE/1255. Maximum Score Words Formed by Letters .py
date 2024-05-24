from typing import Counter

class Solution:
    def maxScoreWords(self, words, letters, score) :
        new_dict=Counter(letters)
        def valid(word):
            wordCount=Counter(word)
            for count in wordCount:
                if wordCount[count]>new_dict[count]:
                    return False
            return True
        def getScore(word):
            value=0
            for ele in word:
                value+=score[(ord(ele))-97]
            return value
        def helper(i):
            if i == len(words):
                return 0
            res = helper(i+1)
            if valid(words[i]):
                for c in words[i]:
                    new_dict[c]-=1
                res = max(res,getScore(words[i])+helper(i+1))
                for c in words[i]:
                    new_dict[c]+=1
            return res
        return helper(0)