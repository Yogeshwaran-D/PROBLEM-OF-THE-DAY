class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        s=0
        e=len(people)-1
        boatCount=0
        while(s<=e):
            if people[s]+people[e] <= limit:
                s+=1
            boatCount+=1
            e-=1
        return boatCount