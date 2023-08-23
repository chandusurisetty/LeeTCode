class Solution:
    def reorganizeString(self, s: str) -> str:
        self.dic={}
        self.result=""
        for i in s:
            if self.dic.get(i):
                self.dic[i]+=1
            else:
                self.dic[i]=1
        
        self.changeme(sorted(self.dic, key=self.dic.get, reverse=True)) 
        
        
        if len(self.result)==len(s):
            return self.result
        return ""   
    def changeme(self,sortedlit):
        
        if self.dic[sortedlit[0]]!=0 :
            # if self.dic[sortedlit[0]]>1 and len(sortedlit)==1:
            #     return ""
            if self.dic[sortedlit[0]]==1 and len(sortedlit)==1:
                self.result+=sortedlit[0]
                return ""
            if self.dic[sortedlit[0]]>1 and  (len(sortedlit)==1 or self.dic[sortedlit[1]]==0):
                return ""
            if self.dic[sortedlit[0]]>0:
                self.result+=sortedlit[0]
                self.dic[sortedlit[0]]-=1
            if self.dic[sortedlit[1]]>0:
                self.result+=sortedlit[1]
                self.dic[sortedlit[1]]-=1
            self.changeme(sorted(self.dic, key=self.dic.get, reverse=True))
       
            
        return ""
