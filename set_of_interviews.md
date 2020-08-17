# ---------------------------------------------
#### 面试
## 不同类型题目
### 考点内容
题号前 + '*'代表未完成，+ '!'代表要回顾
#### 为大类    ### 为细分类别
优先级：
项目 -> 语言基础 -> 计算机基础 -> 算法
# ---------------------------------------------




#### 项目
# ---------------------------------------------
## 1.微服务器:SpringCloud, SpringBoot, Dubbo

## 2.分布式服务框架：Zookeeper

## 3.消息队列：Kafka, RabbitMQ, RocketMQ

## 4.内存数据库：Memcached, Redis

## 5.分布式搜索引擎：Solr, Lucene, ES




#### 语言基础
# ---------------------------------------------
### 1.Javase
(1)Java实现生产者和消费者的三种方法
(2)init方法与clinit方法的区别
反射机制
(3)Java中的引用
(4)Java对象的创建过程
(5)Java中创建子类实例时会创建父类实例？
(6)Java的类加载机制 为什么会出现锁机制？
(7)抽象类和接口的区别
(8)双亲委派模型：启动加载器、扩展加载器、应用程序加载器
(9)重载与重写
(10)Java的类型擦除
(3)简述Java Object类中的方法有哪些
(3)char可以存储汉字嘛？
(3)抽象类和接口的区别
(3)静态分派与动态分派
(3)HashMap与HashTable的区别
(3)什么时候使用HashMap？它有什么特点？
(3)HashMap的基本原理及内部数据结构
(3)HashMap的put和get操作
(3)简述Java中的深拷贝与浅拷贝，C++中的浅拷贝和深拷贝
(3)解释一下static块和static变量的执行顺序
(3)equals()的重写规则
(3)Java中如何创建线程？
(3)JDK1.8新特性

### 2.集合源码
排序算法比较
Hashmap是线程安全的吗?为什么？
ArrayList与LinkedList区别
HashMap、LinkedHashMap和TreeMap
冒泡排序的优化以及快排过程及优化
红黑树
JDK7与JDK8中hashmap的区别
hashmap的初始容量为什么设置为16？
平衡二叉树的插入删除操作

### 3.JVM
JVM内存布局
JVM垃圾回收机制
JVM垃圾回收算法
哪些对象在老年代？
从年轻代到老年代执行的时间以及发生转移的场景
为什么存在GC？
简单可达性分析
Minor GC安全检查
垃圾回收器
引用记数法和可达性算法
类加载机制过程
双亲委派模型
双亲委派机制

### 4.多线程
锁分段技术、ConcurrentHashMap、扩容
Java同步线程有哪些方式？
volatile 和 synchronized的区别
讲一下同步异步（进程和IO）
synchronized和volatile的区别？
线程安全
对象的内存布局
哪些是线程安全的容器？
ConcurrentHashMap介绍
线程启动start和run
HashMap为什么线程不安全？
简述Java内存模型的happen before原则
volatile的原理和实现机制 || volatile到底如何保证可见性和禁止指令重排序的？
volatile关键字的两层语义 || 可见性
volatile保证原子性吗？
volatile能保证有序性吗？

### 5.IO




#### Hadoop
# ---------------------------------------------




#### 计算机基础
# ---------------------------------------------
### 1.数据库
# ---------------------------------------------


### 2.计算机网络
# ---------------------------------------------
1.简述TCP和UDP的区别
TCP是传输控制协议，提供面向连接、可靠的字节流服务。客户和服务器交换数据之前必须建立TCP连接才能传输数据。TCP提供超时重发、丢弃重复数据、校验数据、流量控制等功能。保证数据传输成功。
UDP是用户数据协议，一个面向数据报的运输层协议。UDP不提供可靠性，只是把应用程序传给IP层的数据报发送出去，不保证传输成功。UDP传输之前不需要客户端和服务器建立连接，且没有超时重发机制，所以传输速度很快。
举例，TCP像打电话，要有通路，对方不接就会等，接收有先后顺序；UDP像寄信，只管发，不管收；发信者收信者没有通路；先发未必先到，后发未必后到，还有可能不到。


