/*
    Author: jgz
    Date: 2018/7/11 10:44:06
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#define MAXN 10000
int divide(int dividend, int divisor) {
	long long a=dividend;
	long long b=divisor;
	bool flag=(a*b>=0?true:false);
	if(b<0) b= -b;
	if(a<0) a= -a;
	int inc = b;
	long long  count=1;
	while(a>b) {
		b = b<<1;
		count =count +count ;
	}
	int ret = count;
	long long i;
	for(i=count; i>count/2&&a<b; i--) {
		b -= inc;
	}
	if(divisor==-1&&-i==INT_MIN)
		return INT_MAX;
	return (flag>0?i:-i);
}
int main() {
	const char *fname="dataIn.txt";
	FILE *fp;
	int a,b;
	if((fp=fopen(fname,"r"))==NULL) {
		printf("打开文件%s错误\n",fname);
		return NULL;
	}
	while(fscanf(fp,"%d %d",&a,&b)==2) {
		printf("%d\n",divide(a,b));
	}
	return 0;
}

