#! usr/etc/bin python
#coding: utf-8

class Solution:
    def leftHun(self):
        # input
        Nbear, Nsug = list(map(int, input().split(" ")))
        sugar = list(map(int, input().split(" ")))
        bears = []
        for i in Nbear:
            bears.append(list(map(int, input().split(" "))))

        bearFig, bearHun = zip(*bears)

        # sort
        bearFig.sort()
        bearFig[::-1]
        sugar.sort()
        sugar[::-1]

        # Eat
        for i in range(Nbear):
            while bear


if __name__ == "__main__":
    t = Solution()
    t.leftHun()