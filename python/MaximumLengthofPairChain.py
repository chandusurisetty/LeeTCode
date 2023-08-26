class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        sortedpairs=sorted(pairs, key= self.dd)
        print(sortedpairs)
        maxLen=0
        lastVal=None
        for lit in sortedpairs:
            if  lastVal==None:
                maxLen=1
                lastVal=lit[1]
            elif lit[0]>lastVal:
                print(lit,lastVal)
                lastVal=lit[1]
                maxLen+=1
        return maxLen
    def dd(self,eachVal):
        return eachVal[1]
