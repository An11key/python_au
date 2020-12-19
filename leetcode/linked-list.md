# Linked-list

+ [Linked list cycle](#linked-list-cycle)
+ [Reverse linked list](#reverse-linked-list)
+ [Middle of the linked list](#middle-of-the-linked-list)
+ [Remove nth node from end of list](#remove-nth-node-from-end-of-list)
+ [Linked list cycle ii](#linked-list-cycle-ii)
+ [Merge two sorted lists](#merge-two-sorted-lists)
+ [Palindrome linked list](#palindrome-linked-list)
+ [Reorder list](#reorder-list)
+ [Intersection of two linked lists](#intersection-of-two-linked-lists)
+ [Sort list](#sort-list)

## Linked List Cycle

https://leetcode.com/problems/linked-list-cycle/

```python
class Solution:
    dct = {}
    def find(self, Node):
        if Node.next == None:
            return False
        else:
            if not Node.next in self.dct:
                self.dct[Node.next] = None
                return self.find(Node.next)
                
            else:
                return True
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        return self.find(head)
```

## Reverse Linked List

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

## Middle of the Linked List

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

## Remove Nth Node From End of List

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

## Linked List Cycle II

https://leetcode.com/problems/linked-list-cycle-ii/

```python
class Solution:
    dct = {}
    def find(self, Node):
        if Node.next == None:
            return None
        else:
            if not Node in self.dct:
                self.dct[Node] = None
                return self.find(Node.next)
                
            else:
                return Node
    
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        return self.find(head)
```

## Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/

```python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l=[]
        if not l1 and not l2:
            return l1
        while l1:
            l.append(l1)
            l1=l1.next
        while l2:
            l.append(l2)
            l2=l2.next
        l.sort(key=lambda i:i.val)
        for i in range(1,len(l)):
            l[i-1].next=l[i]
        l[-1].next=None
        return l[0] 
```

## Palindrome Linked List

https://leetcode.com/problems/palindrome-linked-list/

```python
class Solution:
    def deep(self, head) :
        leng = 0
        cur = head
        while cur is not None:
            leng+=1
            cur = cur.next
        leng//=2
        cur = head
        while True:
            if leng == 0:
                return cur
            else:
                cur = cur.next
                leng-=1
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        prev,cur,next = None, head, None
        while cur is not None :
            next = cur.next 
            cur.next = prev
            prev = cur 
            cur = next
        return prev
    def isPalindrome(self, head: ListNode) -> bool:
        head1 = self.reverseList(self.deep(head)) 
        head2 = head
        while head1 is not None:
            if head1.val==head2.val:
                head2 = head2.next
                head1 = head1.next
                continue
            else:
                return False
        return True
```

## Reorder List

https://leetcode.com/problems/reorder-list/

```python
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return head
        arr = []
        while head:
            arr.append(head)
            head = head.next
        
        n = len(arr)

        if n%2 == 0:
            mid = n//2 
        else:
            mid = n//2 + 1
        
        left = arr[:mid]
        right = arr[mid:]
        
        arr[::2] = left
        arr[1::2] = right[::-1]
        
        for i in range(n-1):
            arr[i].next = arr[i+1]
        arr[n-1].next = None
        return arr[0]
```

## Intersection of Two Linked Lists

https://leetcode.com/problems/intersection-of-two-linked-lists/

```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        def get_height(node):
            if not node:
                return 0
            count = 0
            while node:
                count += 1
                node = node.next
            
            return count
        
        
        h_A = get_height(headA)
        h_B = get_height(headB)
            
        currA = headA
        currB = headB
        
        
        if h_A > h_B:
            for _ in range(h_A - h_B):
                currA = currA.next
        elif h_B > h_A:
            for _ in range(h_B - h_A):
                currB = currB.next
        
        
        while currA and currB:
            if currA == currB:
                return currA
            
            if currA.next == currB.next:
                return currA.next
            
            currA = currA.next
            currB = currB.next
        return None
```

## Sort List

https://leetcode.com/problems/sort-list/

```python
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head: 
            return None
        arr = []
        
        p = head
        while p:
            arr.append(p)
            p = p.next
            
        arr.sort(key=lambda x: x.val)
        
        for i in range(1,len(arr)):
            arr[i-1].next = arr[i]
        arr[-1].next = None
        
        return arr[0]
```