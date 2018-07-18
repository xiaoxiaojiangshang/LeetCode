/*
    Author: jgz
    Date: 2018/7/11 9:39:03
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXN 10000
int strStr(char* haystack, char* needle) {
	if (strlen(needle)==0) return 0;
	if(strlen(haystack)<strlen(needle))return -1;
	for(int i=0; i<strlen(haystack)-strlen(needle)+1; i++) {
		char *temp = (char*)malloc(sizeof(char)*strlen(needle));
		memset(temp,0,strlen(needle)*sizeof(char)+1);// 初始化最好+1 
		memcpy(temp,&haystack[i],strlen(needle));
		printf("%s\n",temp);
		if(!strcmp(temp,needle))
			return i;
	}
	return -1;
}
char* longestCommonPrefix(char** strs, int strsSize) {
    char *nul =(char*)malloc(sizeof(char)*0);
    memset(nul,0,sizeof(char));
    if(strsSize==0) return nul;
    if(strsSize==1) return strs[0];
	int count=0;
    for(int i=0;i<strlen(strs[0]);i++){
    	char temp = strs[0][i];
        int flag=1;
        for(int j=1;j<strsSize;j++)
        	if(strs[j][i]!=temp)
              {flag=0;break;}
		if(!flag)break;
            else count++;
     }
     if(count==0) return nul;
     char *ret = (char *) malloc(sizeof(char)*count);
    memset(ret,0,sizeof(char)*count+1);
     memcpy(ret,strs[0],count);
     return ret;
}
int main() {
	const char *fname="dataIn.txt";
	FILE *fp;
	char s[MAXN],p[MAXN];
	if((fp=fopen(fname,"r"))==NULL) {
		printf("打开文件%s错误\n",fname);
		return NULL;
	}
	while(fscanf(fp,"%s %s",s,p)==2) {
		printf("%d\n",strStr(s,p));
	}
	return 0;
}

