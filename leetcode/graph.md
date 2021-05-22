# Graph

+ [Course schedule ii](#course-schedule-ii)
+ [Course schedule](#course-schedule)

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