class Solution:
    def kthSmallestPrimeFraction(self, arr, k):
        n=len(arr)
        new_dict={}
        for i in range(n):
            for j in range(i+1,n):
                new_dict[arr[i]/arr[j]]=[arr[i],arr[j]]
        new_dict_keys=new_dict.keys()
        new_dict_keys=sorted(new_dict_keys)
        return new_dict[new_dict_keys[k-1]]