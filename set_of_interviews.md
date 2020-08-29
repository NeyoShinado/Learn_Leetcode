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
**(1)Java实现生产者和消费者的三种方法
生产者消费者问题也称有限缓冲问题，是经典线程模型：生产者和消费者在同一时间段共用同一个存储空间，生产者存放数据，消费者取用数据。协调不好会出现如下问题：存储空间已满，消费者等待生产者让出空间以取出产品；生产者等待消费者消费产品，从而添加产品。相互等待引发死锁。
Java实现的几种方法：
①wait()/notify()；②await()/signal()；③BlockingQueue阻塞队列；④信号量；⑤管道；


(2)init方法与clinit方法的区别
执行类构造器<clinit>()方法是类初始化的过程。
详解<clinit>()方法由编译器按顺序自动收集类中类变量赋值语句和静态初始化块的语句组合而成；在执行子类<clinit>()方法时先执行父类<clinit>()方法；接口不能使用静态初始化块，但仍有变量初始化操作，因此也会生成<clinit>()方法。**但只有使用了父接口定义的变量时，执行接口<clinit>()方法才会先初始化父接口的<clinit>()方法；另，因为接口的变量都是static final常量，在准备阶段已经初始化了，所以初始化实现类时也不会执行接口的<clinit>()方法。
①执行时机不同：init 是对象构造器方法，执行new时调用该对象的constructor方法时才会执行init方法；而clinit是类构造器方法，jvm进行类加载--验证--解析--初始化中的初始化阶段会调用clinit方法。
②目的不同：init是实例构造器，初始化非静态变量；而clinit是class类构造器，初始化静态变量和静态代码块。
③执行次数：在一个类的生命周期里，类构造器<clinit>()最多被JVM调用一次，实例构造器<init>()能被调用多次。


**(3)反射机制(reflact)
①背景：反射机制是实现Java动态性的关键：Java程序运行，虚拟机要先加载Java类，生成.class文件。若加载不成功就无法编译，自然运行不了。(例如A程序需要B开发的类，但B类没完成，此时无法通过编译；或程序只有运行时才能根据具体环境加载依赖的类，用不到的类就不加载，这就需要动态性)。
②定义：反射机制的起源是java.lang.Class类。每一个类加载后，JVM都会产生一个Class对象(类型类-Class对象是用来代表一个类型的实例)到堆中，作为方法区类的数据结构接口。通过class对象就能获取类的方法、成员、构造器以及修饰符。
总的来说，就是程序运行时再探知、加载编译期间未知的.class文件，并获得类/对象的属性或方法，探知类的结构，这就是反射机制。
③用法：
# 类型类的获取
public void TestClass{
	...
}
TestClass testClass = new TestClass();
testClass.getClass() == TestClass.class;    # 从对象或类型获取类型类的方法
# 访问当前类及继承类的变量
Class mClass = TestClass.class;    # 获取Class类实例
mClass.getName();    # 获取类的名称
Field[] fields = myClass.getFields();    # 获取public变量
Field[] fields = myClass.getDeclaredFileds();    # 获取所有访问权限成员变量
field.getModifiers();    # 获取变量访问权限
field.getType().getName();	# 获取变量类型
# 访问当前类及继承类的方法
Method[] mMethods = mClass.getMethods();	# 获取public方法
Method[] mMethods = mClass.getDeclaredMethods();    # 获取所有权限方法
method.getReturnType();		# 获取方法的返回值类型
method.getParameters();		# 获取方法的参数
method.getExceptionTypes();		# 获取方法抛出的异常
# 访问修改私有类的私有方法
Method privateMethod = mClass.getDeclaredMethod("PrivateMethodName", String.class, int.class)    # 获取私有方法，第一个参数位私有方法名，第二个为方法参数的类型类
privateMethod.setAccessible(true)    # 获取访问权限
privateMethod.invoke(testClass, newStringPar, newIntPar)    # 通过invoke反射修改对象私有方法的参数
# 访问修改私有类的私有变量
Field privateField = mClass.getDeclaredField("privateFieldName")    # 获取对象私有变量
privateField.setAccessible(true)    # 获取私有变量的访问权
privateField.set(testClass, newPar)    # 通过set(object, val)修改变量值
# 访问操作私有类的私有常量
**①final修饰的基本类型及String常量在JVM编译.class文件时会被优化以提升效率：将引用常量的代码直接替换成常量值。(Integer, Long, Boolean等包装类和Object类则不会优化)
所以通过反射修改常量虽然真的可以修改程序里常量的值，但是运行阶段还是直接使用原有的值，反射修改没意义，达到了“不能修改”的效果。
②编译优化：
> private final String Final_Value = "hello"
> if Final_Value.equals("world")		# .java源文件
> if "hello".equals("world")		# 编译后的.class文件
③能修改运行常量值的情况
情况一：Java运行常量声明时不赋值，留在构造器中赋值。由于new对象时才会调用构造器，所以此时的编译只会优化构造器中的赋值语句，取值语句还是指向常量而不是替换的值。所以能用反射机制修改常量。
> class TestClass{
	private final String Final_Value;
	public TestClass(){
		this.Final_Value = "Final";
	}
	public String getFinalValue(){
		return this.Final_Value;
	}
}		# 构造器赋值，.java源文件
> class TestClass{
	private final String Final_Value = "Final";		# 构造器赋值语句被优化
	public TestClass(){}
	public String getFinalValue(){
		return this.Final_Value;		# getter函数的赋值指向常量而非具体值
	}
}
情况二：使用三目表达赋值而非直接的赋值语句，因为运行时的计算不会被编译器计算，也不会被优化。所以能通过反射修改。
> private final String Final_Value = null == null? "Final": null;	# 效果等同于直接赋值的三目赋值语句


