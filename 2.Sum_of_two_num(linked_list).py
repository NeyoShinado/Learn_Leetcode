# 链表：每个节点包括内容和指针，线性地连接起来，分为单链表和双链表。在内存上可以不连续。
# 与数组比较：
#   @劣势
#   1.多了指针的信息，空间利用率低；
#   2.数组访问查找速度更快，可随机访问，因为数组在内存上连续，加上偏移地址即可；
#   @优势
#   1.链表插入删除操作复杂度为O(1)，只需改变指针；而数组要改变元素的内存地址；
#   2.链表可以使用分散的内存空间，避免内存不足的问题；
#   3.大小可变，适合动态存储。


#version 1
# Definition
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def addTwoNumbers(self, l1:listNode, l2:listNode) -> ListNode:  # 类型定义
		head = ListNode(0)  #* 初始化预结点作为链表的头结点，无存储，这样指针移动时也不会丢失链表表头
		node = head         # 初始化链表结点（作为指针移动）
		carry = .0          # 初始化进位
		while l1 or l2:     #* 循环到输入链表都为NULL结点(末尾)
			x = l1.val if l1 else 0 #* 选择条件赋值语句
			y = l2.val if l2 else 0
			sum = x + y + carry # 逐位求和
			carry = sum // 10   # 整除求进位
			node.next = ListNode(int(sum % 10)) # 取余求本位数值，更新结点，且注意数据类型
			if l1:              # 未到末尾保持更新下一位
				l1 = l1.next    
			if l2:
				l2 = l2.next
			node = node.next    # 更新指针
		if carry != 0:          #* 验证最后一位是否需要进一
			node.next = ListNode(1)
		return head.next        #* 从链表真正开始的结点返回

# version2
class Solution:
    def addTwoNumbers(self, l1, l2):
        res = ListNode(0);	# 预结点
        resTemp = resTemp 	# 指针
        flag = 0
        nextSum = 0
        while l1 != None and l2 != None:
            if flag == 0:
                p = l1.val + l2.val
                res.val = p % 10
                nextSum = int(p / 10)
                flag += 1
            else:
                p = l1.val + l2.val + nextSum
                resTemp.next = ListNode(p%10)
                resTemp = resTemp.next
                nextSum = int(p / 10)
            l1 = l1.next
            l2 = l2.next
        while l1:
            p = l1.val + nextSum
            resTemp.next = ListNode(p%10)
            resTemp = resTemp.next
            nextSum = int(p / 10)
            l1 = l1.next
        while l2:
            p = l2.val + nextSum
            resTemp.next = ListNode(p%10)
            resTemp = resTemp.next
            nextSum = int(p / 10)
            l2 = l2.next
        if nextSum != 0:
            resTemp.next = ListNode(1)
        return res
