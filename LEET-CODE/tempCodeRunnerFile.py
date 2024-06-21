maxProfit=[0,0,0]
        currentProfit=[0,0,0]
        left=0
        m=minutes
        for right in range(len(customers)):
            if m==0 :
                currentProfit=[currentProfit[0]-customers[left]+customers[right],left+1,right]
                left+=1
                if  currentProfit[0]> maxProfit[0]:
                    maxProfit=currentProfit
            else:
                currentProfit=[currentProfit[0]+customers[right],left,right]
                maxProfit=currentProfit
                m-=1
        print(maxProfit)