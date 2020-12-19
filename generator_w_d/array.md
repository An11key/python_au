# Array

+ [Reshape the matrix](#reshape-the-matrix)

## Reshape the Matrix

https://leetcode.com/problems/reshape-the-matrix/

```python
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        length = len(nums)*len(nums[0])
        temp = []
        if(length != r*c):
            return nums
        else:
            for i in range (len(nums)):
                for items in nums[i]:
                    temp.append(items)
            nums = []
            for i in range (r):
                t = []
                for j in range (c):
                    t.append(temp[i*c + j])
                nums.append(t)
            return (nums)
```