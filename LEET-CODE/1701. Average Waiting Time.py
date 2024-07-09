class Solution:
    def averageWaitingTime(self, customers):
        waiting = 0
        temp = customers[0][0]
        for ele in customers:
            temp =max( temp+ele[1] , ele[0]+ele[1] )
            waiting += temp - ele[0]
        return waiting / len(customers)