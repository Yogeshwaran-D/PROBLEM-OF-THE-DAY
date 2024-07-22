class Solution:
    def sortPeople(self, names, heights) :
        new_dict={}
        n=len(heights)
        for i in range(n):
            new_dict[heights[i]]=names[i]
        heights.sort(reverse=True)
        for i in range(n):
            names[i]=new_dict.get(heights[i])
        return names