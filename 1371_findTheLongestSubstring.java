// Version 1
// 取余累加更新编码

import java.util.*;

class Solution{
    public int findTheLongestSubstring(String s){
        // init
        int N = s.length();
        int[] cnt = {0, 0, 0, 0, 0};
        int code = 0;
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        int dp = 0;
        int res = 0;
        map.put(0, 0);

        // traverse
        for(int i=0;i<N;i++){
            // candid chars
            if(s.charAt(i) == 'a'){
                cnt[0] += 1;
            }else if(s.charAt(i) == 'e'){
                cnt[1] += 1;
            }else if(s.charAt(i) == 'i'){
                cnt[2] += 1;
            }else if(s.charAt(i) == 'o'){
                cnt[3] += 1;
            }else if(s.charAt(i) == 'u'){
                cnt[4] += 1;
            }

            // cal code
            code = (cnt[0]%2)*1 + (cnt[1]%2)*2 + (cnt[2]%2)*4 + (cnt[3]%2)*8 + (cnt[4]%2)*16;
            if(map.containsKey(code)){
                res = Math.max(i+1 - map.get(code), res);
            }else{
                map.put(code, i+1);
            }
        }
    return res;
    }
}


// Version 2
// 直接位运算更新编码
// TC: O(N), SC: O(2^M) 
class Solution{
    public int findTheLongestSubstring(String s){
        int N = s.length();
        int[] pos = new int[1<<5];  // map
        Arrays.fill(pos, -1);       
        int ans = 0, status = 0;    
        pos[0] = 0;
        for(int i=0;i<N;i++){
            char ch = s.charAt(i);
            if(ch == 'a'){
                status ^= (1<<0);
            }else if(ch == 'e'){
                status ^= (1<<1);
            }else if(ch == 'i'){
                status ^= (1<<2);
            }else if(ch == 'o'){
                status ^= (1<<3);
            }else if(ch == 'u'){
                status ^= (1<<4);
            }

            if(pos[status] >= 0){
                res = Math.max(res, i+1-pos[status]);
            }else{
                pos[status] = i+1;
            }
        }
        return res;
    }
}