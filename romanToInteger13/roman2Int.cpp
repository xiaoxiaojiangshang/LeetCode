/*
    Author: jgz
    Date: 2018/6/29 18:55:14
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXN 100

/*
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
*/
  
int romanToInt(char* s) {
	int value[90]={0};
	value['I']=1,value['V']=5,value['X']=10;
	value['L']=50,value['C']=100,value['D']=500,value['M']=1000;
    int i,sum=0,temp=0;
 	int sLen=strlen(s);
 	for(i=0;i<sLen-1;i++){
 		if(value[s[i]]>=value[s[i+1]])
 			sum +=value[s[i]];
 		else sum -=value[s[i]];
	 }
	 sum += value[s[i]];
	return sum;
}
int main() {
	const char *fname="dataIn.txt";
	FILE *fp;
	char s[MAXN];
	int num;
	if((fp=fopen(fname,"r"))==NULL) {
		printf("打开文件%s错误\n",fname);
		return NULL;
	}
	while(fscanf(fp,"%d %s",&num,s)==2) {
		if(romanToInt(s)==num)
		     printf("true\n");
		else printf("wrong\n");
	}
	return 0;
}


