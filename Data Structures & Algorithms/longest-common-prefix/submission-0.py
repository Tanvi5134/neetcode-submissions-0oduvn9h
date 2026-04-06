class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        f= strs[0]
        l= strs[-1]
        ans = ""
        for i in range (len(f)):
            if f[i] != l[i]:
                return ans
            ans += f[i]

        return ans
       