2.七层协议每一层的任务及作用
①物理层；
②数据链路层：将数据分帧，并处理流控制。指定拓扑结构并提供硬件寻址；
③网络层：为数据在点对点之间传输建立逻辑链路，并分组转发数据包；
④传输层：选择传输协议并添加协议头如TCP,UDP,SPX;
⑤会话层：定义会话的开始、控制和结束；
⑥表示层：定义数据格式及加密；
⑦应用层：为应用程序提供接口和通信服务；


3.简述http状态码
(1)网页应用在接收和解释请求消息后服务器会返回一个HTTP响应消息，由三部分组成：状态行、消息报头、响应正文；
格式如：HTTP-Version(服务器HTTP协议版本) Status-Code(响应状态代码) Reason-Phrase(状态代码的文本描述) CRLF
(2)状态码由三个数字组成，第一个数字代表响应类别，分组如下：
1XX：指示信息--请求已接收，继续处理；
2XX：成功--请求已被成功接收、理解、接受；
3XX：重定向--要求完成请求必须进行进一步的操作；
4XX：客服端错误--请求有语法错误或无法实现；
5XX：服务器端错误--服务器未能实现合法的请求；
(3)常见状态码、描述及说明：
200 OK：客户端请求成功；
400 Bad Request：客户端请求有语法错误；
401 Unauthorized：请求未经授权；
403 Forbidden：服务器收到请求，但拒绝服务；
404 Not Found：请求资源不存在；
500 Internal Server Error：服务器发生不可预期的URL；
503 Server Unavailable：服务器当前不能处理客户端的请求；


4.简述http协议与https协议
https需要到ca申请证书，需要一定费用；
http是超文本传输协议，信息是明文传输；https这是具有安全性的ssl(Secure Sockets Layer)加密传输协议；
http和https使用完全不同的连接方式和端口。前者是80，后者是443；
http连接简单，是无状态的；https协议是由SSL+HTTP协议构建的可加密传输、身份认证的网络协议。


5.简述SSL协议
SSL介于应用层和TCP层之间，应用数据不再直接传给传输层，而是传递给SSL层。SSL层会对数据进行加密并加上SSL头，是网络传输层之上提供的一种基于RSA的对称加密算法。
RSA算法基于一个数论事实：计算两个大素数的乘积很容易，但对乘积进行因式分解却很难，因此可以将乘积公开作为加密密匙。


6.解析DNS过程
(1)DNS全称Domain Name System，即域名系统。是因特网上作为域名和IP地址相互映射的一个分布式数据库，能够让用户方便地通过域名而不是服务器识别需要的IP地址访问网站。
(2)DNS有两种查询方法：一种是递归查询，客户端询问的本地域名服务器若不知道被查询域名的IP地址，本地域名服务器会以DNS客户身份向顶级域名服务器继续查询，知道找到再层层传递回来；第二种是迭代查询，客户端根据顶级服务器返回的其他DNS服务器，不断地询问知道找到为止。
(3)DNS查询过程中，客户端和服务器都会加入缓存机制，减少查询次数。所以浏览器输入要访问网站域名时，操作系统先检查本地hosts文件是否有这个网址的映射关系，没有再询问DNS服务器和其他顶级服务器，知道完成域名解析。


7.三次握手，四次挥手的过程？？为什么三握？？
https://juejin.im/post/6844903958624878606
(1)三次握手
①简介：
三次握手指建立一个TCP连接时，需要客户端和服务器总共发送三个包。进行三次握手的主要作用是为了确认双方的接受能力和发送能力是否正常、指定自己的初始化序列号为后续可靠性传递做准备。实质上就是连接服务器指定端口，建立TCP连接，同步连接双方的序列号和确认号，交换TCP窗口大小信息。
②具体流程：
刚开始客户端处于closed状态，服务端处于listen状态。进行三次握手：
○第一次握手：客户端给服务端发一个SYN报文，指明客户端的初始化序列号ISN(c)。此时客户端处于SYN_SEND状态。
首部的同步位SYN=1，初始序号seq=x，SYN=1的报文段不能携带数据，但要消耗一个序号。
○第二次握手：服务器收到客户端SYN报文后，会以自己的SYN报文作答，也指定了自己的初始化序列号ISN(s)。同时将客户端的ISN+1作为ACK的值，表示已收到客户端的SYN，此时服务器处于SYN_RCVD状态。
确认报文段中SYN=1，ACK=1，确认号ack=x+1，初始序号seq=y。
○第三次握手。客户端收到SYN报文后，同样会发送一个ACK报文，把服务器的ISN+1作为ACK值返回，表示已经收到服务端的SYN报文。此时客户端处于ESTABLISHED状态，服务器收到ACK报文后，也处于ESTABLISHED状态。此时，双方已建立起连接。确认报文段ACK=1，确认号ack=y+1，序号seq=x+1(初始为x，第二个报文段要+1)。ACK报文段不携带数据则不消耗序号。
在socket编程中，客户端执行connect()时，将触发三次握手。

