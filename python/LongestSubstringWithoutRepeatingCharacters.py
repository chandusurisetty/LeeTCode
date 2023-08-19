class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr=""
        count=0
        for i in s:
            if i not in substr:
                substr+=i
            else:
                if len(substr)>count:
                    count=len(substr)
                ind=substr.index(i)
                if len(substr)>ind+1:
                    substr=substr[ind+1:]+i
                else:
                    substr=i
        if count<len(substr):
            return len(substr)
        return count
            
