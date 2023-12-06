class Solution:
    def totalMoney(self, n: int) -> int:
        todayMoney=0
        nweeks=0
        totalMoney=0
        while n>0:
            nweeks+=1

            for i in range(7):
                if n>0:
                    n-=1
                    totalMoney+=(nweeks+i)
                    
        return totalMoney

