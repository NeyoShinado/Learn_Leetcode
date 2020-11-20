# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Version1 
# Brute Force
# 爆栈了
class Solution:
	def flatten(self, root: TreeNode) -> None:
		"""
		Do not return anything, modify root in-place instead.
		"""
		if root:
			root.next = root.right
			tree_link(root, root.left)
		

def tree_link(parent, tree): 
	tree.next = tree.right
	if tree.left:
		tree.right = tree_link(tree, tree.left)
		del tree.left
	else:
		if tree.next:
			tree.right = tree_link(tree, tree.next)
			del tree.next
		else:
			if parent.next:
				parent.right = tree_link(parent, parent.next)
				del parent.next


## Java
# Version 2
class Solution{
	ListNode res = new ListNode();

    public class ListNode{
        int val;
        ListNode next;
        ListNode(){};
        ListNode(int val){this.val = val;}
        ListNode(int val, ListNode next){
            this.val = val;
            this.next = next;
        }
    }

	public void flatten(TreeNode root){
        ListNode start = res;
		dfs(root);
		return start;
	}

	private void dfs(TreeNode node){
		if(node != null){
			res.next = new ListNode(node.val);
            res = res.next;
		}
		if(node.left != null){
			flatten(node.left);
		}
		if(node.right != null){
			flatten(node.right);
		}
	}
}


# Version 3
# 前序遍历
# 二叉树展开会破坏二叉树结构，因此先前序遍历获得节点修改的顺序
# 再按顺序修改各节点的左右子节点信息
# TC: O(N), SC: O(N)
# 递归实现
class Solution{
	public void flatten(TreeNode root){
		List<TreeNode> list = new ArrayList<TreeNode>();
		preorderTraversal(root, list);
		int size = list.size();
		for(int i=1;i<size; i++){
			TreeNode prev = list.get(i-1), curr=list.get(i);
			prev.left = null;
			prev.right = curr;
		}
	}

	public void preorderTraversal(TreeNode root, List<TreeNode> list){
		if(root != null){
			list.add(root);
			preorderTraversal(root.left, list);
			preorderTraversal(root.right, list);
		}
	}
}
# 迭代实现(通过栈)
# 前序遍历中，子树的根节点遍历左右子节点类似于递出和归来的结构
# 且左右子树的遍历顺序有明显的后进（遍历左）先出（遍历右）的结构
# 故可用栈存储待回归的节点 + 一层循环负责深度遍历另一层循环负责切换子树(宽度遍历)
# 通过迭代实现递归遍历
class Solution{
	public void flatten(TreeNode root){
		List<TreeNode> list = new ArrayList<TreeNode>();
		Deque<TreeNode> stack = new LinkedList<TreeNode>();
		TreeNode node = root;
		while(node!=null || !stack.isEmpty()){
			while(node!=null){
				list.add(node);
				stack.push(node);
				node = node.left;
			}
			node = stack.pop();
			node = node.right;
		}
		int size = list.size();
		for(int i=1;i<size;i++){
			TreeNode prev = list.get(i-1), curr = list.get(i);
			prev.left = null;
			prev.right = curr;
		}
	}
}


# Version 4
# 节点遍历与子树展开同步进行的难点在于，展开二叉树会破坏结构
# 左节点可以直接作为next，但右节点何时连接是问题
# 所以要同时展开，就要同步储存子节点的信息，按右节点左节点的顺序入栈
# 该方法若使用递归比较麻烦，因为递归是隐性地使用栈，递归完成前并不知道二叉树的规模，同步合成右子树需要借鉴查找前驱节点的方式
# 迭代实现
class Solution{
	public void flatten(TreeNode root){
		if(root==null){
			return;
		}
		Deque<TreeNode> stack = new LinkedList<TreeNode>();
		stack.push(root);
		TreeNode prev = null;
		while(!stack.isEmpty()){
			TreeNode curr = stack.pop();
			if(prev!=null){
				prev.left = null;
				prev.right = curr;
			}
			TreeNode left = curr.left, right = curr.right;
			if(right!=null){
				stack.push(right);
			}
			if(left!=null){
				stack.push(left);
			}
			prev = curr;
		}
	}
}

# 递归实现
class Solution {
    public void flatten(TreeNode root) {
        if(root == null){
            return;
        }

        TreeNode left = root.left;
        TreeNode right = root.right;

        root.left = null;
        root.right = null;

        flatten(left);
        flatten(right);

        root.right = left;
        TreeNode temp  = root;
        # 找到右子树的接入点
        while(temp.right != null){
            temp = temp.right;
        }
        temp.right = right;
    }
}


# Version 5
# 查找前驱节点
# 左子树的最后一个节点是访问右节点的前驱节点
# TC: O(N), SC: O(1)
class Solution{
	public void flatten(TreeNode root){
		TreeNode curr = root;
		while(curr!=null){
			if(curr.left!=null){
				TreeNode next = curr.left;
				TreeNode predecessor = next;
				# 查找前驱节点
				while(predecessor.right!=null){
					predecessor = predecessor.right;
				}
				predecessor.right = curr.right;
				curr.left = null;
				curr.right = next;
			}
			curr = curr.right;
		}
	}
}