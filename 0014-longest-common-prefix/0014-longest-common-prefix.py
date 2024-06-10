class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        print(strs)
        mini,maxi=min(strs),max(strs)
        print(mini)
        for i in range(len(mini)):
            if mini[i]!=maxi[i]:
                return mini[:i]
        return mini