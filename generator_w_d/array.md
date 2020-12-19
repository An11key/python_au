# Array

+ [Reshape the matrix](#reshape-the-matrix)
+ [Flipping an image](#flipping-an-image)
+ [Transpose matrix](#transpose-matrix)

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

## Flipping an Image

https://leetcode.com/problems/flipping-an-image/

```python
class Solution:
    def flip(self,l):
        for i in range(len(l)//2):
            temp = l[i]
            l[i] = l[-i-1]
            l[-i-1] = temp
    def invert(self,l):
        for i in range(len(l)):
            for j in range(len(l[0])):
                l[i][j] = (l[i][j]-1)*(-1)
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range (len(A)):
            self.flip(A[i])
        self.invert(A)
        return A
```

## Transpose Matrix

https://leetcode.com/problems/transpose-matrix/

```python
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        
        if len(A) != len(A[0]):
            if len(A) < len(A[0]):
                for i in range (len(A[0])-len(A)):
                    A.append(['-1']*len(A[0]))
            elif len(A) > len(A[0]):
                for i in range (len(A)):
                    for j in range (len(A)-len(A[i])):
                        A[i].append('-1')
        for i in range (len(A)):
            for j in range (i):
                temp = A[i][j]
                A[i][j] = A[j][i]
                A[j][i]=temp
        for i in range (len(A)):
            while True:
                try:
                    A[i].remove('-1')
                except:
                    break
        while True:
                try:
                    A.remove([])
                except:
                    break
        return A
```