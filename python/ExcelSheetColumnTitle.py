class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        self.results=""
        self.getme(columnNumber)
        return self.results
    def getme(self, num):
        if num>26:
            if num%26!=0:

                self.results=chr(num%26+64)+self.results
                self.getme(num//26)
            else:
                self.results="Z"+self.results
                self.getme(num//26-1)
        else:
            self.results=chr(num+64)+self.results
