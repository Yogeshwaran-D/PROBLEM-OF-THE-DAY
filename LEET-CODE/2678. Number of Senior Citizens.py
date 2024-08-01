class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res=0
        for num in details:
            if int(num[-4:-2]) > 60:
                res+=1
        return res