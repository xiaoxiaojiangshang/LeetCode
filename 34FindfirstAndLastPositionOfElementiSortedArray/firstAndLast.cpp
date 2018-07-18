/*
    Author: jgz
    Date: 2018/7/17 16:58:52
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "F:\\leetcode\\DealTxt\\preDealTxt.cpp"
int* searchRange(int* nums, int numsSize, int target, int* returnSize) {
	* returnSize = 2;
	int * ret =(int*) malloc (sizeof(int)*2);
	ret[0]=-1,ret[1]=-1;
	if(numsSize==0) return ret;
	int l = 0,mid,r = numsSize - 1;
	while(l<r) {
		mid = (l+r)/2;
		if(nums[mid]<target)
			l = mid+1;
		else r = mid;
	}
	if(nums[l]!=target) return ret;
	else ret[0] = l;
	l = 0,r = numsSize - 1;
	while(l<r) {
		mid = (l+r)/2+1;// »úÖÇ 
		if(nums[mid]>target)
			r = mid -1;
		else l = mid;
	}
	ret[1] = r;
	return ret;
}
int main() {
	const char *fname="dataIn.txt";
	int **dataArray = (int **)malloc(sizeof(int*)*MAXN);
	int rows=DealTxt(fname,dataArray);
	int returnSize ;
	for (int i = 0; i<rows; i++) {
		int * ret = searchRange(&dataArray[i][1],dataArray[i][0],8,&returnSize);
		printf(" %d %d\n",ret[0],ret[1]);
	}
   return 0;
}

