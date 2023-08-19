class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) ->Optional[ListNode]:
        return self.addLink(l1,l2,0,None)
        
    def addLink(self,l1,l2,carrer,prev):
        if l1 or l2 or carrer:
            
            c=(l1.val if l1 else 0)+  (l2.val if l2 else 0) +  carrer
            carrer=c//10
            current=c%10

            temp=ListNode(current)
            if prev:
                prev.next=temp
            
            
            self.addLink(l1.next if l1 else 0,l2.next if l2 else 0 ,carrer,temp)
            return temp
