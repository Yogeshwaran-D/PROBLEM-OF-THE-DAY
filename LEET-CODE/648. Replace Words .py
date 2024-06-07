class Solution:
    def replaceWords(self, dictionary, sentence) :
        new_dict={}
        for word in dictionary:
            new_dict[word]=len(word)
        sentence=sentence.split(" ")
        for i in range(len(sentence)):
            temp=sentence[i]
            res=""
            for j in range(1,len(temp)+1):
                    if temp[:j] in new_dict.keys():
                        if len(temp[:j]) > len(res):
                            res=temp[:j]
            if res !="":
                sentence[i]=res
        return " ".join(sentence)
    
s=Solution()
print(s.replaceWords(dictionary =
["cat","bat","rat"],sentence =
"the cattle was rattled by the battery"))