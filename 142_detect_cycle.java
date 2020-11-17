// Version 0
// TC:O(N), SC:O(N)
// Hashset
/**
 * class ListNode{
 * 	int val;
 *  ListNode next;
 *  ListNode(int x){
 *  	val = x;
 *  	next = null;
 *  }	
 * }
 */

public class Solution{
	public ListNode detectCycle(ListNode head){
		ListNode pos = head;
		Set<ListNode> visited = new HashSet<>();
		while(pos != null){
			if(visited.contains(pos)){
				return pos;
			}else{
				visited.add(pos);
			}
			pos = pos.next;
		}
		return null;
	}
}


// Version 1
// double pointer
// TC: O(N), SC: O(1)
public class Solution{
	public ListNode detectCycle(ListNode head){
		if(head==null || head.next==null){
			return null;
		}
		// init
		ListNode slow = head, fast = head;

		// traverse 1st
		while(fast!=null){
			slow = slow.next;
			if(fast.next==null){
				return null;
			}else{
				fast = fast.next.next;
			}
			if(fast==slow){		// 2nd traverse, fast move 1 step this round
				fast = head;
				while(fast!=slow){
					fast = fast.next;
					slow = slow.next;
				}
				return fast;
			}
		}
		return null;
	}
}