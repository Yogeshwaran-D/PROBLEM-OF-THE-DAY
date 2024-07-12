class Solution:
    def maximumGain(self, s, x , y ) :
        
        def pairs_remover(pair,points):
            nonlocal s
            res=0
            stack=[]
            for ele in s:
                if ele == pair[1] and stack and stack[-1] == pair[0] :
                    stack.pop()
                    res+=points
                else:
                    stack.append(ele)
            s="".join(stack)
            return res

        score=0
        pair= "ab" if x > y else "ba"
        score+=pairs_remover(pair,max(x,y))
        score+=pairs_remover(pair[::-1],min(x,y))
        return score