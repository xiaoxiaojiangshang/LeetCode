/*
    Name:
    Copyright:jgz
    Author: jgp
    Date: 2018/9/25 20:16:49
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "F:\\leetcode\\DealTxt\\preDealTxt.cpp"

//recursive 超时
//int recursive(int** obstacleGrid,int row,int col) {
//	if(obstacleGrid[row][col])
//		return 0;
//	if(row==0&&col==0)
//	   return 1;
//	if(col==0)
//		return recursive(obstacleGrid,row-1,col);
//	if(row==0)
//		return recursive(obstacleGrid,row,col-1);
//	else
//		return recursive(obstacleGrid,row-1,col)+recursive(obstacleGrid,row,col-1);
//}
//int uniquePathsWithObstacles(int** obstacleGrid, int obstacleGridRowSize, int obstacleGridColSize) {
//    return recursive(obstacleGrid,obstacleGridRowSize-1,obstacleGridColSize-1);
//}
int uniquePathsWithObstacles(int** obstacleGrid, int row, int col) {
	int ** dp = (int**) malloc(sizeof(int*)*(row+1));
	int i,j;
	for(i=0; i<=row; i++) {
		dp[i] = (int*) malloc(sizeof(int)*(col+1));
		memset(dp[i],0,sizeof(int)*(col+1));
	}
	i=0;
	//初始赋值比较麻烦一点 
	if(!obstacleGrid[0][0]) {
	   if(!obstacleGrid[0][1]||(row>1&&!obstacleGrid[1][0])) dp[0][1] = 1;
	}
	for(i=1; i<=row; i++) {
		for(j=1; j<=col; j++) {
			if(!obstacleGrid[i-1][j-1])
				dp[i][j] = dp[i-1][j]+dp[i][j-1];
		}
	}
	return dp[row][col];
}
int main() {
	const char *fname="dataIn.txt";
	int **dataArray = (int **)malloc(sizeof(int*)*MAXN);
	int rows=DealTxt(fname,dataArray);
	int *numPerLine = dividTwoParts(dataArray,rows);
	disp(dataArray,numPerLine,rows);
	int resultNum = uniquePathsWithObstacles(dataArray, rows,numPerLine[0]);
	printf("%d\n",resultNum);
	return 0;
}

