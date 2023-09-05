class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        newHead=None
        newTemp=None
        temp=head
        dictc={}
        while temp:
            if newHead==None:
                newHead=Node(temp.val)
            
                newTemp=newHead
                
            else:
                newTemp.next=Node(temp.val)
                newTemp=newTemp.next  
            dictc[temp]=newTemp   
            temp=temp.next 
            
        temp=head
        newTemp=newHead
        while temp:
            if temp.random==None:
                newTemp.random=None
            else:
                newTemp.random=dictc[temp.random]
            temp=temp.next
            newTemp=newTemp.next
            
        

        return newHead
