#include<stdio.h.>
#include<string.h>
#include<stdlib.h>
#define MAXN 1001
char* longestPalindrome(char* s) {
	char *temp=(char*)malloc(1001*sizeof(char));
//	memset(temp,0,sizeof(char)*1000);
	int i,j,b,e,max=0;
	int sLen=strlen(s);
	for(i=0; i<sLen; i++) {
		// odd
		for(j=0; i-j>=0&&i+j<sLen; j++) {
			if(s[i-j]!=s[i+j]) break;
			if(2*j+1>max) {
				max=2*j+1;
				b=i-j,e=i+j;
			}
		}
		//even
		for(j=0; i-j>=0&&i+j+1<sLen; j++) {
			if(s[i-j]!=s[i+j+1]) break;
			if(2*j+2>max) {
				max=2*j+2;
				b=i-j,e=i+j+1;
			}
		}
	}
	for(i=0; i<e-b+1; i++)
		temp[i]	= s[b+i];
	temp[i]='\0';
	return temp;
}


int main() {
	FILE *fp;
	char s[MAXN];
	char *fname="F:\\leetcode\\longestPalindrome5\\dataIn.txt";
	if((fp=fopen(fname,"r"))==NULL) {
		printf("打开文件%s错误\n",fname);
		return NULL;
	}
	while(fgets(s,MAXN,fp)!=NULL) {
		printf("%s\n",s);
		char *temp=longestPalindrome(s);
		printf("%s\n",temp);
	}
	return 0;
}
