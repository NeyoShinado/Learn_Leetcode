// Version 1
// 二分求幂
// TC: O(N), SC: O(N)

class Solution{
    int base = 1337;
    public int superPow(int a, int[] b) {
        LinkedList<Integer> list = new LinkedList<>();
        for (int i : b) {
            list.add(i);
        }
        return superPowList(a, list);
    }

    private int superPowList(int a, LinkedList<Integer> list){
        // calculate super power
        if(list.isEmpty()){
            return 1;
        }
        int cur = list.peekLast();
        list.pollLast();
        int part1 = power(a, cur);
        int part2 = power(superPowList(a, list), 10);
        return (part1 * part2)%base;
    }

    // optimized power operater
    private int power(int x, int k){
        if(k == 0){
            return 1;
        }
        if((k & 1) == 1){
            return (x%base * power(x, k-1))%base;
        }else{
            int subTerm = power(x, k/2);
            return (subTerm * subTerm)%base;
        }
    }
}


// Version 2
// 欧拉公式会比Version 1在常数级上有优势