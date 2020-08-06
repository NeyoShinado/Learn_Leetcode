#! usr/etc/bin python
#coding: utf-8
import math
class Solution:
    def killMonster(self):
        # input
        HP = int(input())
        NA = int(input())
        BA = int(input())

        # init
        cnt = 0
        if BA <= 2 * NA:
            cnt = math.ceil(HP / NA)
        else:
            while HP > 0:
                if HP >= BA:
                    HP -= BA
                    cnt += 2
                elif HP < BA and HP > NA:
                    HP -= BA
                    cnt += 2
                else:
                    HP -= NA
                    cnt += 1
        print(cnt)


if __name__ == "__main__":
    t = Solution()
    t.killMonster()