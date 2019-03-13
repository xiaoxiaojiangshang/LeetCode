/*
    Name:
    Copyright:jgz
    Author: jgp
    Date: 2018/10/29 10:54:38
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "F:\\leetcode\\DealTxt\\preDealTxt.cpp"

int min3(int a,int b,int c){
    int min = a;
    if(min>b) min = b;
    if(min>c) min = c;
    return min;
}
int minDistance(char* s1, char* s2) {
    int s1Len = strlen(s1);
    int s2Len = strlen(s2);
    int **dp = (int**)malloc(sizeof(int*)*(s1Len+1));
    memset(dp,0,sizeof(int*)*(s1Len+1));
    int i,j;// 代表当前位置，第几个字母
    for(i=0;i<s1Len+1;i++) {
        dp[i] = (int*)malloc(sizeof(int)*(s2Len+1));
        memset(dp[i],0,sizeof(int)*(s2Len+1));
    }
    for(i=0;i<s1Len+1;i++){
        dp[i][0] = i;
    }
     for(i=0;i<s2Len+1;i++){
        dp[0][i] = i;
    }
    for(i=1;i<s1Len+1;i++){
        for(j=1;j<s2Len+1;j++){
            if(s1[i-1]==s2[j-1])
                dp[i][j] = dp[i-1][j-1];
            else dp[i][j] = min3(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) +1;
            // dp[i-1][j-1] 代表替换
            // dp[i][j-1] 代表s1 插入一个字母(短了) 
            // dp[i-1][j] 代表s1 删除一个字母 (长了) 
        }
    }
    return dp[s1Len][s2Len];
}

int main() {
	const char *fname="dataIn.txt";
	FILE *fp;
	if((fp=fopen(fname,"r"))==NULL) {
		printf("打开文件%s错误\n",fname);
		return NULL;
	}
	char *s1 = (char*)malloc(MAXN*sizeof(char));
	memset(s1,0,MAXN*sizeof(char));
	char *s2 = (char*)malloc(MAXN*sizeof(char));
	memset(s2,0,MAXN*sizeof(char));
    while(fscanf(fp,"%s %s",s1,s2)==2){
         printf("%s convert to %s, the distance is %d\n",s1,s2,minDistance(s1,s2)) ;
    }
	return 0;
}

