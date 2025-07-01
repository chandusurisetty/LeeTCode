class Solution:
    def possibleStringCount(self, word: str) -> int:
        count=0
        prev=""
        for i in word:
            if prev!=i:
                prev=i
            else:
                count+=1
       
        return count+1
        
