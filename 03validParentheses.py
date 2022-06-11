class Solution:
    def isValid(self, s: str) -> bool:
        # print(s[0:4])
        # s = s.replace(')', '(').replace(']', '[').replace('}', '{')

        # for i in range(0, len(s), 2):
        #     if s[:i] != s[:i+1]:
        #         return False
        #     elif s[:i] == s[:i+1]:
        #         return True
        dic = {'(': ')', '[': ']', '{': '}'}
        res = []
        for c in s:
            print(c, end = ' ')
            if c in dic:
                res.append(c)
                print(res)
            else:
                if(len(res) and dic[res[-1]] == c):
                    del res[-1]
                else:
                    return False
        return res == []111


s = Solution()
print(s.isValid('([])'))
