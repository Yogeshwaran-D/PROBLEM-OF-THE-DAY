class Solution:
    def sortJumbled(self, mapping , nums) :
        mapped_dict={}
        res=[]
        for num in nums:
            str_num=str(num)
            temp=0
            for ele in str_num:
                temp*=10
                temp+=mapping[int(ele)]
            if mapped_dict.get(temp):
                mapped_dict[temp].append(num)
            else:
                mapped_dict[temp]=[num]
        for i in sorted(list(mapped_dict.keys())):
            res+=mapped_dict.get(i)
        return res