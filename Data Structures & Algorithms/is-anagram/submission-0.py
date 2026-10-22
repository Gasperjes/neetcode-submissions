class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mydict1 = dict()
        mydict2 = dict()
        for i in range(len(s)):
            mydict1[s[i]] = mydict1.get(s[i],0) + 1
            mydict2[t[i]] = mydict2.get(t[i],0) + 1
        for key in mydict1:
            if mydict1[key] != mydict2.get(key,0):
                return False
        return True


