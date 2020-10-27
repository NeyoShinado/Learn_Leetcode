/**
 Definition for singly-linked list.
 public class ListNode{
    int val;
    ListNode next;
    ListNode(){}
    ListNode(int val){this.val = val;}
    ListNode(int val, ListNode next){
        this.val = val;
        this.next = next;
    }
 }
 **/

/*
// Version 0
// Merge Sort
// 直接合并思路，not pass
class Solution{
    public ListNode sortList(ListNode head){
        // init
        int N = 0;
        ListNode tmp = head;
        while(tmp != null){
            N += 1;
            tmp = tmp.next;
        }
        int m = 1;

        if(N <= 1){
            return head;
        }
        // merge
        while(m <= N/2){
            head = listMergeSort(head, m, N);
            m *= 2;
        }
        return head;
    }

    private ListNode listMergeSort(ListNode l, int m, int cnt){
        int loff = m;
        int roff = m;
        ListNode r = l;
        r = nextM(r, m);
        ListNode start;
        ListNode curNode;
        if(r.val < l.val){
            start = r;
        }else{
            start = l;
        }
        curNode = start;

        // sort
        while(cnt > 0){
            if(cnt == 2*m+1){       // last update
               roff = m+1;
            }else{
                roff = m;
            }
            loff = m;
            l = r;                // left right init
            r = nextM(r, roff);

            while(loff < m || roff < m){
                if(l.val < r.val){
                    curNode.next = l;
                    l = l.next;
                    curNode = curNode.next;
                    loff -= 1;
                    cnt -= 1;
                }else{
                    curNode.next = r;
                    r = r.next;
                    curNode = curNode.next;
                    roff -= 1;
                    cnt -= 1;
                }
            }
            if(loff == 0){      // l sorted
                curNode.next = r;
                r = nextM(r, roff+1);
                curNode = nextM(curNode, roff);
                cnt -= roff;
            }else{              // r sorted
                curNode.next = l;
                l = nextM(l, loff);
                curNode = nextM(curNode, loff);
                cnt -= loff;
            }
        }
        return start;
    }

    private ListNode nextM(ListNode node, int m){
        while(m > 0){
            node = node.next;
            m -= 1;
        }
        return node;
    }
}


// Version 1
// 递归实现
// TC: O(NlogN), SC: O(N)
class Solution{
    public ListNode sortList(ListNode head){
        if(head==null || head.next == null){
            return head;
        }
        ListNode fast = head.next, slow = head;
        while(fast!=null && fast.next!=null){
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode tmp = slow.next;
        slow.next = null;
        // 划分递出
        ListNode left = sortList(head);
        ListNode right = sortList(tmp);
        ListNode h = new ListNode(0);
        ListNode res = h;
        // 合并归来
        while(left!=null && right!=null){
            if(left.val < right.val){
                h.next = left;
                left = left.next;
            }else{
                h.next = right;
                right = right.next;
            }
            h = h.next;
        }
        h.next = left!=null ? left:right;
        return res.next;
    }
}
**/


// Version 2
// 维护两倍间隔，自下向上直接合并
// 直接合并需要考虑较复杂的长度边界情况
// 同时还要处理链表不擅长的索引查找和区间截取操作，和繁琐的指针操作比较接近
// TC: O(NlogN), SC: O(1)
class Solution{
    public ListNode sortList(ListNode head){
        // init
        ListNode h = head;                  
        int N = 0;
        int m = 1;

        while(h != null){
            h = h.next;
            N += 1;
        }
        ListNode res = new ListNode(0);      // 链表开头标记不能丢失
        res.next = head;

        // merge list for different intv
        while(m < N){
            ListNode curNode = res;         // 记录将要更新的当前节点cur
            h = res.next;                   // 记录更新区间的tail
            while(h != null){
                ListNode l = h;
                int i = m;
                while(i!=0 && h!=null){
                    h = h.next;
                    i -= 1;
                }
                if(i != 0){
                    break;      // 当前间隔下没有r配对合并，虽然今轮不会合并到链表中，也会在下一轮划分中合并
                }
                ListNode r = h;
                i = m;
                while(i!=0 && h!=null){
                    h = h.next;
                    i -= 1;
                }
                int c1 = m;
                int c2 = m-i;
                while(c1!=0 && c2!=0){
                    if(l.val < r.val){
                        curNode.next = l;
                        l = l.next;
                        c1 -= 1;
                    }else{
                        curNode.next = r;
                        r = r.next;
                        c2 -= 1;
                    }
                    curNode = curNode.next;
                }
                curNode.next = (c1!=0) ? l : r;
                while(c1>0 || c2>0){
                    curNode = curNode.next;
                    c1 -= 1;
                    c2 -= 1;
                }
                curNode.next = h;
            }
            m *= 2;
        }
        return res.next;
    }
}