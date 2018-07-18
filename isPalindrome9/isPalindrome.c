#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<limits.h>
#include <stdbool.h>
#define MAXN 10001

bool isPalindrome(int x) {
    if(x<0||(x!=0&&x%10==0))return false;
    int xRev=0;
//    while(x>0){
//    	xRev=xRev*10+x%10;
//    	x=x/10;
//	}
while(x>xRev){
    	xRev=xRev*10+x%10;
    	x=x/10;
}
	return (xRev==x||xRev/10==x);
}

int main() {
	FILE *fp;
	int num;
	char *fname="dataIn.txt";
	if((fp=fopen(fname,"r"))==NULL) {
		printf("打开文件%s错误\n",fname);
		return NULL;
	}
	while(fscanf(fp,"%d",&num)==1) {
	   bool flag=isPalindrome(num);
	   printf("flag= %d\n ",flag);
	}
	return 0;
}
