#Intervals

+[Non-overlapping intervals](#non-overlapping-intervals)
+[Merge intervals](#merge-intervals)
+[Insert interval](#insert-interval)

##Non-overlapping Intervals
##Merge Intervals
##Insert Interval

https://leetcode.com/problems/non-overlapping-intervals/
https://leetcode.com/problems/merge-intervals/
https://leetcode.com/problems/insert-interval/

```python
class Solution:
    def find(self,l1,l2):
        if l2[0]<=l1[0]<l2[1] or l2[0]<l1[1]<=l2[1] or l1[0]<=l2[0]<l1[1] or l1[0]<l2[1]<=l1[1]:
            return 1
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        if len(intervals)<=1:
            return count
        temp = intervals[-1]
        intervals.sort(key = lambda x: x[1])
        i = 1
        while True:
            if self.find(intervals[i-1],intervals[i]) == 1:
                
                count+=1
                del intervals[i]
                i-=1
            i+=1
            if i==len(intervals):
               break 
        return count
```

```python
class Solution:
    def find(self,l1,l2):
        if l1[0]<=l2[0]<=l1[1] or l1[0]<=l2[1]<=l1[1] or l2[0]<=l1[0]<=l2[1] or l2[0]<=l1[1]<=l2[1]:
            return True
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        i = 1
        if len(intervals)==1 or len(intervals)==0:
            return intervals
        intervals.sort(key = lambda x: x[0])
        while True:
            
            if self.find(intervals[i-1],intervals[i]):
                print(1)
                temp = [min(intervals[i-1][0],intervals[i][0]),max(intervals[i-1][1],intervals[i][1])]
                del intervals[i-1]
                del intervals[i-1]
                
            
                intervals.insert(i-1,temp)
                i-=1
            i+=1
            if i>=len(intervals):
                break
            
        return intervals
```

```python
class Solution:
    def find(self,l1,l2):
        if l1[0]<=l2[0]<=l1[1] or l1[0]<=l2[1]<=l1[1] or l2[0]<=l1[0]<=l2[1] or l2[0]<=l1[1]<=l2[1]:
            return True
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        i = 1
        if len(intervals)==1 or len(intervals)==0:
            return intervals
        intervals.sort(key = lambda x: x[0])
        while True:
            
            if self.find(intervals[i-1],intervals[i]):
                print(1)
                temp = [min(intervals[i-1][0],intervals[i][0]),max(intervals[i-1][1],intervals[i][1])]
                del intervals[i-1]
                del intervals[i-1]
                
            
                intervals.insert(i-1,temp)
                i-=1
            i+=1
            if i>=len(intervals):
                break
            
        return intervals
```