(2)需要三次握手的原因：

第一次握手：服务端确认客户端的发送能力、服务端的接收能力正常(确认有传输请求，虽然可能时延时的请求)；

第二次握手：客户端确认：服务端的接收、发送能力正常，客户端的接收、发送能力也正常。但服务端不确定客户端的接收能力是否正常(确认是否是同步的请求)；

第三次握手：服务端确认客户端的接收能力正常(或者客户端需要传输数据)。客户端的接收、发送能力也正常。

因此需要三次握手才能达到要求。如果只需要两次握手，有可能出现以下问题：客户端发出连接请求，因为延迟未收到确认，客户端重发一次。后来收到确认建立连接，传输完成就释放连接。这是第一个报文在网络结点延迟后到达服务器。服务器认为有新的连接请求，于是向客户端发送确认报文，建立连接(不采用三次握手)。但客户端忽略服务端的确认报文，也不发送数据，则服务端一直等待客户端发送数据，浪费资源。

最简单的例子：两人手机通信，男方问：“你爱我吗？“（第一次握手），然后男方收到女方回复“我爱你”（第二次握手），最后直到女方也收到男方的表白“我也爱你”（第三次握手）。两人的情侣关系才最终确认。

(3)半连接队列

服务器第一次收到客户端SYN后，双方还没有建立连接，服务器把SYN_RCVD状态下的请求连接放到一个队列（半连接队列）。

建立起连接后的请求连接会放到全连接队列中，如果队列满了就出现丢包现象。

(4)ISN(Initial Sequence Number)

一端发送SYN时会为连接选一个初始序号ISN，ISN不是固定的，随时间而变化。所以每个连接都有不同的ISN。这样做的目的时为了防止延迟的分组以后又被传送，导致对方错误解析。

另外一个重要作用是建立连接时不固定的ISN让攻击者不容易猜出后续序列号。

(5)第三次握手可以携带数据

第一、二次握手不可以携带数据。第三次握手时是可以携带数据的。

前两次握手时有效的连接还没建立起来，如果可以携带数据，攻击者只要在SYN报文中放入大量数据，就会占用服务器的许多资源。而在第三次握手时，客户端已经处于ESTABLISHED状态，客户端已经建立起连接且服务器端的接收发送能力正常，所以能携带数据。

(6)SYN攻击

①SYN攻击是典型的DoS/DDoS攻击：

服务器的资源是在二次握手分配的，客户端的资源是在三次握手分配的。所以服务器容易受到SYN洪泛攻击（客户端在短时间内伪造大量不存在的IP地址，向服务器不断发送SYN包；服务器则回复确认包且等待客户端确认，由于源地址不存在，服务器需要不断重发直至超时，未连接队列会长时间被占用，导致正常的SYN请求因为队列满而被丢弃，从而引起网络拥堵瘫痪）。

②检测防御方法：

当服务器上看到大量半连接状态，且源IP是随机的，就能断定这是SYN攻击。Linux能用 > netstat -n -p TCP | grep SYN_RECV 指令检测SYN攻击。

防御方法有：缩短SYN超时时间；增加最大半连接数；过滤网关保护；SYN cookies技术。

(7)四次挥手

