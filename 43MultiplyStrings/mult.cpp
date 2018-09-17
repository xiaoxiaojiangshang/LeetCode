/*
    Name:
    Copyright:jgz
    Author: jgp
    Date: 2018/9/5 15:06:58
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "F:\\leetcode\\DealTxt\\preDealTxt.cpp"

char* multiply(char* num1, char* num2) {

	int *temp = (int *)malloc(sizeof(char)*MAXN);
	memset(temp,0,sizeof(char)*MAXN);
	int i,j,p;
	int l1 = strlen(num1), l2 = strlen(num2);
	char *ret = (char*)malloc(sizeof(char)*(l1+l2+1));
	memset(ret,0,sizeof(char)*(l1+l2+1));
	if(num1[0]=='0'||num2[0]=='0') {
	    ret[0]='0';
	    return ret;
    }
	for(i = l1-1; i>=0; i--) {
		for(j = l2-1; j>=0; j--) {
			p = (num1[i]-'0')*(num2[j]-'0')+temp[i+j+1];
			temp[i+j+1] = p %10;
			temp[i+j] += p/10 ;
		}
	}
	j=0;
	i= temp[0]==0?1:0;
	for(; i<l1+l2; i++) {
		ret[j++] = temp[i] +'0';
	}
	return ret;
}
int main() {
	const char *fname="dataIn.txt";
	FILE *fp;
	char *num1 = (char *)malloc(sizeof(char)*MAXN);
	char *num2 = (char *)malloc(sizeof(char)*MAXN);
	memset(num1,0,sizeof(char)*MAXN);
	memset(num2,0,sizeof(char)*MAXN);
	if((fp=fopen(fname,"r"))==NULL) {
		printf("打开文件%s错误\n",fname);
		return NULL;
	}
	while(fscanf(fp,"%s %s",num1,num2)==2) {
		printf("%s\n",multiply(num1,num2));
	}
	return 0;
}

