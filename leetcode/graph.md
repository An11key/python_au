# Graph

+ [Course schedule ii](#course-schedule-ii)
+ [Course schedule](#course-schedule)
+ [Number of islands](#number-of-islands)

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