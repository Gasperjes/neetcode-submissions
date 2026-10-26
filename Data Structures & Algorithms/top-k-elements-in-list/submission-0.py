class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = defaultdict(int)
        for i in nums:
            mydict[i] += 1
        x = mydict.items()
        sortedx = sorted(x, key=lambda x: x[1], reverse=True)

        return [item[0] for item in sortedx[:k]]        