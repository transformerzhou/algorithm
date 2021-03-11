class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, ans = -1,0
        dic = {}
        for j in range(len(s)):
            if s[j] in dic:
                #更新左窗口
                i = max(dic[s[j]], i)
            ans = max(ans, j-i)
            dic[s[j]] = j
        return ans

s = Solution()
s.lengthOfLongestSubstring("abba")

from ltp import LTP

LTP()
