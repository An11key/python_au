# Math

+ [Reverse integer](#reverse-integer)
+ [Palindrome number](#palindrome-number)
+ [Fizz buzz](#fizz-buzz)
+ [Base 7](#base-7)
+ [Fibonacci number](#fibonacci-number)
+ [Largest perimeter triangle](#largest-perimeter-triangle)
+ [Sqrt(x)](#sqrt(x))

## Reverse Integer

https://leetcode.com/problems/reverse-integer/

```python
class Solution:
    def reverse(self, x: int) -> int:
        flag = 1
        if(x<0):
            flag=-1
            x=-x
        x = int(str(x)[::-1])
        if x>2**31:
            return 0
        return flag*x
```

## Palindrome Number

https://leetcode.com/problems/palindrome-number/

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)[::-1]==str(x)
```

## Fizz Buzz

https://leetcode.com/problems/fizz-buzz/

```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ar = [0]*n
        for i in range (1,n+1):
            if i%15==0:
                ar[i-1]="FizzBuzz"
                continue
            if i%3==0:
                ar[i-1]="Fizz"
                continue
            if i%5==0:
                ar[i-1]="Buzz"
                continue
            ar[i-1]=str(i)
        return ar
```

## Base 7

https://leetcode.com/problems/base-7/submissions/

```python
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0:
            return '0'
        st = ''
        flag=''
        if num<0:
            num=-num
            flag='-'
        while num!=0:
            st+=str(num%7)
            num//=7
        return flag+st[::-1]
```

## Fibonacci Number

https://leetcode.com/problems/fibonacci-number/submissions/

```python
class Solution:
    def fib(self, N: int) -> int:
        if N==0:
            return 0
        
        f0 = 0
        f1 = 1
        for i in range (N-1):
            temp=f1
            f1+=f0
            f0=temp
        return f1
```

## Largest Perimeter Triangle

https://leetcode.com/problems/largest-perimeter-triangle/submissions/

```python
class Solution:
    def check(self,a,b,c):
        return a<c+b
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort();
        i = len(A)-1
        while True:
            if self.check(A[i],A[i-1],A[i-2]):
                return A[i]+A[i-1]+A[i-2]
            i-=1
            if i<2:
                break
        return 0
```

## Sqrt(x)

https://leetcode.com/problems/sqrtx/

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        return math.floor(sqrt(x))
```