class Solution:
    def frequencySort(self, nums) :
        count={}
        for num in nums:
            count[num]=1+count.get(num,0)
        frequencies={}
        for key,value in count.items():
            if frequencies.get(value):
                frequencies[value].append(key)
            else:
                frequencies[value]=[key]
        res=[]
        for frequency in sorted(list(frequencies.keys())):
            temp=frequencies[frequency]
            temp.sort(reverse=True)
            for num in temp:
                for i in range(frequency):
                    res.append(num)
        return res