①终止一个连接要经过四次挥手。这是由TCP的半关闭--half-close（连接一端结束发送后还能受到另一端数据的能力）造成的。客户端和服务器都可以主动发起挥手。

②过程（客户端发起为例）：

○第一次挥手：客户端发送一个FIN报文，指定一个序列号(FIN=1,序号seq=u)。客户端处于FIN_WAIT1（终止等待1）状态，主动关闭TCP连接，停止发送数据。等待服务器确认。

○第二次挥手：服务器受到FIN后，把客户端的序列号+1作为ACK报文序列号，发送ACK确认报文(ACK=1,ack=u+1,seq=v)。此时服务器处于CLOSE_WAIT（关闭等待）状态。此时TCP处于半关闭状态，客户端到服务器的连接释放。客户端收到确认后，进入FIN_WAIT2（终止等待2），等待服务器发出连接释放报文。

○第三次挥手：如果服务器也想断开连接，和客户端第一次挥手一样，发送FIN报文(FIN=1,ACK=1,序号seq=w,确认号ack=u+1)。此时服务器处于LAST_ACK（等待确认）状态，表示服务器也不会再向客户端发送数据。等待客户端确认。

○第四次挥手：客户端收到FIN，一样发送一个ACK报文(ACK=1,seq=u+1,ack=w+1)作答，此时客户端处于TIME_WAIT状态。等待一段时间（等待计时器设置的2MSL）确保服务器收到ACK报文再自动进入CLOSED状态。服务器收到报文后执行被动关闭，不会有TIME_WAIT状态，进入CLOSED状态，关闭连接。

(8)四次挥手的原因

建立连接时服务器可以同时发送ACK应答报文和SYN同步报文。但是关闭连接时可能有数据没发送完毕，这是不会立即关闭SOCKET，而是先发送ACK报文，等剩余报文发送完成再发送FIN报文，所以需要四次挥手。

(9)2MSL等待状态

①TIME_WAIT状态也称为2MSL等待状态。TCP都有一个报文段最大生存时间MSL(Maximum Segment Lifetime)，是任何报文被丢弃前在网络内的最长时间。该时间是有限的，因为TCP报文作为IP数据报在网络内传输，IP数据报有限制器生存时间的TTL字段。

②2MSL的意义：

一方面，客户端最后一个ACK有可能丢失（需要一个MSL）。服务器收不到FIN-ACK的确认报文，会超时重发一次（再需要一个MSL），客户端收到后重传一次确认报文，等待计时器重新计时，直到最后双方都能正常关闭；

另一方面，2MSL等待时间能使本链接产生的所有报文都从网络中消失，防止失效的连接请求报文出现在下一连接。

③影响：在2MSL等待期间，定义这个连接的插口（客户端IP地址、端口号，服务器IP地址、端口号）都不能使用。


### 3.操作系统
# ---------------------------------------------
## Linux 概述
(1)什么是Linux
Linux是一套免费的性能稳定的类Unix多用户网络操作系统，继承了Unix以网络为核心的设计思想。是一个基于POSIX和Unix的多用户、多任务、支持多线程和多CPU的操作系统。能运行主要的Unix工具软件、应用程序和网络协议。

(2)Linux和Unix的区别
①开源性：Linux是免费的开源操作系统；Unix是对源码实行知识产权保护的商业操作系统，需要付费使用；
②跨平台性：Linux有良好的跨平台性，能在多种硬件平台上使用；
③可视化界面：Linux拥有窗体管理系统；Unix只有命令行操作；
④硬件环境：Linux对硬件要求较低，安装配置容易；
⑤用户群体：Linux用户群体广泛；Unix多是安全性要求高的大型企业使用；

(3)Kernel是什么
Linux系统的核心，包含内核管理的核心代码。Kernel控制着计算机系统上的所有软硬件，由操作系统中用于管理存储器、文件、外设和系统资源(CPU)的部分组成。负责运行进程并提供进程间的通信。

(4)Linux的基本组件
Kernel、shell和GUI

(5)体系结构
①用户空间：应用程序和C库；
②内核空间：系统调用接口；内核；平台架构代码；

