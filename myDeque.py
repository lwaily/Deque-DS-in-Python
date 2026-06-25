"""
    Name:  Ali Alwaily
    Date:  25 June 2026
    About: This is really my first python program (I knew C, Java, and C++
            before I've now dipped my hands into Python). In this file, I
            implement the Deque Data Structure.
           Deques (pronounced: "deck") (a.k.a. double-sided queues) are a data
            structure that allows for INSERTION and REMOVAL at both ends of
            a list. Essentially, it is a stack and queue in one!
           The deque is implemented here using the python list as the
            backing array.
"""

#DEQUE CLASS
class myDeque:
    #CONSTRUCTOR
    def __init__(self):
        self.newDeque = []
        self.dequeSize = 0

    #SIZE
    def size(self):
        return self.dequeSize

    #ELEMENT ACCESS
    def front(self):
        if self.dequeSize > 0:
            return self.newDeque[0]
        return None

    def back(self):
        if self.dequeSize > 0:
            return self.newDeque[self.dequeSize-1]
        return None

    #ELEMENT INSERTION
    def prepend(self, element):
        temp = []
        temp.append(element)
        for e in self.newDeque:
            temp.append(e)
        self.newDeque = temp
        self.dequeSize += 1

    def append(self, element):
        self.newDeque.append(element)
        self.dequeSize += 1

    #ELEMENT REMOVAL
    def leftPop(self):
        if self.dequeSize > 0:
            self.newDeque.pop(0)
            self.dequeSize -= 1

    def rightPop(self):
        if self.dequeSize > 0:
            self.newDeque.remove(self.back())
            self.dequeSize -= 1

    def clear(self):
        while(self.dequeSize != 0):
            self.leftPop()

    #ELEMENT SEARCH
    def count(self, element):
        result = 0
        for e in self.newDeque:
            if element == e:
                result += 1
        return result

    #PRINT
    def printElements(self):
        for i in self.newDeque:
            print(i)

    #LIST MANIPULATION
    def reverse(self):
        temp = []
        while(self.dequeSize != 0):
            temp.append(self.back())
            self.rightPop()
        self.newDeque = temp


#TESTS (COMMENTED OUT)
"""
d1 = myDeque()
print("Size:")
print(d1.size())

print("\nAppend - Call Front - Left Pop:")
d1.append(1)
d1.append(2)
d1.append(3)
print("Size:")
print(d1.size())
print(d1.front())
d1.leftPop()
print("Size:")
print(d1.size())
print(d1.front())
d1.leftPop()
print("Size:")
print(d1.size())
print(d1.front())
d1.leftPop()

print("\nAppend - Call Front - Right Pop:")
d1.append(1)
print("Size:")
print(d1.size())
d1.append(2)
print("Size:")
print(d1.size())
d1.append(3)
print("Size:")
print(d1.size())
print(d1.front())
d1.rightPop()
print(d1.front())
d1.rightPop()
print(d1.front())
d1.rightPop()

print("\nPrepend - Call Front - Left Pop:")
d1.prepend(1)
d1.prepend(2)
d1.prepend(3)
print(d1.front())
d1.leftPop()
print(d1.front())
print("Size:")
print(d1.size())
d1.leftPop()
print(d1.front())
d1.leftPop()

print("\nPrepend - Call Front - Right Pop:")
d1.prepend(1)
d1.prepend(2)
print("Size:")
print(d1.size())
d1.prepend(3)
print(d1.front())
d1.rightPop()
print(d1.front())
d1.rightPop()
print(d1.front())
d1.rightPop()
print("Size:")
print(d1.size())

#

print("\nAppend - Call back - Left Pop:")
d1.append(1)
print("Size:")
print(d1.size())
d1.append(2)
print("Size:")
print(d1.size())
d1.append(3)
print("Size:")
print(d1.size())
print(d1.back())
d1.leftPop()
print(d1.back())
print("Size:")
print(d1.size())
d1.leftPop()
print("Size:")
print(d1.size())
print(d1.back())
d1.leftPop()
print("Size:")
print(d1.size())

print("\nAppend - Call back - Right Pop:")
d1.append(1)
d1.append(2)
d1.append(3)
print(d1.back())
d1.rightPop()
print(d1.back())
d1.rightPop()
print(d1.back())
d1.rightPop()

print("\nPrepend - Call back - Left Pop:")
d1.prepend(1)
d1.prepend(2)
d1.prepend(3)
print(d1.back())
d1.leftPop()
print(d1.back())
d1.leftPop()
print(d1.back())
d1.leftPop()

print("\nPrepend - Call back - Right Pop:")
d1.prepend(1)
d1.prepend(2)
d1.prepend(3)
print(d1.back())
d1.rightPop()
print(d1.back())
d1.rightPop()
print(d1.back())
d1.rightPop()

print("\nClear Test:")
d1.prepend(1)
d1.prepend(2)
d1.prepend(3)
print(d1.size())
d1.clear()
print(d1.size())

print("\nCount Test:")
d1.prepend(1)
d1.prepend(2)
d1.prepend(3)
d1.prepend(1)
d1.prepend(5)
d1.prepend(6)
print(d1.count(1))

print("\nReverse Test:")
d1.clear()
d1.append(1)
d1.append(2)
d1.append(3)
d1.append(4)
d1.append(5)
d1.append(6)
print("Print:")
d1.printElements()
d1.reverse()
print("Print Reverse:")
d1.printElements()
"""
