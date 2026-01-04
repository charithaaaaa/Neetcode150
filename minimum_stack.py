class MinStack:

    def __init__(self):
        self.main_stack=[]
        self.min_stack=[]

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        if not self.min_stack or val<= self.min_stack[-1]:
            self.min_stack.append(val)
        
    def pop(self) -> None:
        if self.main_stack[-1]==self.min_stack[-1]:
            self.min_stack.pop() #pop from min Stack only if it is equal to main
        self.main_stack.pop()#pop anyway
        

    def top(self) -> int:
        return self.main_stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]
        
# Example usage:
min_stack = MinStack()      
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.getMin())  # Output: -3
min_stack.pop()
print(min_stack.top())      # Output: 0
print(min_stack.getMin())   # Output: -2

