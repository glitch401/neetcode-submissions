from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_c = Counter(s)
        s_t = Counter(t)
        return True if s_t==s_c else False
