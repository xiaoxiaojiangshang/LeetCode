/*
    Name:
    Copyright:jgz
    Author: jgp
    Date: 2018/8/4 15:22:56
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXN 1024*1024
const int N = 8;

void fill(char***ret ,int*returnSize,int*temp,int n) {
	ret[*returnSize] =(char**) malloc(sizeof(char*)*(n+1));
	memset(ret[*returnSize],0,sizeof(char*)*(n+1));
	int i,j;
	for(i=0; i<n; i++) {
	    ret[*returnSize][i] =(char*) malloc(sizeof(char)*(n+1));
        memset(ret[*returnSize][i],0,sizeof(char)*(n+1));
		for(j=0; j<n; j++) {
			ret[*returnSize][i][j] = '.';
		}
		ret[*returnSize][i][temp[i]] = 'Q';
	}
	(*returnSize)++;
}

bool check(int *temp,int cur,int col) {
	for(int i=0; i<cur; i++) {
		if(temp[i]+i==cur+col||temp[i]-i==col-cur||temp[i]==col)
			return false;
	}
	return true;
}
void backTracking (char***ret,int *temp,int cur,int n,int*returnSize) {
	// 出口
	if(cur==n) {
		fill(ret,returnSize,temp,n);
		return;
	}
	// cur 是当前行，col是当前列
	for(int col =0; col<n; col++) {
		if(check(temp,cur,col)) {
			temp[cur] = col;
			backTracking(ret,temp,cur+1,n,returnSize);
		}
	}
}
char*** solveNQueens(int n, int* returnSize) {
	char ***ret = (char***)malloc(sizeof(char**)*MAXN);
	int *temp =(int*)malloc(sizeof(int)*(n+1));
	memset(temp,0,sizeof(int)*(n+1));
	*returnSize = 0;
	backTracking(ret,temp,0,n,returnSize);
	free(temp);
	return ret;
}

disp(char ***ret,int N,int returnSize) {
	int i,j,k;
	for(i=0; i<returnSize; i++) {
		printf("solution %d\n",i+1);
		for(j=0; j<N; j++) {
			for(k=0; k<N; k++) {
				printf("%c",ret[i][j][k]);
			}
			printf("\n");
		}
		printf("\n");
	}
}
int main() {
	int returnSize;
	char ***ret = solveNQueens(N,&returnSize);
	disp(ret,N,returnSize) ;
	return 0;
}