**(4)Java中的引用
引用类型保存的值是对象的内存地址，赋值运算只会写入新对象的地址。原有对象不会改变，也不被任何引用指向，称为“垃圾对象”，后续会被垃圾回收器回收。
Java有四种引用类型：
①强引用：Java最常见的引用，类似于"Object a = new Object()"这类引用，可以直接访问目标对象，强引用对象不会被垃圾回收器回收，可能导致内存泄漏；
②软引用：
③弱引用：
④虚引用：


(5)Java对象的创建过程
对象创建过程包含类初始化和类实例化两个阶段。
①对象创建的方法：通过new关键字调用任意类构造器实现；通过Class类的newInstance(反射机制)调用无参构造器实现；使用java.lang.relect.Constructor类的newInstance(反射机制)创建，可以调用有参和私有的构造函数；使用clone方法创建实现Cloneable接口的对象，途中不会调用任何构造器；使用反序列机制创建实现Serializable接口的对象，同样不使用构造器；
②创建过程：虚拟机分配内存存放实例变量，同时赋予默认值（0）。然后根据三种结构执行初始化(实例变量初始化、代码块初始化、构造器初始化)。为保证顺利初始化对象，显示调用父类构造器时要放在子类构造器的第一行。总的来说，类的实例化是一个递归过程：先向上递去探寻顶层父类，再向下归来初始化各相关类。
**注：若子类重写了父类初始化用到的方法，子类初始化前的父类初始化，由于重写方法用到的子类变量仍没随着子类初始化而建立，所以会以默认值返回给父类初始化调用。
总的来说，类实例化的一般过程是：父类的类/静态构造器<clinit>() -> 子类的类/静态构造器<clinit>() -> 父类的成员变量和实例代码块 -> 父类的构造函数 -> 子类的成员变量和实例代码块 -> 子类的构造函数。
③其他：实例变量在对象初始化过程中最多能被赋值几次？第一次，JVM为对象分配完空间后给每一个实例变量赋默认值；第二次，初始化声明实例变量时的赋值操作；第三次，代码块的初始化操作；第四次，构造函数的初始化操作。
类初始化需要在类实例化之前进行，但不意味着要类初始化结束后才能类实例化，实例化可以嵌套到静态构造器中与类初始化同时进行。

#test# 最终输出的结果是什么
public class StaticTest {
    public static void main(String[] args) {
        staticFunction();
    }

