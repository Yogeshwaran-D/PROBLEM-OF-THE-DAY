class Solution:
    def minimumPushes(self, word: str) -> int:
        count=Counter(word)
        res=0
        for i,x in enumerate(sorted(count.values(),reverse=True)):
            res+= ((i//8)+1) * x
        return res