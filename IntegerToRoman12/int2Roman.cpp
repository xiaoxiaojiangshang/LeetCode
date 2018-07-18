/*
    Author: jgz
    Date: 2018/6/29 9:55:14
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXN 100


  
char* intToRoman(int num) {
	const char *c[4][10]={
            {"","I","II","III","IV","V","VI","VII","VIII","IX"},
            {"","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"},
            {"","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"},
            {"","M","MM","MMM"}
        };  
	char *s=(char*)malloc((100)*sizeof(char));
	memset(s,0,sizeof(s));
	int th = num/1000;
	if(th) strcat(s,c[3][th]);
	num=num%1000;
	int hu = num/100;
	if(hu) strcat(s,c[2][hu]);
	num=num%100;
	int te = num/10;
	if(te) strcat(s,c[1][te]);
	int di = num%10;
	if(di) strcat(s,c[0][di]);
    return s;
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
		if(strcmp(intToRoman(num),s)==0)
		     printf("true\n");
		else printf("wrong\n");
	}
	return 0;
}


