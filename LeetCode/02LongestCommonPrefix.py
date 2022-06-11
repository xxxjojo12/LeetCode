class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs: return ''
        m, M, i = min(strs), max(strs), 0
        print(m, M)

        for i in range(min(len(m), len(M))):
            if m[i] != M[i]:
                break
        else:
            i += 1
        return m[:i]

s = Solution()
print(s.longestCommonPrefix(['slr', 'slar', 'slaaa', 'slxxhhh']))