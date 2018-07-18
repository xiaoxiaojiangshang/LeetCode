#include<stdio.h>
#define MAXN 100000

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
	if(nums1Size>nums2Size)
		return findMedianSortedArrays(nums2,nums2Size,nums1,nums1Size);
	int imin=0,imax=nums1Size,halfLen=(nums1Size+nums2Size+1)/2;
	bool oddOrEven=((nums1Size+nums2Size)%2==1?true:false);
	double maxLeft,minRight;
	while(imin<=imax) {
		int i=(imin+imax)/2;
		int j=halfLen-i;
//		if (i<nums1Size) {
//			if(nums2[j-1]>nums1[i])// 因为i并不成立，舍去
//				imin=i+1;
//		} else if(i>0) {
//			if(nums1[i-1]>nums2[j])
//				imax=i-1;
		if (i<nums1Size&&nums2[j-1]>nums1[i]) {
			imin=i+1;
		} else if(i>0&&nums1[i-1]>nums2[j]) {
			imax=i-1;
		} else {
			if (i==0)
				maxLeft=nums2[j-1];
			else if(j==0)
				maxLeft=nums1[i-1];
			else
				maxLeft=nums1[i-1]>nums2[j-1]?nums1[i-1]:nums2[j-1];
			if (oddOrEven) //odd
				return maxLeft;
			if (i==nums1Size)
				minRight=nums2[j];
			else if(j==nums2Size)
				minRight=nums1[i];
			else minRight=nums1[i]<nums2[j]?nums1[i]:nums2[j];
			return (maxLeft+minRight)/2;
		}
	}
	return 1;
}

int  DealTxt(char *fname,int (*dataArray)[MAXN]) {
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
int main() {
	int nums1[MAXN]= {0};
	int nums2[MAXN]= {0};
	char *fname="dataIn.txt";
	int dataArray[2][MAXN]= {0};
	int rows=DealTxt(fname,dataArray);
	for (int i=0; i<dataArray[0][0]; i++)
		nums1[i]=dataArray[0][i+1];
	for (int i=0; i<dataArray[1][0]; i++)
		nums2[i]=dataArray[1][i+1];
	double s = findMedianSortedArrays(nums1,dataArray[0][0],nums2,dataArray[1][0]);
	printf("%.1f",s);
	return 0;
}
