// Version 0
// 下标错误
class Solution{
	public int peakIndexInMountainArray(int[] arr){
		// init
		int N = arr.length;
		int l = 0;
		int r = N-1;
		int mid = (l+r) / 2;
		int lmid = (l+mid) / 2;
		int rmid = (mid+r) / 2;

		// double binary search
		while(r-l+1>4){
			// divide by peak location
			if(arr[l]<arr[lmid] && arr[lmid]>arr[mid]){
				r = mid-1;
				l++;
			}else if(arr[lmid]<arr[mid] && arr[mid]>arr[rmid]){
				l = lmid;
				r = rmid-1;
			}else if(arr[mid]<arr[rmid] && arr[rmid]>arr[r]){
				l = mid+1;
				r--;
			}

			// update var
			mid = (l+r) / 2;
			lmid = (l+mid) / 2;
			rmid = (mid+r) / 2;
		}

		// peak locate
		int res = l;
		int[] candid = {l, lmid, mid, rmid, r};
		for(int i:candid){
			if(arr[i] > arr[res]){
				i = res;
			}
		}
		return res;
	}
}


// Version 1
// TC:O(logN), SC:O(1)
class Solution{
	public int peakIndexInMountainArray(int[] A){
		int l = 0, h = A.length-1;
		while(l<h){
			int mid = (l+h)/2;
			if(A[mid]<A[mid+1]){
				l = mid+1;
			}else{
				h = mid;
			}
		}
		return l;
	}
}
