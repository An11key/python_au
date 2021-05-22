# Graph

+ [Course schedule ii](#course-schedule-ii)

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