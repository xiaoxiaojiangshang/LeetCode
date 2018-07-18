/*
	update： 
    Author: jgz
    Date: 2018/7/17 9:42:18
    mallco内存分配比直接二维数组靠谱 
*/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAXN 1024

int  DealTxt(const char *fname,int **dataArray) {
	FILE *fp;
	char s[MAXN];
	if((fp=fopen(fname,"r"))==NULL) {
		printf("打开文件%s错误\n",fname);
		return NULL;
	}
	int row=0;
	while(fgets(s,MAXN,fp)!=NULL) {
		int count=1,temp=0,num=0;
		bool neg=false,beginFlag=false,endFlag=false;
		dataArray[row] = (int *)malloc(sizeof(int)*MAXN);
		memset(dataArray[row],0,sizeof(int)*MAXN);
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
				while(s[temp+1]<'0'||s[temp+1]>'9') {
					if((s[temp+1]=='\n'||s[temp+1]=='\0')&&(s[temp]<'0'||s[temp]>'9')) {
						endFlag=true;
						break;
					}
					if(s[temp+1]=='-')
						neg=true;
					temp++;
				}
			}

			temp++;
		}
		if(!endFlag)
			dataArray[row][count]=(neg==true?-num:num);
		else count--;
		dataArray[row][0]=count;
		row++;
	}
	return row;
}

void disp(int **dataArray,int rows) {
	int i,j;
	for(i=0; i<rows; i++)  {
		for(j=0; j<=dataArray[i][0]; j++) {
			printf("%d ",dataArray[i][j]);
		}
		printf("\n");
	}
}

//int main() {
//	const char *fname="dataIn.txt";
//	int **dataArray = (int **)malloc(sizeof(int*)*MAXN);
//	int rows=DealTxt(fname,dataArray);
//	disp(dataArray,rows);
//	return 0;
//}
