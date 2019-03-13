/*
    Name:
    Copyright:jgz
    Author: jgp
    Date: 2018/11/1 21:38:38
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "F:\\leetcode\\DealTxt\\preDealTxt.cpp"

bool searchMatrix(int** matrix, int matrixRowSize, int matrixColSize, int target) {
	int left= 0 ,right = matrixRowSize* matrixColSize-1;
	int  mid_row,mid_col,mid;
	while(left<=right) {
		mid = (left+right)/2;
		mid_row = mid/matrixColSize;
		mid_col = mid%matrixColSize;
		if(matrix[mid_row][mid_col]==target)
			return true;
		if(matrix[mid_row][mid_col]<target) {
			left = mid +1;
		}
		if (matrix[mid_row][mid_col]>target) {
			right = mid -1;
		}
	}
	return false;
}
int main() {
	const char *fname="dataIn.txt";
	int **dataArray = (int **)malloc(sizeof(int*)*MAXN);
	int rows=DealTxt(fname,dataArray);
	int *numPerLine = dividTwoParts(dataArray,rows);
	int target = 2;
	printf("The answer is %d\n",searchMatrix(dataArray, rows, numPerLine[0],target));
	return 0;
}

