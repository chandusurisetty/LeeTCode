class MyStack:

    def __init__(self):
        self.q=collections.deque()
        
    def push(self, x: int) -> None:

        self.q.append(x)
        
    def pop(self) -> int:
        if self.q:
            val=self.q.pop()
            return val
          
    def top(self) -> int:
        if self.q:
            return self.q[-1]

    def empty(self) -> bool:
        if self.q:
            return False
        return True
        
