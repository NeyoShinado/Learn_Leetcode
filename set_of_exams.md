## Algorithm
(1)series_sum
给出一个正整数N和长度L，找出一段长度大于等于L的连续非负整数，他们的和恰好为N。答案可能有多个，我们需要找出长度最小的那个。
输入描述:
输入数据包括一行： 两个正整数N(1 ≤ N ≤ 1000000000),L(2 ≤ L ≤ 100)
输出描述:
从小到大输出这段连续非负整数，以空格分隔，行末无空格。如果没有这样的序列或者找出的序列长度大于100，则输出No。
>Summary:
1.√map(Fun, Iterable_object) , 对可迭代对象重复运算；返回迭代器(只可往前迭代，迭代完成时引起StopIteration 异常。)  
2.√python遍历习惯从0开始  
3.注意python数值运算过程中自动对数据类型的扩展变换  
4.^ 是按位异或运算符，** 是幂运算符


### String
(3)length_of_longest_substring
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
>Summary:
1.滑动窗口动态规划
2.Python 的数组矩阵操作、Numpy--array、Pandas--Series,df
3.Python 字符串函数


(11)longest_palindrome
找出字符串s的最长回文字串。
>Summary:
1.！注意指针加偏移值的负值，边界以及尾部加一情况  #"ccb"
2.情况枚举的相互独立，相互穷尽  #"sooos"
3.range() 函数的某位设定（正负步长）


(10)!median_of_sorted_seqs
找出两个正序数列的中位数，要求时间复杂度不大于O(log(m+n))
>Summary:
1.二分法(k分法)实现对数级别的复杂度
2.设计算法关于空间复杂度的考量
3.√归并排序算法：通过等份划分再逐层排序，使得排序算法的时间复杂度从暴力枚举的O(N^2)降至O(NlogN)，空间复杂度为O(N);Python与Java的排序算法也是用基于归并排序的Timsort。
归并排序的核心，是每次排序归并记录了上一次排序的大小顺序(二叉树结构)，所以每次归并摸清的集合元素以两倍的规模上升。枚举排序由于没有保留每次排序的记录，所以重复的计算量很大。
4.python测试
5.程序的边界条件考虑
6.编程的逻辑结构
7.尾递归




## Data Structure
(2)Sum_of_two_num(Linked-list)
给出两个非空的链表用来表示两个非负的整数。其中，它们各自的位数是按照逆序的方式存储的，并且它们的每个节点只能存储一位数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字0之外，这两个数都不会以0开头。
>Summary:
1.if-else 条件赋值语句的多种写法：
if a>b:
    c=a
else:
    c=b
------
c = a if a>b else b
------
c = [a,b][a>b]
------
c=(a>b and [a] or [b])[0]
2.√链表定义注意保留预结点，否则更新指针容易丢失表头
3.def foobar(a:int, b:"it's b", c: str=5) -> tuple: 函数注解语法(Function Annotations)
获取注解有两种方法：
①foobar.__annotations__; ②import inspect, inspect.signature(foobar)
另，Python 解释器不会基于函数注解自动进行类型检查，类型检查需要自己实现。




## Database