(6)为什么要分为用户空间和内核空间
背景：现代CPU实现了不同的工作模式，执行的指令和访问寄存器也不同。Linux为了保护内核安全，把系统分成了两部分。用户空间和内核空间是程序执行的两种不同状态，可以通过系统调用和硬件中断完成用户空间到内核空间的转移。

(7)BASH和DOS的区别
①BASH命令区分大小写；
②BASH下，/是目录分隔符，\是转义字符；DOS下，/是命令参数分隔符，\是目录分隔符；
③DOS遵循命名文件名约定：8字符文件名后+"."，扩展名三个字符;

(8)Linux启动过程
①主机加电自检，加载BIOS硬件信息；
②读取MBR引导文件；
③引导Linux内核；
④运行第一个进程init（进程号1）；
⑤进入相应的运行级别；
⑥运行终端，输入用户名和密码；

(9)Linux使用的进程间通信方式
①管道pipe，流管道s_pipe，有名管道FIFO；
②信号；
③消息队列；
④共享内存；
⑤信号量；
⑥套接字socket；

(10)Linux由哪些系统日志文件
/var/log/messages：进程日志文件的汇总，从该日志可以看出任何入侵；

(11)交换空间(swap space)是什么
RAN没有足够内存容纳所有执行程序时，用于临时保存并发运行程序的空间。

(12)root账号
root账户类似于管理员账户，有完全控制系统的权限。

(13)LILO
Linux的引导加载程序，将Linux系统加载到主内存中。

(14)BASH
Linux默认的Shell。

(15)CLI
命令行界面，command line interface

(16)开源的优势
能将软件、源码免费地分发他人，人们可以添加功能以及调试更正源码的错误，发布增强版本的源码，让它运行得更好，使得整个社区的人收益。


## 磁盘、目录、文件
(1)Linux文件系统
Linux的重要概念：一切都是文件。所有资源：网卡、磁盘驱动器、打印机、IO设备、普通文件目录都能被看作一个文件。用户可以通过读写设备文件的方式实现对设备的访问。
Linux支持5种文件类型：①普通文件存储信息；②目录文件管理文件；③链接文件用于不同目录文件的共享；④设备文件访问硬件设备；⑤命名管道(FIFO)协助京城之间的通信。

(2)常用目录
①/bin：常用命令的可执行文件；
②/etc：系统管理和配置文件；
③/home：所有用户文件的根目录；
④/usr：存放系统应用程序；
⑤/opt：额外安装的应用程序包；
⑥/root：系统管理员的主目录；
⑦/proc：虚拟文件系统目录；
⑧/sbin：存放系统级别的二进制可执行文件，只有root能访问；
⑨/dev：设备文件；
⑩/mnt：临时挂载其他文件系统的挂载点；
⑾/boot：存放系统引导时的依赖文件；
⑿/lib：系统运行相关的库文件；
⒀/tmp：公用临时文件存储点；
⒁/var：存放运行时需要改变数据的文件，大文件(日志文件)的溢出区；
⒂/lost+found：非正常关机临时保存的文件；

(3)inode
块中存放文件的元信息（创建者、创建日期等）的区域为inode，又称索引节点，记录了文件的磁盘地址表。Linux下的文件都通过inode识别。

(4)硬链接、软链接
①硬链接是一个指向文件索引节点的指针，不受文件位置变动影响。以文件副本形式存在，不占用实际空间。且硬链接和源文件中的一个存在，文件都会保留下来。
缺点：不能在不同文件系统的文件间建立；只有root才能创建；不能给目录创建。
②软链接没有文件系统的限制以及跨越机器、网络进行链接，同时任何用户都能创建。可以给不存在的文件，目录创建。
缺点：只是包含了源文件的路径信息，源文件移动位置就找不到了。


## 安全
(1)网站数据库注入
编写代码时没有用户输入数据的合法性进行判断，使得用户可以提交一段数据库查询代码获取数据。这就是SQL注入。由于从正常的WWW端口访问，如果不查看日志很难发现入侵。可以使用nginx_waf过滤预防。

(2)CC、DDos攻击


## Shell
(1)Shell脚本
Shell脚本是管理员完成日常任务的文本文件。

