class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        getSub=""
        for i in s:
            if getSub:
                if i ==getSub[0]:
                    
                    if not s.replace(getSub,""):
                        return True
                    getSub+=i
                else:
                    getSub+=i

            else:
                getSub=i
        return False
                
