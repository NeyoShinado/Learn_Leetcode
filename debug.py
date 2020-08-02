#!usr/bin/python
# **utf-8**

if __name__ == "__main__":
    # input
    s1 = "991086334737101014141447823434124179111084831929311089596731075933473557543639836"
    s2 = "73378335716510109111963597814326771110829569262663543213269127839633"
    n1 = len(s1)
    n2 = len(s2)

    # init
    res = []  # string list for res
    tmp = 0  # cur_val for each bit

    for i in range(n1):
        carry = 0  # carry for each product
        for j in range(n2):
            tmp = int(s1[-i-1]) * int(s2[-j-1])
            # 最高位可能未有进位，不能用
            if len(res) >= i + j + 1:
                tmp += int(res[i + j])
                res[i + j] = str(tmp % 10 + carry)
            else:
                res.insert((i + j), str(tmp % 10 + carry))
            carry = tmp // 10
    if carry != 0:
        if len(res) >= n2 + i + 1:
            res[n2 + i] = str(carry)
        else:
            res.insert((n2 + i), str(carry))

    res = res[::-1]
    res = "".join(res)
    print(len(res))