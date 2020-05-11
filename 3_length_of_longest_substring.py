'''
#!/usr/bin/python
#Version1
import pandas as pd
import numpy as np


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        loc_dict = {}    # location of rep_chars
        max_repnum = 0    # nrow of dist df
        dist = pd.DataFrame()

        rep_chars = set(s)
        for char in rep_chars:
            loc_dict[char] = [i for i,v in enumerate(s) if v == char]
            if len(loc_dict[char]) > max_repnum:
                max_repnum = len(loc_dict[char])


        for char in rep_chars:
            dist[char] = rep_chars_dist(loc_dict[char], max_repnum)
            

        dist_vec = dist.values.reshape((1, -1))
        sort_dist = np.sort(dist_vec * -1)[0]    # from largest to smallest
        rank_id = np.argsort(dist_vec * -1)[0]

        ## filter interval from largest to smallest
        rep_chars_list = list(rep_chars)
        if list(rep_chars.difference(set(char))):
            for i in range(len(sort_dist)):
                max_interval = sort_dist[i] * -1#*
                id = rank_id[i]
                char = rep_chars_list[id // max_repnum - 1]
                #! there may be repeat char_id(same dist), should clean the dist df if it's unfit
                print(which(list(np.array(dist[char]) == (sort_dist[i] * -1))), "\n")
                char_id = which(list(np.array(dist[char]) == (sort_dist[i] * -1)))[0]

                #! be aware of no repeat char situation
                for cmp_char in list(rep_chars.difference(set(char))):    # traverse other chars to find out where is a qualifid substring
                    if len(which(list(np.array(dist[cmp_char]) > dist[char][char_id]) and list(np.array(dist[cmp_char]) < dist[char][char_id + 1]))) < 2:
                        flag = True
                        continue
                    else:
                        flag = False
                        # clean the repeat unfit len
                        dist[char][char_id] = 0
                        break

                if flag:
                    break
        else:
            max_interval = 1

        return max_interval


def rep_chars_dist(loc_dict, maxnum):
    # loc_dict: list element of loc_dict
    dist = [0] * (maxnum - 1)
    N = len(loc_dict)
    for i in range(1, N):
        dist[i - 1] = loc_dict[i] - loc_dict[i - 1]


    return dist


def which(lst):
    return list(np.where(lst)[0])
'''


'''
# 滑动窗口方法，动态规划
#Version 2
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Hash set to record the specific chars of window
        occ = set()
        n = len(s)
        id_r, ans = -1, 0
        for id_l in range(n):
            # 左指针右移一格，集合移除一个字符
            if id_l != 0:
                occ.remove(s[i - 1])
            while id_r + 1 < n and s[id_r + 1] not in occ:
                # 右指针右移一格，集合添加一个无重复字符
                occ.add(s[id_r + 1])
                id_r += 1
            ans = max(ans, id_r - id_l + 1)
        return ans
'''


#Version 3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        id_l, res, c_dict = -1, 0, {}
        for id_r, c in enumerate(s):
            #！
            if c in c_dict and c_dict[c] > id_l:
                id_l = c_dict[c]
                c_dict[c] = id_r
            else:
                c_dict[c] = id_r
                res = max(res, id_r - id_l)
        return res


'''
Summary
方法一 先找出重复字符的索引，计算所有子字符串的长度，再进行排序筛选
筛选的条件是：①子字符串中没有其他重复字符则选用；②否则剔除
冗余度较高，要遍历多次；

方法二（Hash Set） 滑动窗口的动态规划方法，使用窗口右边界递增的规律遍历一次即可；
且动态过程中窗口内的字符可缓存给下一个窗口使用；

方法三（Hash Dict） 结合了前两者的特点，使用滑动窗口右界遍历的同时，还
用到子字符串中无重复字符的特点，左边界更新得更快些
'''