class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = defaultdict(list)
        for i in strs:
            arr = [0]*26
            for j in i:
                arr[ord(j)-ord("a")] += 1

            key = tuple(arr)
            mydict[key].append(i)
        return list(mydict.values())
        