/*
    Name:
    Copyright:jgz
    Author: jgp
    Date: 2018/10/31 20:48:21
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "F:\\leetcode\\DealTxt\\preDealTxt.cpp"

void setZeroes(int** matrix, int matrixRowSize, int matrixColSize) {
	int i,j;
	bool first_col_flag = false;
	bool first_row_flag = false;
	for(i=0; i<matrixRowSize; i++)
		if(matrix[i][0]==0) {
			first_col_flag= true;
			break;
		}
	for(j=0; j<matrixColSize; j++)
		if(matrix[0][j]==0) {
			first_row_flag= true;
			break;
		}
	for(i=1; i<matrixRowSize; i++) {
		for(j=1; j<matrixColSize; j++)
			if(matrix[i][j]==0) {
				matrix[i][0] = 0;
				matrix[0][j] = 0;
			}
	}
	for(i=1; i<matrixRowSize; i++) {
		for(j=1; j<matrixColSize; j++) {
			if(	matrix[i][0]==0||matrix[0][j]==0)
				matrix[i][j] = 0;
		}
	}
	for(i=0; i<matrixRowSize; i++)
		if(first_col_flag) matrix[i][0] = 0;
	for(j=0; j<matrixColSize; j++)
		if(first_row_flag) matrix[0][j] = 0;
	return ;
}

int main() {
	const char *fname="dataIn.txt";
	int **dataArray = (int **)malloc(sizeof(int*)*MAXN);
	int rows=DealTxt(fname,dataArray);
	int *numPerLine = dividTwoParts(dataArray,rows);
	setZeroes(dataArray, rows, numPerLine[0]);
	disp(dataArray,numPerLine,rows);
	return 0;
}

