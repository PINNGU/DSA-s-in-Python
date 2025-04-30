#stack , simplest to recreate in python
#used in recursion and other places , a  LAST IN, FIRST OUT data structure , similar to a stack of papers or plates 
#popular methods are push (to the top) , and pop (from the top) elements of stack
#i will also add type so its similar to some other non dynamic programming languages
import sys


class STACK():

    stack = []
    def __init__(self,types):
        if types == 'int' or 'float' or 'str' or 'bool':
            self.type = types 
        else:
            sys.exit("ERR:Creation:Wrong stack type.")

    def push(self,val):
        if self.type in str(type(val)):
            self.stack.append(val)
            return val
        else:
            sys.exit("ERR:Push:Wrong stack type.")

    def pop(self):

        if self.stack[-1]:
            val = self.stack[-1]
            del self.stack[-1]
            return val
        else:
            sys.exit("ERR:Pop:Stack empty.")
    
    def type_of(self):
        print(self.type)

    def peek(self):
        pass

    def is_empty(self):
        pass

    def size(self):
        pass

    def __str__(self):
        pass
    
stack1 = STACK('int')


stack1.push(7)
stack1.push(14)

#stack1.push(True) err
#stack1.push("klsk") err

x = stack1.pop()
print(x)
stack1.pop()

#stack1.pop() err

stack2 = STACK('str')
stack2.push("yo")
stack2.push("here")
stack2.push("blue")

stack3 = STACK('float')
stack3.push(14.3)
stack3.push(92.14)
stack3.push(4.182)




