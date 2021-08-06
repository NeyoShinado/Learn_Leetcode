/*public class ListNode{
	int val;
	ListNode next;
	ListNode(){};
	ListNode(int val){this.val = val;}
	ListNode(int val, ListNode next){this.val = val;this.next = next;}
}*/

// Version 0
// 顺序合并
// TC: O(k^2N), SC: O(1)
class Solution{
	public ListNode mergeKLists(ListNode[] lists){
		ListNode res = null;
		for (int i=0;i < lists.length; i++){
			res = mergeTwoLists(res, lists[i]);
		}
		return res;
	}

	public ListNode mergeTwoLists(ListNode a, ListNode b){
		if(a == null || b == null){
			return a != null ? a : b;
		}
		ListNode head = new ListNode(0);
		ListNode tail = head, aPtr = a, bPtr = b;
		while(aPtr != null && bPtr != null){
			if(aPtr.val < bPtr.val){
				tail.next = aPtr;
				aPtr = aPtr.next;
			}else{
				tail.next = bPtr;
				bPtr = bPtr.next;
			}
			tail = tail.next;
		}
		tail.next = (aPtr != null ? aPtr : bPtr);
		return head.next;
	}
}

// Version 1
// 分治合并
// TC: O(kNlogk), SC:O(logk)
class Solution{
	public ListNode mergeKLists(ListNode[] lists){
		return merge(lists, 0, lists.length-1);
	}

	public ListNode merge(ListNode[] lists, int l, int r){
		if(l == r){
			return lists[l];
		}
		if(l > r){
			return null;
		}
		int mid = (l+r) >> 1;
		return mergeTwoLists(merge(lists, l, mid), merge(lists, mid+1, r));
	}

	public ListNode mergeTwoLists(ListNode a, ListNode b){
		if(a == null || b == null){
			return a != null ? a : b;
		}
		ListNode head = new ListNode(0);
		ListNode tail = head, aPtr = a, bPtr = b;
		while(aPtr != null && bPtr != null){
			if(aPtr.val < bPtr.val){
				tail.next = aPtr;
				aPtr = aPtr.next;
			}else{
				tail.next = bPtr;
				bPtr = bPtr.next;
			}
			tail = tail.next;
		}
		tail.next = (aPtr != null ? aPtr : bPtr);
		return head.next;
	}
}


// Version 2
// 优先队列合并
// TC: O(), SC: O()
class Solution{
	class Status implements Comparable<Status>{
		int val;
		ListNode ptr;
		
		Status(int val, ListNode ptr){
			this.val = val;
			this.ptr = ptr;
		}

		public int compareTo(Status status2){
			return this.val - status2.val;
		}
	}

	PriorityQueue<Status> queue = new PriorityQueue<Status>();

	public ListNode mergeKLists(ListNode[] lists){
		for(ListNode node: lists){
			if(node != null){
				queue.offer(new Status(node.val, node));
			}
		}
		ListNode head = new ListNode(0);
		ListNode tail = head;
		while(!queue.isEmpty()){
			Status f = queue.poll();
			tail.next = f.ptr;
			tail = tail.next;
			if(f.ptr.next != null){
				queue.offer(new Status(f.ptr.next.val, f.ptr.next));
			}
		}
		return head.next;
	}
}