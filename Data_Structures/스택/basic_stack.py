class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")
    
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def __len__(self):
        return len(self.items)

if __name__ == "__main__":
    S = Stack()
    S.push(10)
    S.push(2)
    print(S.pop())  # Output: 2 
    print(S.top())  # Output: 10
    print(len(S))   # Output: 1
