
"""
题目 三、 字符串的排列

给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例1:

输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").


示例2:

输入: s1= "ab" s2 = "eidboaoo"
输出: False


注意：

输入的字符串只包含小写字母
两个字符串的长度都在 [1, 10,000] 之间
"""

# 方式一：最优方式
"""
执行用时：44 ms
"""
from collections import Counter
def checkInclusion(s1 ,s2):
    """
    :param s1:
    :param s2:
    :return:
    :解题思路：input字符a-z，因此用字典存储a-z的26个字符，其对应值为对应字幕出现的次数。最终比较
    """
    if len(s2) < len(s1): # 判断s2_length < s1_length，则s2不含有字串对应s1
        return False
    # Counter. 字典的子类，提供了可哈希对象的计数功能
    cnt1 = Counter(s1)              # cnt1存储：s1中字符，以及对应出现的次数
    num = len(s1)
    left ,right = 0 ,num -1            # s2滑动窗口左右指针
    cnt2 = Counter(s2[left:right])  # cnt2存储：s2滑动窗口中字符，以及对应出现次数
    while right < len(s2):          # 当滑动窗口 右指针 < len(s2)
        cnt2[s2[right]] += 1        # 右侧指针继续右滑
        if cnt2==cnt1:
            return True
        # cnt2 不等于 cnt1,窗口右滑，删除最左边元素，字母次数-1=0，然后直接删除

        cnt2[s2[left]] -= 1         # 每次增加窗口最右边的元素，删除最左边的元素。
        # cnt2中对应s2[left]的字符，次数-1，若-1后==0，则手动删除，left指针向右移动即可。
        if cnt2[s2[left]] == 0:
            del cnt2[s2[left]]      # 删除最左边元素
        left  += 1
        right += 1
    return False



"""

步骤说明：
使用和s1等长的滑动窗口判断s2在这个窗口内的字符出现个数和s1的字符出现个数是否相等。

使用的是一个字典，统计次数就行，比较简单。第一遍的时候是每次切片都去使用Counter，这样的话超时了。所以改用了每次增加窗口最右边的元素，删除最左边的元素，如果左边的元素次数已经为0了，需要手动删除这个元素，否则影响字典相等的判断。

时间复杂度为O(N)，空间复杂度O(1)。N为s2长度，假设判断两个字典是否相等的时间复杂度是O(1).

参考链接：https://blog.csdn.net/fuxuemingzhu/article/details/82876662
"""

# 方式二：滑动窗口优化方案
"""
思路：
1. 用cnt存储s1与s2相同的字母数量
2. 滑动窗口大小不变，每向右滑动增加一个字母，判断cnt与len(c1)是否相等。
"""
import collections
def checkInclusion_1(self, s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    l1, l2 = len(s1), len(s2)
    c1 = collections.Counter(s1)
    c2 = collections.Counter()
    cnt = 0
    p = q = 0
    while q < l2:
        c2[s2[q]] += 1
        if c1[s2[q]] == c2[s2[q]]:
            cnt += 1
        if cnt == len(c1):
            return True
        q += 1
        if q - p + 1 > l1:
            if c1[s2[p]] == c2[s2[p]]:
                cnt -= 1
            c2[s2[p]] -= 1
            if c2[s2[p]] == 0:
                del c2[s2[p]]
            p += 1
    return False
"""
执行用时：52 ms
"""

def main():
    s1 = 'ab'
    s2 = 'eidboaoo'
    print(checkInclusion(s1,s2))


if __name__ == '__main__':
    main()