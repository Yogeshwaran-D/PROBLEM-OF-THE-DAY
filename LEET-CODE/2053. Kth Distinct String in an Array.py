class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        frequency={}
        for ele in arr:
            frequency[ele]=1+frequency.get(ele,0)
        i=0
        for key,value in frequency.items():
            if frequency.get(key)==1:
                i+=1
                if i== k :
                    return key
        return ""