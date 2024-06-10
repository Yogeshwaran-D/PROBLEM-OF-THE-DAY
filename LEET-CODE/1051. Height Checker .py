class Solution:
    def heightChecker(self, heights) :
        count=[0]*101
        arr=[]
        res=0
        for i in heights:
            count[i]+=1
        for i in range(1,101):
            while count[i]>0:
                arr.append(i)
                count[i]-=1
        for i in range(len(heights)):
            if heights[i] != arr[i] :
                res+=1
        return res

        # n=len(heights)
        # index=0
        # temp=sorted(heights)
        # for i in range(n):
        #     if heights[i]!=temp[i]:
        #         index+=1
        # return index