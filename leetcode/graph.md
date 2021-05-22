# Graph

+ [Course schedule ii](#course-schedule-ii)
+ [Course schedule](#course-schedule)
+ [Number of islands](#number-of-islands)
+ [Is graph bipartite?](#is-graph-bipartite?)
+ [Cheapest flights within k stops](#cheapest-flights-within-k-stops)

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