(2)变量类型
①系统变量：通常大写字母命名，set命令查看
②用户自定义变量：echo $<var>查看变量值

(3)$?
检查上一命令是否成功执行，是返回0，否则返回非零。

(4)使脚本可执行
>chmod a+x myscript.sh

(5)调试shell脚本
>sh -x myscript.sh / sh -nv myscript.sh

(6)标准/错误输出重定向
&> file

(7)测试文件权限/类型
>test

(8)获取终端输入
>read var    # 输入赋值给变量

(9)执行算术运算
>expr ... / $[...]


## 实操
(1)操作系统版本
桌面用户Ubuntu；服务器RHEL或CentOS；两者首选CentOS

(2)解决用户反馈网站访问慢
①服务器出口带宽不够：服务器并发量大导致用户出口带宽小；跨运营商网络导致带宽缩减。
②服务器负载过大，响应不过来：使用w 或uptime命令查看系统负载，负载高就用top查看cpu、mem占用情况，要么CPU繁忙，要么内存不足；
③数据库瓶颈：慢查询比较多，需要SQL优化；数据库响应慢，可加一个数据库缓存；也可搭建MySQL主从，一台MySQL服务器负责写，其他几台从数据库服务器负责读。
④网站开发代码没有优化好。

(3)针对网站访问慢，怎么排查？怎么解决？
排查：
①确定是用户端还是服务端问题；
②如果自己访问也慢，利用浏览器调试器查看加载哪些数耗时多；
③针对服务器负载情况，查看硬件消耗情况；
④如果硬件资源消耗不高，就查看日志。
解决：
①出口带宽问题--加大出口带宽；
②慢查询多--优化SQL语句；
③数据库响应慢--添加数据库缓存；或搭建MySQL主从服务器；
④购买CDN服务，加载用户访问；
⑤从框架进行优化，多服务器分工；

(4)Linux性能调优
①关闭daemons；
②关闭GUI；
③改变内核参数；
④处理器子系统调优；
⑤内存子系统调优；
⑥文件子系统调优；
⑦网络子系统调优；


## 文件管理命令
(1)cat
功能：链接文件打印到标准输出设备
用法：
①显示整个文件 >cat filename；
②键盘输入创建文件 >cat > filename；
③合并文件 >cat file1 file2 > file；

(2)chmod
功能：更改文件拥有者、群组、其他用户的文件调用权限
用法：
①文件详细信息：>ls -l
-rwxr--r-- 1 root root 1K 11-13 06:03 test.log
第一个字符"-"表非目录文件，"d"表目录
②给指定用户指定权限：>chmod 751 -R test/ / chmod u=rwx, g=rx, o=x -R test/  # -R 处理指定目录及其之目录的所有文件

(3)chown
功能：修改文件的拥有者

(4)cp
功能：赋值至文件或目录
用法：①-i 原文件存在提示是否覆盖，shell脚本没有-i参数会自动覆盖！；

(5)find
功能：文件树中查找文件并进行相应操作
用法：
①格式：find path -options [-print -exexc -ok]；
②命令选项：-name 按文件名查找；-perm 按文件权限查找；-user 按属主查找；-group 按文件属组查找；-type 按文件类型查找
③example：
	find -atime -2  # 两天内修改过的文件；
	find ./ -name '*.log'
	find /opt -perm 777
	find -size +1000c  # 大于1K的文件
	find -size 1000c  # 等于1K的文件

(6)head
功能：显示文件开头，默认10行

(7)less
功能：浏览文件，且不需要加载整个文件，能查看多个文件，并有翻页模式

(8)ln
功能：创建文件同步链接，节省空间
参数：-b 覆盖以前的链接；-s 创建软链接

(9)locate




## 文件编辑命令


## 磁盘管理命令


## 系统管理命令


## 备份压缩命令




