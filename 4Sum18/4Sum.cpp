/*
    Author: jgz
    Date: 2018/7/5 21:06:43
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXN 1000

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

int cmp(const void *a,const void*b) {
	return *(int*)a - *(int*)b;
}

int** fourSum(int* nums, int numsSize, int target, int* returnSize) {
	qsort(nums,numsSize,sizeof(int),cmp);
	int **ret=(int**)malloc(20000*sizeof(int*));
	int i,j;//保证nums[i]和nums[j]与其他组不同即可满足唯一性。
	*returnSize=0;
	for (i=0; i<numsSize-2; i++) {
		if(i!=0&&nums[i]==nums[i-1])
			continue;
		for(j=i+1; j<numsSize-1; j++) {
			if (j>i+1&&nums[j]==nums[j-1]) continue;
			int l=j+1,r=numsSize-1;
			while(l<r) {
				int sum=nums[i]+nums[l]+nums[r]+nums[j];
				if(sum>target) r--;
				else if(sum<target)l++;
				else {
					ret[*returnSize]=(int *)malloc(sizeof(int)*4);
					ret[*returnSize][0]=nums[l],ret[*returnSize][1]=nums[i];
					ret[*returnSize][2]=nums[j],ret[*returnSize][3]=nums[r];
					while(nums[l]==nums[l+1])l++;
					while(nums[r-1]==nums[r])r--;
					l++;
					r--;// 已经找到，所以不再符合；
					(*returnSize)++;

				}
			}
		}

	}
	return ret;
}

int main() {
	const char *fname="dataIn.txt";
	int dataArray[10][MAXN]= {0};
	int rows=DealTxt(fname,dataArray);
//	disp(dataArray,rows);
	int returnSize=0,target=0;;
	for (int i=0; i<rows; i++) {
		int **ret=fourSum(&dataArray[i][1],dataArray[i][0],target,&returnSize);
		for(int j=0; j<returnSize; j++) {
			for(int k=0; k<4; k++)
				printf("%d ",ret[j][k]);
			printf("\n");
		}
	}
	return 0;
}

