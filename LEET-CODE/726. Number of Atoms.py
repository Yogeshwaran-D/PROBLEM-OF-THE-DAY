from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula) :
        stack=[defaultdict(int)]
        i=0
        while i<len(formula):
            if formula[i] == "(":
                stack.append(defaultdict(int))
            elif formula[i] == ")":
                cur_map=stack.pop()
                count=""
                while i+1 < len(formula) and formula[i+1].isdigit():
                    count+=formula[i+1]
                    i+=1
                count= 1 if not count else int(count)
                prev_map=stack[-1]
                for element in cur_map:
                    prev_map[element] += cur_map[element] * count 
            else:
                element=formula[i]
                count=""
                if i+1 < len(formula) and formula[i+1].islower():
                    element=formula[i:i+2]
                    i+=1
                while i+1 < len(formula) and formula[i+1].isdigit():
                    count+=formula[i+1]
                    i+=1
                count= 1 if not count else int(count)
                cur_map=stack[-1]
                cur_map[element]+=count
            i+=1
        count_map=stack[-1]
        res=""
        for element in sorted(count_map.keys()):
            count= "" if count_map[element] == 1 else str(count_map[element])
            res+=element+count
        return res