class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1=version1.split('.') 
        v2=version2.split('.')
        v1Len=len(v1)
        v2Len=len(v2)
        maxLen=max(v1Len,v2Len)
        for i in range(maxLen):
            n1=0 if i>= v1Len else int(v1[i])
            n2=0 if i>= v2Len else int(v2[i])
            if n1>n2:
                return 1
            elif n2>n1:
                return -1
        return 0