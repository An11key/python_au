# Array

+ [Max consecutive ones](#max-consecutive-ones)

## Max Consecutive Ones

https://leetcode.com/problems/max-consecutive-ones/

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max1 = 0
        c = 0
        for item in nums:
            if item!=0:
                c+=1
            else:
                if c>max1:
                    max1=c
                c=0
        if c>max1:
            max1=c
        return max1
```