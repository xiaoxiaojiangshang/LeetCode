/*
    Author: jgz
    Date: 2018/7/20 21:37:38
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "F:\\leetcode\\DealTxt\\preDealTxt.cpp"
#define MAXN 100
int** combinationSum(int* candidates, int candidatesSize, int target, int** columnSizes, int* returnSize) {
    
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
for(int i=0;i<rows;i++){
	int **ret = (&dataArray[i][1],dataArray[i][1],7,,&returnSize);
}
	return 0;
}

