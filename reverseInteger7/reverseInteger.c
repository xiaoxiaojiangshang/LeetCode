#include<stdio.h.>
#include <stdbool.h>
#include<limits.h>
int reverse(int x) {
	
	long long  numRev=0;
	int a=0;
	bool flag=true;
	if (x<0)
		x=-x,flag=false;
	
	while(x>0) {
		a=x%10;
		numRev =numRev*10 +a;
		x=x/10;
	}
	if (numRev>INT_MAX) return 0;
	else if(flag)
		return numRev;
	else return -numRev;
}

int main() {
	FILE *fp;
	int num;
	char *fname="F:\\leetcode\\reverseInteger7\\dataIn.txt";
	if((fp=fopen(fname,"r"))==NULL) {
		printf("打开文件%s错误\n",fname);
		return NULL;
	}
	while(fscanf(fp,"%d",&num)==1) {
		printf("%d",num);
		int numRev=reverse(num);
		printf("  %d\n",numRev);
	}
	return 0;
}
