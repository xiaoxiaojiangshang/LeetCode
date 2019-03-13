/*
    Name:
    Copyright:jgz
    Author: jgp
    Date: 2018/9/27 11:16:32
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "F:\\leetcode\\DealTxt\\preDealTxt.cpp"

int minPathSum(int** grid, int row, int col) {
    int ** dp = (int**) malloc(sizeof(int*)*(row+1));
	int i,j;
	for(i=0; i<=row; i++) {
		dp[i] = (int*) malloc(sizeof(int)*(col+1));
		memset(dp[i],0,sizeof(int)*(col+1));
	}
	// bound
	dp[0][0] = grid[0][0] ;
	for(i=1;i<col;i++){
	    dp[0][i] = dp[0][i-1] +grid[0][i];
    }
    for(i=1;i<row;i++){
	    dp[i][0] = dp[i-1][0] +grid[i][0];
    }
    // middle
    for(i=1;i<row;i++){
        for(j=1;j<col;j++){
            dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j];
        }
    }
    return dp[row-1][col-1];
}
int main() {
	const char *fname="dataIn.txt";
	int **dataArray = (int **)malloc(sizeof(int*)*MAXN);
	int rows=DealTxt(fname,dataArray);
	int *numPerLine = dividTwoParts(dataArray,rows);
	disp(dataArray,numPerLine,rows);
	int resultNum = minPathSum(dataArray, rows,numPerLine[0]);
	printf("%d\n",resultNum);
	return 0;
}

