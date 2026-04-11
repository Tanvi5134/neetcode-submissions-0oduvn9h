class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        res = defaultdict(list)

        for s in strs:
            st = sorted(s)
            key = "".join(st)
            res[key].append(s)
        return list(res.values())