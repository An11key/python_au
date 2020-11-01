# String

+ [Valid anagram](#valid-anagram)
+ [Reverse string](#reverse-string)
+ [Reverse vowels of a string](#reverse-vowels-of-a-string)

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

## Reverse Vowels of a String

https://leetcode.com/problems/reverse-vowels-of-a-string/

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        c = []
        for i in s:
            if i in 'aeiouAEIUO':
                c.append(i)
        c.reverse()
        j = 0
        d = []
        print(len(s))
        for i in range (len(s)):
            if s[i] in 'aeiouAEIUO':
                d.append(c[j])
                j+=1
                continue 
            d.append(s[i])
        return ''.join(d)
```