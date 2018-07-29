/*
    Author: jgz
    Date: 2018/7/27 19:50:58
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "F:\\leetcode\\DealTxt\\preDealTxt.cpp"
void swap(int*a,int*b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}
void backTrack(int **ret,int *nums,int numsSize,int cur,int* returnSize) {
	if(cur==numsSize) {
		ret[*returnSize] =(int*) malloc(sizeof(int)*numsSize);
		memcpy(ret[*returnSize],nums,sizeof(int)*numsSize);
		(*returnSize)++;
		return ;
	} else {
		for(int i=cur; i<numsSize; i++) {
			swap(&nums[cur],&nums[i]);
			backTrack(ret,nums,numsSize,cur+1,returnSize);
			swap(&nums[cur],&nums[i]);
		}
	}
}

int** permute(int* nums, int numsSize, int* returnSize) {
	int size =1;
	for(int i=2; i<=numsSize; i++) {
		size =size*i;
	}
	int **ret =(int**)malloc(sizeof(int*)*(size+1));
	memset(ret,0,sizeof(int*)*(size+1));
	* returnSize = 0; 
	backTrack(ret,nums,numsSize,0,returnSize);
	return ret;
}
void disp(int **ret,int numsSize,int returnSize) {

	for(int i=0; i<returnSize; i++) {
		for(int j=0; j<numsSize; j++)
			printf("%d ",ret[i][j]);
		printf("\n");
	}
}
int main() {
	const char *fname="dataIn.txt";
	int **dataArray = (int **)malloc(sizeof(int*)*MAXN);
	int rows=DealTxt(fname,dataArray);
	FILE *fp;
	int returnSize;
	if((fp=fopen(fname,"r"))==NULL) {
		printf("打开文件%s错误\n",fname);
		return NULL;
	}
	for(int i=0; i<rows; i++) {
		int **ret = permute(&dataArray[i][1],dataArray[i][0],&returnSize) ;
//		printf("%d %d %d",ret[0][0],ret[0][1],ret[0][2]);
		disp(ret,dataArray[i][0],returnSize);
	}
	return 0;
}

