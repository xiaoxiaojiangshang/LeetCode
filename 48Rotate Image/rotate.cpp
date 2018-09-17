/*
    Name:
    Copyright:jgz
    Author: jgp
    Date: 2018/9/4 10:52:24
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "F:\\leetcode\\DealTxt\\preDealTxt.cpp"
void rotate(int** matrix, int row, int *Col) {
    int i,j,k;
    int x,y,temp,temp1,temp2;
    for(i=0;i<row/2;i++){
        for(j=i;j<row-i-1;j++) {
            x=i,y=j,temp1 = matrix[x][y];
            for(k=0;k<4;k++){
                temp2= matrix[y][row-1-x];
                matrix[y][row-1-x] = temp1;
                temp = x;
                x = y;
                y= row -1 -temp;
                temp1 = temp2;
            }
        }
    }
    return;
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
    int *numPerLine = dividTwoParts(dataArray,rows) ;
    rotate(dataArray,numPerLine[0],&numPerLine[0]);
    disp(dataArray,numPerLine,rows);
 return 0;
}

