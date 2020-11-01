# String

+ [Valid anagram](#valid-anagram)

## Valid Anagram

https://leetcode.com/problems/valid-anagram/submissions/

```python
class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s, key=lambda x: x.lower())==sorted(t,key=lambda x:x.lower())
```