    static StaticTest st = new StaticTest();

    static {   //静态代码块
        System.out.println("1");
    }

    {       // 实例代码块
        System.out.println("2");
    }

    StaticTest() {    // 实例构造器
        System.out.println("3");
        System.out.println("a=" + a + ",b=" + b);
    }

    public static void staticFunction() {   // 静态方法
        System.out.println("4");
    }

    int a = 110;    // 实例变量
    static int b = 112;     // 静态变量
}/* Output: 
        2
        3
        a=110,b=0
        1
        4
 */


(6)Java中创建子类实例时会创建父类实例吗？
不会，创建子类实例所需的父类属性从方法区获得，存储的空间位于子类的堆内存，是属于子类实例的。


(7)Java的类加载机制 为什么会出现锁机制？
类加载机制分为五个部分：
①加载：在内存中生成这个类的java.lang.Class对象，作为方法区这个类的数据入口；加载在JVM外部实现以便应用程序决定通过哪种类加载器获取类；
②验证：确保Class文件的字节流包含的信息符合虚拟机要求；
③准备：在方法区分配类变量的内存并设置初始值(基本类型为0，引用类型为null)，不过类变量若是final，编译器会为value生成ConstantValue属性，赋值为指定值；
④解析：虚拟机将常量池中的符号引用替换为直接引用；
⑤初始化：初始化阶段开始真正执行类中的Java代码，执行类构造器<clinit>方法的过程；


(8)抽象类和接口的区别
接口可以理解为一种比“抽象类”更抽象的类型；
①语法层面上：抽象类可以提供成员方法实现的具体细节；变量可以是各种类型；可以有静态代码块和静态方法，接口不行；一个类只能继承一个抽象类，但可以实现多个接口；
②设计层面上：抽象类是对整个事物的抽象，采用模板式设计，便于公共部分的更改；接口则是对类的局部行为进行抽象，采用辐射式设计，改动一个接口要对所有实现类进行改动。


(9)双亲委派模型：启动加载器、扩展加载器、应用程序加载器
①启动类加载器(Bootstrap ClassLoader)：加载JAVA_HOME\lib目录中的类；
②扩展类加载器(Extension ClassLoader)：加载JAVA_HOME\lib\ext目录中的类；
③应用程序类加载器(Application ClassLoader)：加载用户路径上的类。
一个类收到类加载请求，会将这个请求委派给父类完成，所有加载请求都应该传到启动类加载器中。只有父类加载器无法完成请求时，子类加载器才会尝试加载。双亲委派的好处是无论使用哪个加载器加载，最终都委托给启动类加载器加载，保证了得到同样的Object对象。


(10)重载与重写
重写是子类对父类允许访问方法实现细节进行重写。返回值类型是原方法返回值的派生类，形参不变，访问权限只能更低。只能抛出父类异常及其子异常。重写体现父类子类的多态性；
重载是一个类里方法名字相同、参数不同的现象；重载方法的返回值类型、访问修饰符、抛出异常可以不同；重载体现同一个类的多态性；


**(11)Java的类型擦除
**泛型即参数化类型。是什么？
Java的泛型基本上在编译器中实现，编译结束后会擦除Java的泛型


(12)简述Java Object类中的方法有哪些
①wait：让当前线程进入等待状态，也能释放当前线程的锁；
②notify：唤醒当前对象上等待的单个线程； 
③notifyAll：唤醒所有线程；
④clone：克隆先给新对象分配内存，然后再将原对象的各个域填充到新对象域中，是深复制； 
⑤hashcode：根据具体的哈希函数将对象的信息映射成一个散列值，在包含容器类中使用能减少equals方法的调用次数，提高检索性能；
⑥equals：==可以理解为“浅对比”，即直接对比引用类型变量是否指向同一个对象地址；重写的equal方法往往用于实现“深对比”的作用，比较的是指向对象的内容；
⑦toString：返回该对象的字符串表示，通常形式--“类名@此对象的无符号十六进制哈希码表示”；
⑧finalize：清理本地对象占用的内存资源；


