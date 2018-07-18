#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#define MAXN 100001

char* convert(char* s, int numRows) {
	if(numRows==1) return s;
	int sLen=strlen(s),i;
	//多一个长度，并初始化
	char *temp=(char*)malloc((sLen+1)*sizeof(char));
	memset(temp,0,sizeof(char)*(sLen+1));
	int count=0;
	for(i=0; i<numRows; i++) {
		int posi=i;
		if(posi<sLen) temp[count]=s[posi],count++;
		int step1=2*(numRows-i-1);
		int step2=2*i;
		while(1) {
			posi += step1;
			if(posi>=sLen)
				break;
			if(step1)
				temp[count]=s[posi],count++;
			posi += step2;
			if(posi>=sLen)
				break;
			if(step2)
				temp[count]=s[posi],count++;
		}
	}
//	printf("%s\n",temp);
	return temp;
}

int main() {
	FILE *fp;
	char s[MAXN],rightStr[MAXN];
	int numRows;
	char *fname="F:\\leetcode\\ZigZagConversion6\\dataIn.txt";
	if((fp=fopen(fname,"r"))==NULL) {
		printf("打开文件%s错误\n",fname);
		return NULL;
	}
	while(fscanf(fp,"%d",&numRows)==1) {
		fscanf(fp,"%s",s);
		fscanf(fp,"%s",rightStr);
		char *temp=convert(s,numRows);
		if (strcmp(temp, rightStr) == 0)
			printf("true\n");
		else printf("wrong\n");
	}
	return 0;

}
