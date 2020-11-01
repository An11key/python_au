# String

+ [Valid anagram](#valid-anagram)
+ [Reverse string](#reverse-string)

## Valid Anagram

https://leetcode.com/problems/valid-anagram/submissions/

```python
class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s, key=lambda x: x.lower())==sorted(t,key=lambda x:x.lower())
```

## Reverse String

https://leetcode.com/problems/reverse-string/

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s = s.reverse()
```