(13)char可以存储汉字嘛？
char是按字符存储的，可以存储Unicode字符集中的汉字。
默认情况下unix平台，javac用utf-8格式读取java源文件，然后以utf-8格式写.class；默认情况下windows平台，javac用gbk格式读取java源文件然后以utf-8格式写.class；


(14)抽象类和接口的区别
略


(15)静态分派与动态分派
分派指的是java对方法的调用，即如何确定运行时方法的执行版本，是多态性的体现。重载是静态分派，重写是动态分派。
重载在编译期间确定，执行重载方法的版本是按照参数的静态类型而不是实际类型作为分派依据。
虚拟机的invokevirtual指令实现动态调用的解析过程：①找到对象的实际类型C；②查找类型C中常量描述符和名称相符的方法，并校验访问权限。通过则返回方法的直接引用；否则返回非法访问异常；③若类型C中没有符合的方法，按继承关系从下至上对父类进行查找；仍没找到就抛出抽象方法异常错误。
方法重写的本质即调用invokevirtual把运行时常量池的符号引用解析为不同的直接引用。JVM通过在方法区中建立虚方法表来优化动态分派的频繁操作，通过方法表的索引替代元数据查找，直接对接地址入口。


(16)HashMap与HashTable的区别
HashMap和HashTable都提供键值映射服务，可以遍历视图，支持浅拷贝和序列化。不过HashTable已经被淘汰，不建议使用。
①时间上：HashMap出现得较晚；
②对外接口：两者都实现了Map,Clineable,Serializable三个接口。而HashMap继承自抽象类AbstractMap，HashTable继承自抽象类已经废弃的Dictionary；
③对Null：HashMap支持null键和null值，将null的hashCode定为0。HashTable遇到null会抛出NullPointerException异常。
**④初始容量上：HashTable是11，HashMap是16；HashMap的最大容量是2^30or1<<30(使用的类型为int，最高31位是符号位，容量不能为负，所以取不到)，默认负载因子都是0.75(泊松分布碰撞最小)；**
扩容阈值：threshold = newCap * loadFactor;占用容量大于阈值开始扩容
HashMap扩容源码：
# 小于2^30
static final int tableSizeFor(int cap){
    int n = cap - 1;
    n |= n >>> 1;
    n |= n >>> 2;
    n |= n >>> 4;
    n |= n >>> 8;
    n |= n >>> 16;
    return (n<0) ? 1 : (n >= MAXIMUM_CAPACITY) ? MAXIMUM_CAPACITY : n + 1；
}
# 大于2^30
此时resize()最后一段会将阈值设为Integer.MAX_VALUE(0x7FFFFFFF)，所以这是**HashMap的实际最大容量**

