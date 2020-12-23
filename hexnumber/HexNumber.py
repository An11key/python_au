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
            self.index += 1
            return self.get(self.index - 1)
        else:
            raise StopIteration


class hexn:
    def __init__(self, num):
        self.list = MyLinkedList()
        self.num = num
        for i in num:
            if ord(i) > 64:
                self.list.addAtHead(ord(i) - 55)
            else:
                self.list.addAtHead(ord(i) - 48)


def summ(num1, num2):
    if num1.list.get(0) == num2.list.get(0) == 0:
        return hexn('0')
    res = 0
    mn = 1
    for i in range(min(num1.list.length, num2.list.length)):
        # result.list.addAtTail(next(num1.list)+next(num2.list))
        res += mn * (next(num1.list) + next(num2.list))
        mn *= 16
    if num1.list.length > num2.list.length:
        for i in range(num1.list.length - num2.list.length):
            # result.list.addAtTail(next(num1.list))
            res += mn * next(num1.list)
            mn *= 16
    elif num1.list.length < num2.list.length:
        for i in range(num2.list.length - num1.list.length):
            # result.list.addAtTail(next(num2.list))
            res += mn * next(num2.list)
            mn *= 16
    result = hexn(from_10_to_16(res))
    return result


def from_10_to_16(num):
    res = ''

    while (num != 0):
        if num % 16 > 9:
            res += chr(num % 16 + 55)
        else:
            res += chr(num % 16 + 48)

        num //= 16

    return res[::-1]


num1 = hexn('1')
num2 = hexn('43')

res = summ(num1, num2)
print(res.num)
