// Version 0
// 使用LinkedHashMap(或Python 的OrderedDict)数据结构实现
class LRUCache extends LinkedHashMap<Integer, Integer>{
	private int capacity;

	public LRUCache(int capacity){
		super(capacity, 0.75F, true);
		this.capacity = capacity;
	}

	public int get(int key){
		return super.getOrDefault(key, -1);
	}

	public void put(int key, int value){
		super.put(key, value);
	}

	@Override
	protected boolean removeEldestEntry(Map.Entry<Integer, Integer> eldest){
		return size() > capacity;
	}
}


// Version 1
// 哈希表 + 双向链表实现
// 对于get，判断key是否存在--存在即移动到链表头部；
// 对于put，判断key是否存在--存在就更新哈希表并移动到链表头部；
// 							不存在就创建新节点添加到链表头，进行容量判定；
// 			第二层的容量判断--超出容量就删除链表的尾部节点以及哈希表的对应项；
public class LRUCache{
	class DLinkedNode{
		int key;
		int value;
		DLinkedNode pre;
		DLinkedNode next;
		public DLinkedNode(){}
		public DLinkedNode(int _key, int _value){
			key = _key;
			value = _value;
		}
	}

	private Map<Integer, DLinkedNode> cache =  new HashMap<>();
	private int size;
	private int capacity;
	private DLinkedNode head, tail;

	public LRUCache(int capacity){
		this.size = 0;
		this.capacity = capacity;
		// 使用伪头部和伪尾部节点
		head = new DLinkedNode();
		tail = new DLinkedNode();
		head.next = tail;
		tail.pre = head;
	}

	public int get(int key){
		DLinkedNode node = cache.get(key);
		if(node==null){
			return -1;
		}
		moveToHead(node);
		return node.value;
	}

	public void put(int key, int value){
		DLinkedNode node = cache.get(key);
		if(node==null){
			node = new DLinkedNode(key, value);
			cache.put(key, node);
			addToHead(node);
			++size;
			if(size > capacity){
				DLinkedNode tail = removeTail();
				cache.remove(tail.key);
				--size;
			}
		}else{
			node.value = value;
			moveToHead(node);
		}
	}

	private void addToHead(DLinkedNode node){
		node.pre = head;
		node.next = head.next;
		head.next.pre = node;
		head.next = node;
	}

	private void moveToHead(DLinkedNode node){
		removeNode(node);
		addToHead(node);
	}

	private DLinkedNode removeTail(){
		DLinkedNode res = tail.pre;
		removeNode(res);
		return res;
	}

	private void removeNode(DLinkedNode node){
		node.next.pre = node.pre;
		node.pre.next = node.next;
	}
}