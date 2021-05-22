# Graph

+ [Course schedule ii](#course-schedule-ii)
+ [Course schedule](#course-schedule)
+ [Number of islands](#number-of-islands)
+ [Is graph bipartite?](#is-graph-bipartite?)
+ [Cheapest flights within k stops](#cheapest-flights-within-k-stops)
+ [Shortest path in binary matrix](#shortest-path-in-binary-matrix)
+ [Maximum depth of n-ary tree](#maximum-depth-of-n-ary-tree)
+ [Min stack](#min-stack)
+ [Implement queue using stacks](#implement-queue-using-stacks)
+ [Implement stack using queues](#implement-stack-using-queues)
+ [House robber ii](#house-robber-ii)

## Course Schedule II

https://leetcode.com/problems/course-schedule-ii/

```python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for i, j in prerequisites:
            graph[j].append(i)
            indegree[i] += 1 
            
        queue = deque(i for i in range(numCourses) if indegree[i] == 0)
        courses = []
        while queue:
            course = queue.popleft()
            courses.append(course)
            for i in graph[course]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        return courses * (len(courses) == numCourses)
```

## Course Schedule

https://leetcode.com/problems/course-schedule/

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not numCourses or not prerequisites: return True
        graph = {}
        for pair in prerequisites:
            _from, _to = pair
            graph.setdefault(_from, []).append(_to)
        visiting, visited = set(), set()
        def dfs(node):
            if node in visiting: return False
            visiting.add(node)
            res = True
            for child in graph.get(node, []):
                if child not in visited:
                    res &= dfs(child)
                    if not res: return False
            visiting.discard(node)
            visited.add(node)
            return res
        for i in range(numCourses):
            if not dfs(i): return False
        return True
```

## Number of Islands

https://leetcode.com/problems/number-of-islands/

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        def dfs(i,j):
            
            grid[i][j]="0"
            
            for nr,nc in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                
                if 0<=nr<m and 0<=nc<n and grid[nr][nc]=="1":
                    dfs(nr,nc)
        
        count = 0
        
        for i in range(m):
            for j in range(n):
                
                if grid[i][j]=="1":
                    count+=1
                    dfs(i,j)
        
        return count
```

## Is Graph Bipartite?

https://leetcode.com/problems/is-graph-bipartite/

```python
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(graph, val, side):
            ans = True
            bi[val] = side
            new_side = 1 if not side else 0
            for ind in graph[val]:
                ans = ans and (dfs(graph, ind, new_side) if bi[ind] is None else False if bi[ind] != new_side else True)
            return ans
        
        
        bi = [None for val in range(len(graph))]
        ans = True
        for val in range(len(graph)):
            if bi[val] is None:
                ans = ans and dfs(graph, val, 0)
        return ans
```

## Cheapest Flights Within K Stops

https://leetcode.com/problems/cheapest-flights-within-k-stops/

```python
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u,v,cost in flights:
            graph[u].append([v,cost])
        
        visited = {src:0}
        min_cost = sys.maxsize
        queue = []
        queue.append([src,0,k])
        
        while queue:
            len1 = len(queue)    
            for i in range(len1):
                node,node_cost,k_val = queue.pop(0)
                if node == dst and k_val >= -1:
                    min_cost = min(min_cost,node_cost)
                
                for neigh,cost in graph[node]:
                    if neigh not in visited or cost+node_cost<visited[neigh]:
                        queue.append([neigh,cost+node_cost,k_val-1])
                        visited[neigh] = cost+node_cost
        if min_cost == sys.maxsize:
            return -1
        return min_cost
```

## Shortest Path in Binary Matrix

https://leetcode.com/problems/shortest-path-in-binary-matrix/

```python
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        if grid[0][0] == 1:
            return -1
        q = [(0, 0, 1)]
        while len(q) > 0:
            x, y, d = q.pop(0)
            if x == rows-1 and y == cols-1:
                return d
            for a, b in ((x-1, y-1), (x+1, y+1), (x-1, y), (x+1, y), (x, y-1), (x, y+1), (x-1, y+1), (x+1, y-1)):
                if 0 <= a < rows and 0 <= b < cols and grid[a][b] == 0:
                    grid[a][b] = 1
                    q.append((a, b, d+1))

        return -1
```

## Maximum Depth of N-ary Tree

https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

```python
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        if not root.children: return 1
        return max(self.maxDepth(i)+1 for i in root.children)
```

## Min Stack

https://leetcode.com/problems/min-stack/

```python
class MinStack:
    val=[] 

    def __init__(self):
        self.val.clear()
    def push(self, x: int) -> None:
        self.val.append(x)
        

    def pop(self) -> None:
        self.val.pop()

    def top(self) -> int:
        return self.val[-1]

    def getMin(self) -> int:
        return min(self.val)
```

## Implement Queue using Stacks

https://leetcode.com/problems/implement-queue-using-stacks/

```python
class MyQueue:

    def __init__(self):
        self.arr=[]
        

    def push(self, x: int) -> None:
        self.arr.append(x)
        

    def pop(self) -> int:
        if len(self.arr)>0:
            x=self.arr[0]
            self.arr.remove(self.arr[0])
            return x
        
        

    def peek(self) -> int:
        if len(self.arr)>0:
            return self.arr[0]
        
        

    def empty(self) -> bool:
        if len(self.arr)>0:
            return False
        return True
```

## Implement Stack using Queues

https://leetcode.com/problems/implement-stack-using-queues/

```python
class MyStack:

    def __init__(self):
        self.arr=[]
        

    def push(self, x: int) -> None:
        self.arr.append(x)
        

    def pop(self) -> int:
        if len(self.arr)>0:
            return self.arr.pop()

    def top(self) -> int:
        if len(self.arr)>0:
            return self.arr[-1]
        

    def empty(self) -> bool:
        if len(self.arr)>0:
            return False
        return True
```

## House Robber II

https://leetcode.com/problems/house-robber-ii/

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) <= 3:
            return max(nums)
        
        def helper(dp):
            dp[1] = max(dp[0], dp[1])

            for i in range(2, len(dp)):
                dp[i] = max(dp[i - 1], dp[i] + dp[i - 2])

            return dp[-1]
        
        p1 = helper(nums[:len(nums) - 1])
        p2 = helper(nums[1:])
        return max(p1, p2)
```