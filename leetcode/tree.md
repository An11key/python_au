# Tree

+ [Maximum depth of binary tree](#maximum-depth-of-binary-tree)
+ [Binary tree inorder traversal](#binary-tree-inorder-traversal)
+ [Invert binary tree](#invert-binary-tree)
+ [Binary search tree iterator](#binary-search-tree-iterator)
+ [Binary tree level order traversal](#binary-tree-level-order-traversal)
+ [Kth smallest element in a bst](#kth-smallest-element-in-a-bst)
+ [Validate binary search tree](#validate-binary-search-tree)
+ [Symmetric tree](#symmetric-tree)

## Maximum Depth of Binary Tree

https://leetcode.com/problems/maximum-depth-of-binary-tree/

```python
class Solution:
    
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        visited = []
        leng = []
        def dfs(root,l):
            visited.append(root)
            if root.left and root.left not in visited:
                dfs(root.left,l+1) 
            if root.right and root.right not in visited:
                dfs(root.right,l+1)
            leng.append(l+1)
        
        
        dfs(root,0)
        return max(leng)
```

## Binary Tree Inorder Traversal

https://leetcode.com/problems/binary-tree-inorder-traversal/

```python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        visited = []
        
        def dfs(root):
            if root:
                dfs(root.left)
                visited.append(root.val)
                dfs(root.right)
        dfs(root)
        return visited
```

## Invert Binary Tree

https://leetcode.com/problems/invert-binary-tree/

```python
class Solution:
    
    def switch(self,root):
        if root.left or root.right:
            print(root.val)
            temp = root.left
            root.left = root.right
            root.right = temp
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if root:
                self.switch(root)
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        return root
```

## Binary Search Tree Iterator

https://leetcode.com/problems/binary-search-tree-iterator/

```python
class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self.cur = root
        
    def next(self):
        while self.curr:
            self.stack.append(self.curr)
            self.cur = self.curr.left
        self.cur = self.stack.pop()
        out = self.cur.val
        self.cur = self.cur.right
        return out

    def hasNext(self):
        return self.stack or self.cur
```

## Binary Tree Level Order Traversal

https://leetcode.com/problems/binary-tree-level-order-traversal/

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return None
        print(root)
        queue = [root]
        res = [[root.val]]
        
        while queue:
            temp = []
            leng = len(queue)
            for i in range (leng):
                cur = queue.pop()
                if cur.left:
                    queue.insert(0,cur.left)
                    temp.append(cur.left.val)
                if cur.right:
                    queue.insert(0,cur.right)
                    temp.append(cur.right.val)
            if temp:
                print(temp)
                res.append(temp)
        return res
```

## Kth Smallest Element in a BST

https://leetcode.com/problems/kth-smallest-element-in-a-bst/

```python
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res = []
        def dfs(root):
            if(root):
                res.append(root.val)
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        res.sort()
        return res[k-1]
```

## Validate Binary Search Tree

https://leetcode.com/problems/validate-binary-search-tree/

```python
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        check = []
        interval=[]
        
        def isval(root, interv):
            if root.left:
                if root.left.val>=root.val or root.left.val<=interv:
                    check.append(1)
            if root.right:
                if root.right.val<=root.val or root.right.val>=interv:
                    check.append(1)
                    
        
        def dfs(root):
            if root:
                dfs(root.left)
                dfs(root.right)
                isval(root)
            
        dfs(root)
        if 1 in check :
            return False
        else:
            return True
```

## Symmetric Tree

https://leetcode.com/problems/symmetric-tree/

```python
class Solution:
    
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)


    def isMirror(self, root1, root2):
        if root1 is None and root2 is None:
            return True

        if root1 is not None and root2 is not None:
            if root1.val == root2.val:
                return (self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left))
```