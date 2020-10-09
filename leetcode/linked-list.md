#Linked-list

+[Reverse linked list](#reverse-linked-list)
+[Middle of the linked list](#middle-of-the-linked-list)
+[Remove nth node from end of list](#remove-nth-node-from-end-of-list)

##Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/

```python
class Solution:
    
    def deep(self, Node, prev):
        if Node.next==None:
            Node.next = prev
            return Node
        else:
            temp = Node.next
            Node.next = prev
            return self.deep(temp, Node)
            if Node.next == None:
                return Node
            
        
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        return self.deep(head,None)
```



##Middle of the Linked List

https://leetcode.com/problems/middle-of-the-linked-list/

```python
class Solution:
    leng = 1
    
    def find_middle(self, Node):
        if(Node.next == None):
            self.leng//=2
            print(self.leng)
        else:
            self.leng += 1
            self.find_middle(Node.next)
    def inputa(self, Node):
        if self.leng == 0:
            return Node
        else:
            self.leng-=1
            return self.inputa(Node.next)
    
    def middleNode(self, head: ListNode) -> ListNode:
        
        self.find_middle(head)
        return self.inputa(head)
```



##Remove Nth Node From End of List

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

```python
class Solution:
    i = 0
    def dele(self,Node,ind):
        
        if Node is None:
            self.i = ind
        else:
            self.dele(Node.next,ind)
            if self.i != 0:
                self.i-=1
            else:
                Node.next = Node.next.next
                self.i-=1
    
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next is None:
            return None
        self.dele(head,n)
        if self.i == 0:
            head = head.next
        return head
```