⑤HashTable每次扩容为2N+1(要求容量为素数或奇数)；HashMap为2N(且要求是2的幂)，目的是保证通过位操作模拟取余；
⑥数据结构：都创建了一个继承自Map.Entry的私有内部类，每个Entry对象存储hash表中的键值对。
Entry对象的四个属性：key--键；value--值；hash--键的hash值;entry--指向链表中的下一个Entry对象的引用；
JDK1.7的HashMap采用数组+链表实现，通过链表处理冲突，缺点是hash值相等的元素较多时查询效率会不断降低。
而JDK1.8的优化是，当桶中元素数目大于8时会将链表转为红黑树；
**⑦算法：hash函数和扩容算法不同
HashTable采用取模运算寻址 --> id = (hash & 0x7FFFFFFF) % tableLength，要求尽量使用素数、奇数容量使得取模哈希分布更加均匀。
证：
h=ag, m=bg, h=(a//b)m+res --> a=(a//b)b+(res//g)，左右都是整数，说明哈希和模有公约数g时，模的取值范围不是想象中的{0~m-1}，而是{0, k, ...,(m-1)g}，缩小了g倍，在处理等差数列等规则输入时可能会产生严重的哈希冲突，所以模设为素数(或公因子很少的数)就不会有这种事情发生了。
HashMap则是通过位运算代替取模运算寻址--> 数组地址id = (Map容量-1) & hashCode = hashCode % 2^n。因为位运算直接操作内存数据，不需要转成十进制再运算，速度更快。但由于要求哈希表大小为2的幂，因为2^n-1相当于取所有低位作为地址，尽可能打散了数据；若用15之类的容量，15-1=14=0x1110，最后一位永远不会用到，造成空间浪费。
**

⑧线程安全：
    HashTable加了synchronized锁，是线程安全的，但put,get效率会很差。
    HashMap不是线程安全的，一方面是多线程对同一位置的put操作，另一方面是扩容方法可能形成环导致卡死；解决方法可以使用线程安全的ConcurrentHashMap或Collections.synchronizedMap()代替。


(17)什么时候使用HashMap？它有什么特点？
HashMap时一个存储键值对的集合，是基于Map接口的实现。
特点：可以接受null键值；无序的；非同步的；HashMap存储着Entry(hash,key,value,next)对象。


(19)HashMap的put和get操作
①put：
首先根据元素hash值寻址。寻到址后判断数组是否为空，空就直接存进去，非空比对键值判断是否需要覆盖，不能覆盖就遍历链表/红黑树直到没有相同键值为止，此时再判断链表长度是否大于8，是的话就将链表转为红黑树。
首先调用hash() 根据key生成一个hash值(null键hash为0)；
然后调用putVal() 进行赋值，若表tab为空则调用resize()给tab和n赋值；
接着根据位运算寻址，找出数组下标；
若内容为空，就用newNode()创建entry对象并赋值；
若内容非空，且发生键值冲突，就直接替换原内容；
若发生位置冲突，则存进链表/红黑树中，若链表长度超出阈值，同时将其转变为树；
②get：



(20)简述Java中的深拷贝与浅拷贝，C++中的浅拷贝和深拷贝
(21)解释一下static块和static变量的执行顺序
(22)equals()的重写规则
(23)Java中如何创建线程？
(24)JDK1.8新特性

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

(9)more
功能：类似cat，以页显示方式阅读

(10)mv
功能：移动或重命名文件，若文件名相同可以覆盖

(11)rm
功能：删除文件，+ “-r” 删除目录；rm删除后的文件通常还能恢复

(12)tail
功能：查看文件末尾，+ “-f” 循环读数

(13)touch
功能：修改文件目录的时间属性，不存在则创建文件

(14)whereis
功能：只能搜索程序的二进制文件、man说明文件和源码文件。whereis和locate都基于内建数据库进行搜索的，比find遍历硬盘要快。

(15)which
功能：搜索系统命令是否存在PATH中，返回第一个结果
Summary：①which 查看PATH指令的可执行文件位置；②whereis 查看指令的文件位置；③locate 配合数据库查看文件位置；④find 通过硬盘查找文件；⑤>echo $PATH 查看环境变量


## 文件编辑命令
>Summary:
grep 适合单纯查找匹配文本；sed 适合编辑匹配到的文本；awk 适合对文本作格式化处理；

**(1.1)grep
功能：文本搜索指令--全局正则搜索(Global Regular Expression Print)，搜索文件或标准输入符合模式的文本，结果行送到标准输出。
格式：grep [option] pattern file/dir
常用参数：
-A n --after-context显示匹配字符后n行
-B n --before-context显示匹配字符前n行
-C n --context 显示匹配字符前后n行
-c --count 计算符合样式的列数
-i 忽略大小写
-l 只列出文件内容符合指定的样式的文件名称
-f 从文件中读取关键词
-n 显示匹配内容的所在文件中行数
-R 递归查找文件夹
-v 显示不包含匹配文本的行
正则表达式：
①[^]：匹配不在指定范围内的字符
②x\{m\}：重复字符x，m次
③x\{m,\}：重复字符x,至少m次
④x\{m,n\}  #重复字符x，至少m次，不多于n次
⑤\w：匹配文字和数字字符，也就是[A-Za-z0-9]  
⑥\W：\w的反置形式，匹配一个或多个非单词字符
⑦\b：单词锁定符


**(1.2)sed
功能：处理编辑一个或多个文件
格式：sed [-hnV] [-e<script>] [-f<script>] [文本文件]
    -e<script> 以指定的script处理输入文本
    -f<script> 以指定的script文件处理输入文本
script操作说明：①a--下一行拼接字符串；②c--取代n1，n2之间的行；③d--删除；④i--上一行插入字符串；⑤p--打印；⑤s--搭配正则模型替换；
用例：
①在第4行添加一行内容 >sed -e 4a\newLine testfile
②删除3行以后内容 >sed '3,$d' testfile
③新增隔换行内容，script文本内换行前加上'\' 
>sed '2a Drink tea or .../
>drink beer' testfile
④行的替换 >sed '2,5c No text' testfile
⑤删除包含内容项的行 >sed '/root/d' testfile
⑥执行{}组合命令 >sed '/root/{s/bash/blueshell/;p;q}'   #替换内容后显示，最后退出
⑦以行为单位进行部分数据替换 >sed 's/要被替换的字符串/新的字符串/g'
⑧-e表示多点编辑。>sd -e '3,$d' -e 's/bash/blueshell/'   #先删除，后替换
⑨直接修改文件内容(危险操作)：-i >sed -i '$a # This is the end.' testfile 给文件最后行加上内容


**(1.3)awk
功能：处理文本文件语言，强大文本分析工具
格式：awk [opt] '{[pattern] action}' var=value {filenames}
内建变量是awk预定义好的变量，主要如下：
①FS：字段分隔符，默认空格
②OFS：输出字段分隔符，默认空格
③RS：输入记录分隔符(换行符)
④ORS：输出换行符
⑤NF：当前行字段数(列数)
⑥NR：行号，文本行行号
⑦$n：第n个字段
⑧$0：所有记录行
运算符：
①赋值： = += -= /= %= ^= **=
②条件表达： ?:
③匹配、不匹配正则表达式：~ !~
④关系运算符：< <= > >= != ==
⑤连接： 空格
⑥求幂：^ ***
⑦字段引用：$
⑧包含：in
用例：
①每行按空格或tab分割，输出1、4项  >awk '{print $1,$4}' testfile
②指定多个内置变量(' ' ',')为分隔符  >awk -F'[ ,]' '{print $1,$2}' testfile
③设置变量  >awk -v a=1 '{print $1, $1+a}' testfile
④-f 参数调用awk脚本处理  >awk -f {awk脚本} testfile
⑤过滤第一列大于2的行  >awk '$1>2' testfile
⑥匹配正则表达式，~模式开始，/模式内容/  >awk '$2 ~/th/ {print $2,$4}' testfile
⑦


(2)wc
功能：统计指定文件的字节、行、字符、词数


## 磁盘管理命令
(1)cd
功能：路径切换
用法：①cd / 根目录；②cd ~ home目录；③cd - 进入上次工作路径

(2)df
功能：显示文件系统磁盘空间使用情况

(3)du
功能：查看文件、目录的磁盘空间使用情况

(4)ls
功能：查看文件信息
参数：-r 逆序排列；-t 修改时间排序；-S 大小排序；

(5)mkdir
功能：创建目录，-p 参数允许创建路径中的目录不存在，会自动创建补全


## 网络通讯命令
(1)ifconfig
功能：查看配置网络接口
用法：①查看所有网络接口>ifconfig -a；②启动或停止某个接口>ifconfig eth0 up/down

(2)iptables
功能：配置防火墙，开放端口
用法：
①拒绝IP912.168.1.101访问本机80端口>iptables -I INPUT -s 192.168.1.101 -p tcp --dport 80 -j REJECT；
②开启80端口(web默认对外端口)>iptables -A INPUT -p tcp --dport 80 -j ACCEP;
③保存配置>iptables save

(3)netstat
功能：显示网络状态
参数：-a 显示所有连线的Socket；-n 直接使用IP地址而不是域名服务器；-p 显示正在使用Socket的程序识别码和程序名；-l 显示监控中的服务器Socket
实操：
①统计当前进程连接数>nestat -an | grep ESTABLISHED | wc -l
②查看系统开启的端口>netstat -lnp
③查看连接到80端口状态链接的个数>netstat -an | grep ESTABLISHED

(4)ping
功能：使用ICMP传输协议检测远端主机的网络功能
使用：>ping -c 2 www.baidu.com

(5)telnet
功能：登入远端主机


## 系统管理命令
(1)date
功能：显示或设定系统时间
使用：显示下一天日期>date +%Y%m%d --date="+1 day"

(2)free
功能：显示内存使用情况，包括物理内存、交换区内存和内核缓冲区，默认kb单位
参数：-s<间隔秒> 持续间隔显示；-t 统计总和

(3)ps
功能：查看当前进程运行状态；动态查询结果使用>top；
进程状态码：①运行R；②中断S；③不可中断D；④僵死Z；⑤停止T；

(4)kill
功能：发送指定信号终止进程。默认信号-15，无法终止可用-9强制终止。

(5)top
功能：动态显示执行进程的信息。进程ID、内存占用率、CPU占用率。支持交互命令。
前五行显示信息：
①任务队列信息：当前系统时间、系统持续运行时间、登录用户数、load average--1分钟、5分钟、15分钟的负载情况（除以逻辑CPU大于5表明超负荷运转）；
②进程情况：总任务数以及各状态任务数统计信息；
③cpu占用百分比状态信息：us--用户空间、sy--内核空间、ni--改变过优先级的进程、id--空闲CPU、wa--IO等待、hi--硬中断、si--软中断；
④内存状态：total--总物理内存、used--使用中内存、free--空闲内存、buffers--缓存内存；
⑤swap交换区信息：total、used、free、cached
进程状态监控：PR--进程优先级、NI--负值表高优先级，正值表低优先级。


## 备份压缩命令
(1)bzip2
用法：①创建.bz2压缩文件 >bzip2 _filename_；②解压.bz2文件 >bzip2 -d _filename_

(2)gzip
用法：①创建.gz文件 >gzip _filename_；②解压.gz文件 >gzip -d _filename_；③显示压缩比率 >gzip -l _filename_

(3)tar
功能：tar本身只有打包功能，压缩及解压是调用其他功能完成的。
参数：①-c 建立新压缩文件；②-f 指定压缩文件；③-x 解压；④-u 添加更改了和现有的文件到压缩包；⑤-z gzip压缩；⑥-j bzip2压缩

(4)unzip
功能：①解压zip文件 >unzip _filename_；②查看zip文件内容 >unzip -l _filename_


#### Base/编程算法
# ---------------------------------------------
### 1.排序算法
排序本质就是消除逆序，随机数组的逆序数是O(N^2)级别的，采用交换相邻元素的规则一次只能消除一个逆序数，这是冒泡、插入排序不能突破O(N^2)下界的原因。交换相隔比较远的元素能消除更多的逆序，这就是希尔、快排、堆排等改进算法能提升的关键。
稳定性定义：每次排序前后两个数的相对位置不变则算法稳定

1.冒泡排序 -- TC:O(N^2), SC:O(1), 稳定
步骤：指针不断右移，每次修正一对元素，最后一次修正交换的位置表示后面的元素已正确排序；重复直至没有元素交换发生。
源码：
def bubbleSort(nums):
    for i in range(len(nums)-i):
        for j in range(1, len(nums)):
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
    for i in range(1, len(nums)):
        insertIndex = i-1
        while insertIndex >= 0 and nums[insertIndex] > nums[insertIndex+1]:
            nums[insertIndex+1] = nums[insertIndex]
            insertIndex -= 1
    return nums

4.希尔排序 -- TC:O(NlogN), SC:O(1), 不稳定
步骤：插入排序的改进版，由于有剪枝技巧，插入排序在几乎排好序的数组中效率高，TC能达到O(N)。但对于一般分布的数据是低效的，一次遍历只移动一位。
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
流程：递出过程--数组的不断二分；归来过程--数组的不断排序合并
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
        bucket[arr[i]] += 1

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


### 2.树
(1)树节点的定义：
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

(2)先序遍历：
def preorderTraversal(root):    # 递归实现
    res = []
    if not root:
        return res
    res.append(root.val)
    res += preorderTraversal(root.left)
    res += preorderTraversal(root.right)
    return res

def preorderTraversal(root): 	# 迭代实现
    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        if not node:
            continue
        res.append(node.val)
        stack.append(node.right)
        stack.append(node.left)
    return res

## DFS
(3)二叉树最大深度
def maxDepth(root):
    if not root:
        return 0
    return max(maxDepth(root.left)+1, maxDepth(root.right)+1)

(4)二叉树镜像
def mirrorTree(root):
    if root:
        root.left, root.right = mirrorTree(root.right), mirrorTree(root.left)
        return root
    else:
    	return

(5)**对称二叉树
def isSymmetric(root):
    if not root:
        return True
    return subMirror(root.left, root.right)

def subMirror(root1, root2):
    if not root1 and not root2:
        return True
    elif not root1 or not root2:
        return False
    elif root1.val != root2.val:
        return False
    # 可拆分为两子树的子问题
    return subMirror(root1.left, root2.right) and subMirror(root1.right, root2.left)

(6)路径总和
# Version1
# 嵌套递归查询路径和
global res = []
global candidSolution = []
def pathSum(root, sum):
	if not root:
		return res
	searchPath(root, sum)
	searchPath(root.left, sum)			# 嵌套搜寻不同节点
	searchPath(root.right, sum)


def searchPath(node, target): 			# 搜寻以node为起点的子路径
	if not node:
		return roads
	candidSolution.append(node.val)		# 维护当前路径
	target -= node.val
	if target == 0:
		res.append(candidSolution)

	searchPath(node.left, target)
	searchPath(node.right, target)
	del candidSolution[-1]				# 搜寻完本层要弹出当前节点回溯父节点的状态
	
# Version2
# 字典+前缀和+回溯
# 路径和一次遍历算完，减轻计算冗余
# 不过由于该方法是快速搜索优化，适合统计数量，不适合统计路径方案
def pathSum(root, sum):
	mp = {}
	mp[0] = 1
	res = 0

	def dfs(root, pathSum, target):
		if not root:
			return
		pathSum += root.node
		cnt = 0 if (pathSum-target) not in mp.keys() else mp[pathSum-target]
		mp[pathSum] = 1 if pathSum not in mp.keys() else mp[pathSum]+1
		cnt += dfs(root.left, pathSum, target)
		cnt += dfs(root.right, pathSum, target)
		mp[pathSum] -= 1 	# 遍历完当前节点要回溯
		return cnt

	res = dfs(root, 0, sum)
	return res

(7)重建二叉树
def buildTree(preorder, inorder):
	N = len(preorder)
	if N == 0:
		return None
	root = TreeNode(preorder[0])
	id = inorder.index(preorder[0])
	Nleft = id
	Nright = N-1-id
	root.left = buildTree(preorder[1:id+1], inorder[:id])
	root.right = buildTree(preorder[N-Nright:], inorder[id+1:])
	return root

(8)搜索最近公共祖先
def LCA(root, p, q):
    # 两点要么呈祖孙节点关系，要么呈左右子节点关系
    # 利用递归层层归来的特性
    # 有找到就返回点，找不到就返回空
    if not root or root == p or root == q:
        return root

    left = LCA(root.left, p, q)
    right = LCA(root.right, p, q)
    if left and right:
        return root

    return left if left else right

(9)序列化和反序列化
from collections import deque
class Codec:
    def serialize(self, root):
        if not root: return None
        queue = deque()
        queue.append(root)
        res = ""
        while queue:
            node = queue.popleft()
            if node:
                res += str(node.val) + ","
                queue.append(node.left)
                queue.append(node.right)
            else:
                res += "None,"
        return res

    def deserialize(self, data):
        if not data: return None
        data = data.split(",")
        root = TreeNode(data.pop(0))
        queue = [root]
        while queue:
            node = queue.pop(0)
            if data:
                val = data.pop(0)
                if val != "None":
                    node.left = TreeNode(val)
                    queue.append(node.left)
            if data:
                val = data.pop(0)
                if val != "None":
                    node.right = TreeNode(val)
                    queue.append(node.right)
        return root