class Solution:
    def minMovesToSeat(self, seats, students) :
        maxIndex=max(max(seats),max(students))+1
        seatsArray=[0]*maxIndex
        studentsArray=[0]*maxIndex
        for i in seats :
            seatsArray[i]+=1
        for i in students :
            studentsArray[i]+=1
        f,s=0,0
        n=len(seats)
        res=0
        while n:
            if seatsArray[f] == 0 :
                f+=1
            if studentsArray[s] ==0 :
                s+=1
            if seatsArray[f] and studentsArray[s] :
                res+=abs(f-s)
                seatsArray[f] -=1 
                studentsArray[s] -=1
                n-=1
        return res