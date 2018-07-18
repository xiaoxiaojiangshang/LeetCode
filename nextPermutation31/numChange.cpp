/*
    Author: jgz
    Date: 2018/7/16 9:37:25
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include<stdio.h>
#define MAXN 128

int  DealTxt(const char *fname,int (*dataArray)[MAXN]) {
	FILE *fp;
	char s[MAXN];
	if((fp=fopen(fname,"r"))==NULL) {
		printf("打开文件%s错误\n",fname);
		return NULL;
	}
	int row=0;
	while(fgets(s,MAXN,fp)!=NULL) {
		int count=1,temp=0,num=0;
		bool neg=false,beginFlag=false;
		while(s[temp]!='\n'&&s[temp]!='\0') {
			if(s[temp]=='-')
				neg=true;
			else if(s[temp]>='0'&&s[temp]<='9') {
				num=num*10+s[temp]-'0';
				beginFlag=true;
			} else {
				if(beginFlag) {
					dataArray[row][count]=(neg==true?-num:num);
					count++;
					neg=false;
					num=0;
				}
				// 去除不符合的字符
				while((s[temp+1]<'0'||s[temp+1]>'9')&&s[temp]!='\n') {
					if(s[temp+1]=='-')
						neg=true;
					temp++;
				}
			}

			temp++;
		}
		dataArray[row][count]=(neg==true?-num:num);
		dataArray[row][0]=count;
		row++;
	}
	return row;
}
// solution just larger,we should find a[i]<a[i+1](end->0),reverse it and make 
// i+1-->end 最小 reverse it
void swap(int *a,int *b){
	int temp = *a;
	*a = *b;
	*b = temp;
}
void reverse(int* nums, int numsSize){
	int med =numsSize/2;
	for(int i=0;i<med;i++){
		swap(&nums[i],&nums[numsSize-i-1]);
	}
}
void nextPermutation(int* nums, int numsSize) {
	if (numsSize==0) return;
	int i,j;
	for(i = numsSize-2;i>=0;i--){
		if(nums[i]>=nums[i+1])
			continue;
		else break;
	}
	for(j=i+1;j<numsSize;j++){
		if(nums[i]<nums[j])
			continue;
		else break;
	}
	if(i!=-1) {
		swap(&nums[i],&nums[j-1]);
	}
	reverse(&nums[i+1],numsSize-i-1);
}
void disp(int *nums) {
	for(int j=1; j<=nums[0]; j++) {
		printf("%d ",nums[j]);
	}
	printf("\n");
}
int main() {
	const char *fname="dataIn.txt";
	int dataArray[MAXN][MAXN];
	memset(dataArray,0,sizeof(int)*MAXN*MAXN);
	int rows=DealTxt(fname,dataArray);
	for (int i = 0; i<rows; i++) {
		nextPermutation(&dataArray[i][1],dataArray[i][0]);
		disp(dataArray[i]);
	}
	return 0;
}

