/*
    Name:
    Copyright:jgz
    Author: jgp
    Date: 2018/11/2 10:04:55
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "F:\\leetcode\\DealTxt\\preDealTxt.cpp"
//using namespace std
void sortColors(int* nums, int numsSize) {
//	int *count = (int*) malloc(sizeof(int)*4);
//	memset(count,0,sizeof(int)*4);
//	for(int i=0; i<numsSize; i++) {
//		count[nums[i]] = count[nums[i]]+1;
//	}
//	memset(nums,0,sizeof(int)*count[0]);
//	fill_n(&nums[count[0]],count[1],1);
//	fill_n(&nums[count[0]+count[1]],count[2],2);
    int start = 0, end = numsSize-1;
    for(int i=0;i<numsSize;i++){
        if(nums[i]==0) 
            swap(&nums[i],&nums[start++]);
        else if(nums[i]==2&&i<end)
            swap(&nums[i--],&nums[end--]);
    }
}
int main() {
	const char *fname="dataIn.txt";
	int **dataArray = (int **)malloc(sizeof(int*)*MAXN);
	int rows=DealTxt(fname,dataArray);
	int *numPerLine = dividTwoParts(dataArray,rows);
	for (int i=0; i<rows; i++) {
		sortColors(dataArray[i],numPerLine[i]);
	}
	disp(dataArray,numPerLine,rows);
	return 0;
}

