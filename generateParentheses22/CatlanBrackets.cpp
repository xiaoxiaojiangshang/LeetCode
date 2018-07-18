/*
    Author: jgz
    Date: 2018/7/8 10:43:12
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXN 10000

void Catalan (int n,int open,int close,int* returnSize,char * prefix,char **ret){
	if(open+close==n*2){
		ret[*returnSize]=(char*)malloc(sizeof(char)*2*n);
		memset(ret[*returnSize],0,sizeof(char)*(2*n+1));
//		printf("prefix=%s %d\n",prefix,strlen(prefix));
		memcpy(ret[*returnSize],prefix,n*2);
		(*returnSize)++;
		return ;
	}
	if(open<n){
		prefix[open+close]='(';
		Catalan (n,open+1,close,returnSize,prefix,ret);
	}
	if(close<open){
		prefix[open+close]=')';
		Catalan (n,open,close+1,returnSize,prefix,ret);
	}
}
char** generateParenthesis(int n, int* returnSize) {
//	if(n==0) return NULL;
    *returnSize=0;
    char **ret =(char**)malloc(sizeof(char*)*20000);
    char *prefix = (char *)malloc(sizeof(char)*2*n);
    memset(prefix,0,sizeof(char)*(2*n+1));
    Catalan(n,0,0,returnSize,prefix,ret);
	return ret;
}
int main() {
	const char *fname="dataIn.txt";
	FILE *fp;
	int N,returnSize;
	if((fp=fopen(fname,"r"))==NULL) {
		printf("打开文件%s错误\n",fname);
		return NULL;
	}
	while(fscanf(fp,"%d",&N)==1) {
		char **ret =generateParenthesis(N, &returnSize);
		for(int j=0; j<returnSize; j++) {
			printf("%s\n",ret[j]);
		}
		printf("\n");
	}
	return 0;
}

