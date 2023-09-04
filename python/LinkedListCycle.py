class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        lit=[]
        temp=head
        while temp:
            if temp in lit:
                return True
            lit.append(temp)
            temp=temp.next
