class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        str_one = {}
        str_two = {}
        for i in range(len(s)):
            if s[i] not in str_one:
                str_one[s[i]] = 0
            str_one[s[i]] += 1
            if t[i] not in str_two:
                str_two[t[i]] = 0
            str_two[t[i]] += 1
        str_one = dict(sorted(str_one.items()))
        str_two = dict(sorted(str_two.items()))

        for char in str_one:
            if char not in str_two:
                return False
            elif str_one[char] != str_two[char]:
                return False
        return True









