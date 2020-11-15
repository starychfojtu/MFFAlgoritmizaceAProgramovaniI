import LinkedList as ll

class Stack:
    def __init__(self):
        self.__list = ll.LinkedList()

    def push(self, value):
        self.__list.prepend(value)

    def pop(self):
        return self.__list.pop()

    def count(self):
        return self.__list.count()