#### Base/编程算法
# ---------------------------------------------
### 1.排序算法
1.冒泡排序 -- TC:O(N^2), SC:O(1), 稳定
步骤：指针不断右移，每次修正一对元素，最后一次修正交换的位置表示后面的元素已正确排序；重复直至没有元素交换发生。
源码：
def bubbleSort(nums):
    for i in range(1, len(nums)):
        for j in range(len(nums)-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

2.选择排序 -- TC:O(N^2), SC:O(1), 不稳定
步骤：不断从未排序数组中找出最小/大元素，放大已排序数组的队尾，重复直至排序完毕。
源码：
def selectionSort(nums):
    for i in range(len(nums)-1):
        minIndex = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[i]:
                minIndex = j
        if i != minIndex:
            nums[i], nums[minIndex] = nums[minIndex], nums[i]
    return nums

3.插入排序 -- TC:O(N^2), SC:O(1), 稳定
步骤：像打扑克一样，从未排序数组抽出元素插入到排序数组合适的位置中。
源码：
def insertSort1(nums):
    for i in range(1, len(nums)):
        insertIndex = i-1
        while nums[insertIndex] > nums[i] and insertIndex >= 0:
            insertIndex -= 1
        nums.insert(insertIndex+1, nums.pop(i))
    return nums

def insertSort2(nums):
    for i in range(len(nums)):
        insertIndex = i-1
        current = nums[i]
        while insertIndex >= 0 and nums[insertIndex] > current:
            nums[insertIndex+1] = nums[insertIndex]
            insertIndex -= 1
        nums[insertIndex+1] = current
    return nums

4.希尔排序 -- TC:O(NlogN), SC:O(1), 不稳定
步骤：插入排序的改进版，插入排序在几乎排好序的数组中效率高，TC能达到O(N)。但对于一般分布的数据是低效的，一次遍历只移动一位。
希尔排序按不同的增量因子将数组分为若干子数组分别进行插入排序，等到整体“基本有序”时再进行插入排序。
源码：
def shellSort(nums):
    import math
    gap = 1
    while(gap < len(nums)/3):
        gap = gap*3 + 1
    while gap > 0:
        for i in range(gap, len(nums)):
            tmp = nums[i]
            j = i - gap
            while j >= 0 and nums[j] > tmp:
                nums[j+gap] = nums[j]
                j -= gap
            nums[j+gap] = tmp
        gap = math.floor(gap/3)
    return nums

5.归并排序 -- TC:O(NlogN), SC:O(N), 稳定
步骤：采用分治思想，将数组不断二分为最小子数组，然后对子数组不断排序合并重组出完整的数组
实现：自上而下递归；自下而上迭代(推荐)
源码：
def mergeSort(nums):
    import math
    if len(nums) < 2:
        return nums
    middle = math.floor(len(nums)/2)
    left, right = nums[0:middle], nums[middle:]
    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop[0])
        else:
            result.append(right.pop[0])
    while left:
        result.append(left.pop[0])
    while right:
        result.append(right.pop[0])
    return result

6.快速排序 -- TC:O(NlogN), SC:O(logN), 不稳定
原理：快排是在冒泡排序基础上的分治法，优于一般的对数复杂度算法（因为常数因子较小），且出现最坏情况O(N^2)的可能性很低（需要逆序数组）。通常默认使用快排算法。
步骤：随机抽出一个元素作为基准(pivot)，将数列划分为小于基准和大于基准两部分，再递归地从子序列中选出子基准划分更小的序列，直到不能再划分为止。由于划分后的子序列不断变小，需要比较的空间也呈指数级减少。
源码：
def quickSort(nums, left=None, right = None):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(nums)-1 if not isinstance(right, (int, float)) else right
    if left < right:
        partitionIndex = partition(nums, left, right)
        quickSort(nums, left, partitionIndex-1)
        quickSort(nums, partitionIndex+1, right)
    return nums

def partition(nums, left, right):
    pivot = left
    index = pivot + 1
    i = index
    while i <= right:
        if nums[i] < nums[pivot]:
            swap(nums, i, index)
            index += 1
        i += 1
    swap(nums, pivot, index-1)
    return index-1

def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]

7.堆排序 -- TC:O(NlogN), SC:O(1), 不稳定
步骤：创建一个堆，不断shiftdown() ，然后将堆首推出，堆的尺寸减一，直至排序完毕。
源码：
def buildMaxHeap(arr):
    import math
    for i in range(math.floor(len(arr)/2), -1, -1):
        heapify(arr, i)

