# первое решение
class Solution:
    vowels = frozenset({'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'})
    def halvesAreAlike(self, s: str) -> bool:
        mid = len(s) // 2
        count = sum(s[idx] in self.vowels for idx in range(mid))
        count -= sum(s[idx] in self.vowels for idx in range(mid, len(s)))   
        return not count
    
# второе решение
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        v='aeiou'
        x = int(len(s)/2)
        a = s[0:x]
        b = s[x:]
        aa, bb = 0,0
        for i,j in zip(a,b):
            if i in v:
                aa += 1
            if j in v:
                bb += 1
        if aa == bb:
            return True
        else:
            return False 
