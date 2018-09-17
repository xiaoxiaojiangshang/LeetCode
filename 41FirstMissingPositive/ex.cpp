/*
    Name:
    Copyright:jgz
    Author: jgp
    Date: 2018/8/28 16:43:49
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "F:\\leetcode\\DealTxt\\preDealTxt.cpp"

int firstMissingPositive(int* nums, int numsSize) {
    int *temp = (int *)malloc(sizeof(int)*(numsSize+1)) ;
    memset(temp,0,sizeof(int)*(numsSize+1));
    for(int i = 0;i<numsSize;i++){
        if(nums[i]>0&&nums[i]<numsSize+1)
            temp[nums[i]] = 1;
    }
    for(int i = 1;i<numsSize+1;i++){
        if(temp[i]==0)
            return i; 
    }
    return numsSize+1;
}

int main() {
	const char *fname="dataIn.txt";
	int **dataArray = (int **)malloc(sizeof(int*)*MAXN);
	int rows=DealTxt(fname,dataArray);
	FILE *fp;
	if((fp=fopen(fname,"r"))==NULL) {
		printf("打开文件%s错误\n",fname);
		return NULL;
	}
//	disp(dataArray,rows);
    for (int i=0;i<rows;i++){
        printf("%d\n",firstMissingPositive(&dataArray[i][1],dataArray[i][0]));
    }
 return 0;
}