def heapify(arr, i):
    left = 2*i + 1
    right = 2*1 + 2
    largest = i
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    if right < arrLen and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def heapSort(arr):
    global arrLen
    arrLen = len(arr)
    buildMaxHeap(arr)
    for i in range(len(arr)-1, 0, -1):
        swap(arr, 0, i)
        arrLen -= 1
        heapify(arr, 0)
    return arr

# ------ 以上算法都为比较排序算法 ------ #
容器的不同用法：
①计数排序：根据键值分配桶；
②桶排序：根据范围分配桶；
③基数排序：根据键值的位来分配桶；

8.计数排序 -- TC:O(N+K), SC:O(K), 稳定
前提：要求知道输入整数数据的确定范围(明确大小的基数，字符串之类具有可比较性的对象则不行)
原理：开辟额外数组空间，统计每个数出现的频数，再反向填充目标数组；基数范围小时很快
源码：
def countingSort(arr, maxVal):
    bucketLen = maxValue + 1
    bucket = [0] * bucketLen
    arrLen = len(arr)

    for i in range(arrLen):
        if not bucket[arr[i]]:
            bucket[arr[i]] = 0
        bicket[arr[i]] += 1

    sortedIndex = 0
    for j in range(bucketLen):
        while bucket[j] > 0:
            arr[sortedIndex] = j
            sortedIndex += 1
            bucket[j] -= 1
    return arr

9.桶排序 -- TC:O(N+K), SC:O(N+K), 稳定
原理：是计数排序的改进，利用映射函数将数据存在不同的桶中，然后再对桶内元素进行比较排序；桶的数量越多，数据分得越均匀，速度越快
# 例：对小数进行桶排序
def bucketSort(arr, max_num):
    buf = {i:[] for i in range(int(max_num)+1)}
    N = len(arr)
    for i in range(N):
        buf[int(arr[i])].append(arr[i])
    arr = []
    for i in range(len(buf)):
        if buf[i]:
            arr.extend(sorted(buf[i]))
    return arr

10.基数排序 -- TC:O(N*K), SC:O(N+K), 稳定
原理：将数据按位数切割为不同部分，然后按照位数分别进行比较。因而能处理字符串、浮点数等数据类型
如：按高位至低位的顺序进行桶排序，完成十进制数的排序。

### 2.选择算法

### 剑指offer常问
字符串转换成整数
链表中倒数第K个结点 -- 栈
二维数组中的查找 -- 二分查找
替换空格
从尾到头打印链表 -- 栈实现
重建二叉树
*用两个栈实现队列
*斐波那契数列及变形题
二进制中1的个数 -- 布莱恩算法
在O(1)时间删除链表结点
调整数组顺序使奇数位于偶数前面 -- 双指针
反转链表 -- 保存父子结点栈实现
合并两个排序的链表
树的子结构
*二叉树的镜像
顺时针打印矩阵 -- 引入层数变量
*栈的压入、弹出序列
二叉搜索树的后序遍历序列
*二叉树中和为某一值的路径
数组中出现次数超过一半的数字
最小的k个数 -- 最大堆
连续子数组的最大和
第一个只出现一次的字符
两个链表的第一个公共结点 -- visited集合
链表中环的入口结点 -- Floyd判环
*跳台阶
变态跳台阶
矩形覆盖
从上往下打印二叉树 -- BFS
二叉搜索树的第K个结点

### 位操作
(1)a ^ b ^ b = a的应用
1.原地交换两个变量
通常做法：
a = a + b
b = a - b
a = a - b
异或做法：
a = a ^ b
b = a ^ b
a = a ^ b
位运算不会溢出，同时位运算速度也更快
2.O(n)复杂度找出成对数中的单独数
res = a1 ^ a2 ^ ... ^ a2 ^ a1 ^ alone
3.硬盘备份恢复
硬盘分为N部分，最后一部分n用于备份，是由其他部分异或得到的。当某一部分a数据受损之后，就可以用其他部分异或恢复：a^b^...^(n-1) = n -> a^a^b^...^(n-1)^n^n =n^n^a=a

