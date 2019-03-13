/*
    Name:
    Copyright:jgz
    Author: jgp
    Date: 2018/10/9 19:13:06
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "F:\\leetcode\\DealTxt\\preDealTxt.cpp"

char* simplifyPath(char* path1) {
	// 先用一个二维char 将其拆分
	char *path = (char*)malloc(sizeof(char)*(strlen(path1)+1));
	memset(path,0,sizeof(char)*(strlen(path1)+1));
	memcpy(path,path1,strlen(path1));
	if(path[strlen(path1)]=='\n')
		path[strlen(path1)] = '/';
	else
		path[strlen(path1)-1] = '/';
	char *ret =(char*)malloc(sizeof(char)*MAXN);
	memset(ret,0,sizeof(char)*MAXN);
	int *record =(int*)malloc(sizeof(int)*strlen(path)) ;
	memset(record,0,sizeof(int)*strlen(path));
	int i = 0,posi = 0,count =0;
	for(; i<strlen(path); i++) {
		if(path[i]=='/')
			record[posi++] = i;
	}
	char** temp =(char**)malloc(sizeof(char*)*MAXN);
	memset(temp,0,sizeof(char*)*MAXN);
	for(i=0; i<posi-1; i++)	{
		if((record[i+1]-record[i]==1)||((record[i+1]-record[i]==2)&&path[record[i]+1]=='.'))
			continue;
		temp[count] = (char*)malloc(sizeof(char)*MAXN);
		memset(temp[count],0,sizeof(char)*MAXN);
		memcpy(temp[count++],&path[record[i]+1],record[i+1]-record[i]-1);
	}
	int *flag =(int*)malloc(sizeof(int)*count) ;
	memset(flag,0,sizeof(int)*count);
	for(i=0; i<count; i++) {
		if(strcmp(temp[i],"..")!=0)
			flag [i] = 1;
		else {
			int k = i-1;
			while(k!=-1&&flag[k]==0)
				k--;
			if(k>=0)  flag[k] = 0;
		}
	}
	int start =0;
	for(i=0; i<count; i++) {
		if(flag[i]) {
			ret[start++]='/';
			memcpy(&ret[start],temp[i],strlen(temp[i]));
			start += strlen(temp[i]);
		}
	}
	if(strlen(ret)==0) 
        ret[0] = '/';
	return ret;
}

int main() {
	const char *fname="dataIn.txt";
	FILE *fp;
	char s[MAXN];
	if((fp=fopen(fname,"r"))==NULL) {
		printf("打开文件%s错误\n",fname);
		return NULL;
	}
	while(fgets(s,MAXN,fp)!=NULL) {
		printf("%s\n",simplifyPath(s));
	}
	return 0;
}

