class Solution:
    def survivedRobotsHealths(self, positions, healths, directions) :
        new_dict={}
        for i in range(len(positions)):
            new_dict[positions[i]]=i
        positions.sort()
        stack=[]
        for robot in positions:
            i=new_dict[robot]
            if directions[i] == "R":
                stack.append(i)
            else :
                while  stack and healths[i] :
                    j=stack.pop()
                    if healths[i] > healths[j]:
                        healths[j]=0
                        healths[i]-=1
                    elif healths[i] < healths[j]:
                        healths[j]-=1
                        healths[i]=0
                        stack.append(j)
                    else:
                        healths[i]=0
                        healths[j]=0
                
        return [x for x in healths if x !=0 ]
