class Stack:
    def __init__(self):
        self.__stk = []


    def push(self, val):
        self.__stk.append(val)


    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__counter = 0


    def get_counter(self):
        return self.__counter
    

    def push(self, value):
        Stack.push(self, value)
        self.__counter += 1


    def pop(self):
        value = Stack.pop(self)
        self.__counter -= 1
        return value
	

stk = CountingStack()
for i in range(100):
    stk.push(i)

for i in range(99):
    stk.pop()

print(stk.get_counter())