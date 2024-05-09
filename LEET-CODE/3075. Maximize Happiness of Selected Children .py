class Solution:
    def maximumHappinessSum(self, happiness, k):
        reversedHappiness = sorted(happiness,reverse=True)
        sumOfHappiness=0
        for  i in range (k):
            value = reversedHappiness[i] - i
            if value > 0:
               sumOfHappiness+=value
        return sumOfHappiness 