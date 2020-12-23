class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.length = 0
        self.head = None
        self.cur = self.head
        self.index = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.length:
            return -1
        cur = self.head
        while index != 0:
            index -= 1
            cur = cur.next

        return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)
        self.length += 1
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = Node(val)
        self.length += 1
        cur = self.head
        if cur is None:
            self.head = node
            return 0
        while cur.next is not None:
            cur = cur.next
        cur.next = node
        node.prev = cur

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.length:
            return 0
        cur = self.head
        prev = cur
        if index == 0:
            self.addAtHead(val)
        elif self.length == index:

            self.addAtTail(val)
        else:
            while index != 0:
                index -= 1
                prev = cur
                cur = cur.next
            node = Node(val)
            self.length += 1
            node.next = cur
            node.prev = cur.prev
            cur.prev = node
            prev.next = node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < self.length:
            self.length -= 1
            if index == 0:
                self.head = self.head.next
            else:
                cur = self.head
                prev = self.head
                while index != 0:
                    index -= 1
                    prev = cur
                    cur = cur.next
                prev.next = cur.next

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.length:
            self.index+=1
            return self.get(self.index-1)
        else:
            raise StopIteration



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
