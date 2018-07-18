/*
    Author: jgz
    Date: 2018/7/18 10:16:02
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "F:\\leetcode\\DealTxt\\preDealTxt.cpp"
int searchInsert(int* nums, int numsSize, int target) {
    int l = 0,mid,r = numsSize - 1;
	while(l<=r) {
		mid = (l+r)/2;
		if (nums[mid]==target) return mid;
		if(nums[mid]<target)
			l = mid+1;
		else r = mid-1;
	}
	return l; 
}
int main() {
	const char *fname="dataIn.txt";
	int **dataArray = (int **)malloc(sizeof(int*)*MAXN);
	int rows=DealTxt(fname,dataArray);
	int returnSize ;
	for (int i = 0; i<rows; i++) {
		int ret = searchInsert(&dataArray[i][1],dataArray[i][0],2);
		printf("%d\n",ret);
	}
   return 0;
}

