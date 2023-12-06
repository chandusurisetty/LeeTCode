class Solution:
    def largestGoodInteger(self, num: str) -> str:
        first=""
        second=""
        maxval=-1

        for i in num:
            if first=="":
                first=i
            else:
                if first==i:
                    if second=="":
                        second=i
                    else:
                        if second==i:
                            if maxval<int(i):
                                
                                maxval=int(i)
                                print(maxval)
                        else:
                            first=""
                            second=""
                else:
                    first=i
                    second=""
            
        if maxval==-1:
            return ""
        results= str(maxval)*3
        return results


            
