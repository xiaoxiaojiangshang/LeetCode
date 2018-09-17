/*
    Name:
    Copyright:jgz
    Author: jgp
    Date: 2018/9/6 20:42:20
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "F:\\leetcode\\DealTxt\\preDealTxt.cpp"

int* spiralOrder(int** matrix, int row, int col) {
    int *ret = (int *)malloc(sizeof(int)*(row*col+100));
    memset(ret,0,sizeof(int)*(row+col+100));
    int i,j,k,count=0;
    for(i=0;i<(row+1)/2;i++){
        //1
        if(i>=col-i) break;
        for(j=i;j<col-i;j++)
            ret[count++] = matrix[i][j];
        if(i+1>=row-i) break;
        for(k=i+1;k<row-i;k++)
            ret[count++] = matrix[k][col-i-1];
        if(col-i-2<i) break;
        for(j=col-i-2;j>=i;j--)
            ret[count++] = matrix[row-i-1][j];
        if(row-i-2<i) break;
        for(k=row-i-2;k>=i+1;k--)
            ret[count++] = matrix[k][i];
    }
    int *ret1 = (int *)malloc(sizeof(int)*(row*col));
    memset(ret1,0,sizeof(int)*(row*col));
    memcpy(ret1,ret,sizeof(int)*(row*col));
    return ret1;
}
int main() {
	const char *fname="dataIn.txt";
	int **dataArray = (int **)malloc(sizeof(int*)*MAXN);
	int rows=DealTxt(fname,dataArray);

	int *numPerLine = dividTwoParts(dataArray,rows) ;
	int *ret = spiralOrder(dataArray,rows,numPerLine[0]);
	for(int i =0; i<rows*numPerLine[0]; i++) printf("%d ",ret[i]);
	return 0;
}

