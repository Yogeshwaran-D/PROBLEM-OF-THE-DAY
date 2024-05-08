class Solution:
    def findRelativeRanks(self, score):
        revScore=sorted(score,reverse=True)
        n=len(score)
        new_dict={}
        for i in range(n):
            new_dict[revScore[i]]=i
        for j in range(n):
            place=new_dict.get(score[j])
            if place == 0 :
                score[j]="Gold Medal"
            elif place == 1 :
                score[j]="Silver Medal"
            elif place == 2 :
                score[j]="Bronze Medal"
            else:
                score[j]=f'{place+1}'
        return score