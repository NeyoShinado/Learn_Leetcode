// Version 1
// Trie 选用链表结构实现

class TrieNode{
	// links to child node
	private TrieNode[] links;
	private final int N = 26;
	private boolean End;

	public TrieNode(){
		links = new TrieNode[N];
	}

	public boolean containsKey(char ch){
		return links[ch-'a'] != null;
	}

	public TrieNode get(char ch){
		return links[ch-'a'];
	}

	public void put(char ch, TrieNode node){
		links[ch-'a'] = node;
	}

	/** SetEnd when it's wordEnd instead of prefixEnd */
	public void setEnd(){
		End = true;
	}

	public boolean isEnd(){
		return End;
	}
}

class Trie{

	private TrieNode root;
	/** Initialize Trie */
	public Trie(){
		root = new TrieNode();
	}

	/** Insert a word into trie */
	public void insert(String word){
		TrieNode node = root;
		for(int i=0;i<word.length();i++){
			char ch = word.charAt(i);
			if(!node.containsKey(ch)){
				node.put(ch, new TrieNode());
			}
			node = node.get(ch);
		}
		node.setEnd();
	}

	/** Search a prefix in trie */
	public TrieNode searchPrefix(String word){
		TrieNode node = root;
		for(int i=0;i<word.length();i++){
			char ch = word.charAt(i);
			if(node.containsKey(ch)){
				node = node.get(ch);
			}else{
				return null;
			}
		}
		return node;
	}

	/** Search a word in trie */
	public boolean search(String word){
		TrieNode node = searchPrefix(word);
		return node != null && node.isEnd();
	}

	/** Confirm if there is any word in the trie */
	public boolean startsWith(String prefix){
		TrieNode node = searchPrefix(prefix);
		return node != null;
		}
}

/**
 * test
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param1 = obj.search(word);
 * boolean param2 = obj.startsWith(prefix);
 */