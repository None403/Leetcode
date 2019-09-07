
"""
leetcode中python提交代码格式：
class Solution(object):

    def function_name(self,s):
        res = ""
        if len(s) == 0:
            return ""
        for each in zip(*s):#zip()函数用于将可迭代对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
            if len(set(each)) == 1:#利用集合创建一个无序不重复元素集
                res += each[0]
            else:
                return res
        return res

"""

"""
题目 一、：无重复字符的最长子串 https://leetcode-cn.com/explore/interview/card/bytedance/242/string/1012/
示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

"""

def lengthOfLongestSubstring(s):
    """
    :param s:
    :return: 无重复最长子串
    :解体方法：滑动窗口
    """
    last = {}
    left, ans = 0, 0
    for i in range(len(s)):
        if s[i] in last and last[s[i]] >= left:
            left = last[s[i]] + 1
        last[s[i]] = i
        ans = max(ans, i - left + 1)
    return ans



def main():
    s1 = input('输入任意字符串')
    lengthOfLongestSubstring(s1)


if __name__ == '__main__':
    main()



