/*
    Name:
    Copyright:jgz
    Author: jgp
    Date: 2018/7/28 12:30:46
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
bool exist(int **ret,int numsSize,int returnSize,int *nums) {
	for(int i=0; i<returnSize; i++) {
		if(memcmp(ret[i],nums,sizeof(int)*numsSize)==0) {
			return false;
		}
	}
	return true;
}
void backTrack(int **ret,int *nums,int numsSize,int cur,int* returnSize) {
	if(cur==numsSize&&exist(ret,numsSize,*returnSize,nums)) {
		ret[*returnSize] =(int*) malloc(sizeof(int)*numsSize);
		memcpy(ret[*returnSize],nums,sizeof(int)*numsSize);
		(*returnSize)++;
		return ;
	} else {
		for(int i=cur; i<numsSize; i++) {
			if(i>cur&&(nums[i]==nums[i-1]||nums[i]==nums[cur]))
//			if(i>cur&&(nums[i]==nums[cur]))
				continue;
			swap(&nums[cur],&nums[i]);
			backTrack(ret,nums,numsSize,cur+1,returnSize);
			swap(&nums[cur],&nums[i]);
		}
	}
	return ;
}
//void backTrack(int **ret,int *nums,int numsSize,int cur,int* returnSize,int *visited,int min) {
//	if(cur==numsSize) {
//		ret[*returnSize] =(int*) malloc(sizeof(int)*numsSize);
//		memcpy(ret[*returnSize],nums,sizeof(int)*numsSize);
//		(*returnSize)++;
//		return ;
//	} else {
//		for(int i=cur; i<numsSize; i++) {
//			if(i<cur&&visited[nums[i]-min])
//				continue;
//			visited[nums[i]-min]=1;
//			swap(&nums[cur],&nums[i]);
//			backTrack(ret,nums,numsSize,cur+1,returnSize,visited,min);
//			swap(&nums[cur],&nums[i]);
//			visited[nums[i]-min]=0;
//		}
//	}
//	return ;
//}
int** permuteUnique(int* nums, int numsSize, int* returnSize) {
	int size =1;
	for(int i=2; i<=numsSize; i++) {
		size =size*i;
	}
	int **ret =(int**)malloc(sizeof(int*)*(size+1));
	memset(ret,0,sizeof(int*)*(size+1));
	//sort and get min
	int min= nums[0],max = min= nums[0];
	for(int i=0; i<numsSize; i++) {
		if(nums[i]<min)
			min = nums[i];
		else max = nums[i];
		for(int j=i+1; j<numsSize; j++) {
			if(nums[i]>nums[j])
				swap(&nums[i],&nums[j]);
		}
	}
	* returnSize = 0;
//	int *visit = (int *)malloc(sizeof(int)*(max-min+1));
//	memset(visit,0,sizeof(int)*(max-min+1));
//	backTrack(ret,nums,numsSize,0,returnSize,visit,min);
	backTrack(ret,nums,numsSize,0,returnSize);
	return ret;
}
//void reduDup(int **ret,int numsSize,int returnSize) {
//	int count = 0;
//	for(int i=0; i<returnSize; i++) {
//		for(int j=i+1; j<returnSize; j++) {
//			if(memcmp(ret[i],ret[j],sizeof(int)*numsSize)==0) {
//				for(int k=0; k<numsSize; k++)
//					printf("%d ",ret[i-2][k]);
//				printf("\n");
//				for(int k=0; k<numsSize; k++)
//					printf("%d ",ret[i-1][k]);
//				printf("\n");
//				for(int k=0; k<numsSize; k++)
//					printf("%d ",ret[i][k]);
//				printf("\n\n");
//				for(int k=0; k<numsSize; k++)
//					printf("%d ",ret[j-2][k]);
//				printf("\n");
//				for(int k=0; k<numsSize; k++)
//					printf("%d ",ret[j][k]);
//				printf("\n");
//				for(int k=0; k<numsSize; k++)
//					printf("%d ",ret[j][k]);
//				printf("i==%d,j==%d\n\n",i,j);
//				count++;
//			}
//		}
//	}
//	printf("%d",count);
//}
void disp(int **ret,int numsSize,int returnSize) {
	for(int i=0; i<returnSize; i++) {
		if(i==551 or i==568) printf("\ndebug\n");
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
		int **ret = permuteUnique(&dataArray[i][1],dataArray[i][0],&returnSize) ;
		disp(ret,dataArray[i][0],returnSize);
//		reduDup(ret,dataArray[i][0],returnSize);
		printf("%d\n\n",returnSize);
	}
	return 0;
}
