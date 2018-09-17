/*
    Name:
    Copyright:jgz
    Author: jgp
    Date: 2018/8/31 12:41:34
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "F:\\leetcode\\DealTxt\\preDealTxt.cpp"

//贪心算法 
int jump(int* nums, int numsSize) {
   if(numsSize<=1) return 0;
   int level = 0;
   int curr=0,currTemp,currMaxTemp=0;
   while(1){
       level++;
       if(nums[curr]+curr>=numsSize-1) return level;
       for(int i=1;i<=nums[curr];i++)
         if(nums[i+curr]+curr+i>currMaxTemp){
             currTemp = i+curr;
             currMaxTemp = nums[i+curr]+curr+i;
         }
        curr = currTemp;
   }
   return level;
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
	for (int i=0; i<rows; i++) {
		printf("%d\n",jump(&dataArray[i][1],dataArray[i][0]));
	}
	return 0;
}

