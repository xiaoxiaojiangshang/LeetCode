/*
    Author: jgz
    Date: 2018/7/17 11:07:58
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "F:\\leetcode\\DealTxt\\preDealTxt.cpp"

/* 核心是判断所要查找的数字在left or right
找到有序的一边，判断target是否 在其范围，否则在另一边
*/
int search(int* nums, int numsSize, int target) {
	int left = 0,right = numsSize-1;
	while(left<=right) {
		int mid = (left+right)/2;
		if(nums[mid]==target)
			return mid;
		if(nums[mid]<nums[right]) { // right order
			if(nums[mid]<target&&nums[right]>=target)
				left = mid +1;
			else right = mid -1;
		} else {
			if(nums[mid]>target&&nums[left]<=target)
				right = mid -1;
			else left = mid +1;
		}
	}
	return -1;
}

int main() {
	const char *fname="dataIn.txt";
	int **dataArray = (int **)malloc(sizeof(int*)*MAXN);
	int rows=DealTxt(fname,dataArray);
	disp(dataArray,rows);
	for(int i=0; i<rows; i++) {
		printf("ans=%d\n",search(&dataArray[i][1],dataArray[i][0],5));
	}
	
	return 0;
}

