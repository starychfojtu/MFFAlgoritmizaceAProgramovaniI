class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.__head = None
        self.__count = 0

    def prepend(self, value):
        """
        Inserts a new value as the first item in the list. Runs in O(1).
        """
        node = Node(value, self.__head)
        self.__head = node
        self.__count += 1

    def append(self, value):
        """
        Appends a new value at the end of the list. Runs in O(n) (Bonus points for O(1)).
        """
        node = Node(value, None)

        if self.__head is None:
            self.__head = node
        else:
            lastNode = self.__head
            while lastNode.next is not None:
                lastNode = lastNode.next

            lastNode.next = node

        self.__count += 1

    def clear(self):
        """
        Clears the whole list. Runs in O(1).
        """
        self.__head = None
        self.__count = 0

    def count(self):
        """
        Returns count of the items in the list. Runs in O(1).
        """
        return self.__count

    def find(self, value):
        """
        Returns a first ```Node``` with specified ```value``` or None if there is no such node. Runs in O(n).
        This is the only function which exposes ```Node```.
        """
        node = self.__head
        while node is not None and node.value != value:
            node = node.next

        return node

    def insert(self, value, after):
        """
        Inserts ```value``` right after the first occurance of ```after```. Throws exception if not exists. Runs in O(n).
        """
        node = self.find(after)
        assert node is not None, "Given value is not present."

        newNode = Node(value, node.next)
        node.next = newNode
        self.__count += 1

    def pop(self):
        """
        Removes the first value and returns it. Throws if empty. Runs in O(1).
        """
        assert self.__head is not None
       
        value = self.__head.value
        self.__head = self.__head.next
        self.__count -= 1
        return value

    def remove(self, value):
        """
        Removes first occurance of value. Does nothing if not present. Runs in O(n).
        """
        if self.__head is None:
            return

        if self.__head.value == value:
            self.__head = self.__head.next
            self.__count -= 1
        else:
            nodeBefore = self.__head
            while nodeBefore.next is not None and nodeBefore.next.value != value:
                nodeBefore = nodeBefore.next

            if nodeBefore.next is not None:
                nodeBefore.next = nodeBefore.next.next
                self.__count -= 1

    def to_list(self):
        """
        Returns list equivalent of LinkedList. Runs in O(n).
        """
        result = []
        node = self.__head
        while node is not None:
            result.append(node.value)
            node = node.next

        return result