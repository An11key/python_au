#Intervals

+[Non-overlapping Intervals](#non-overlapping-intervals)

##Non-overlapping Intervals

https://leetcode.com/problems/non-overlapping-intervals/

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