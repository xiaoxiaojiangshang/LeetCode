/*
    Name:
    Copyright:jgz
    Author: jgp
    Date: 2018/8/29 15:08:36
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "F:\\leetcode\\DealTxt\\preDealTxt.cpp"

// 思路奇妙 
int trap(int* height, int heightSize) {
   if(heightSize<3) return 0; 
   int left = 0,right =heightSize-1,sumTrap = 0;
   int maxLeft = height[left],maxRight = height[right];
   while(left<right) {
       if(height[left]<height[right]){
           if(maxLeft>=height[left])
                sumTrap += maxLeft-height[left];
            else maxLeft= height[left];
            left++;
       }
       else{
           if(maxRight>=height[right])
                sumTrap += maxRight-height[right];
            else maxRight= height[right];
            right--;
       }
   }
   return sumTrap;
}
int main() {
	const char *fname="dataIn.txt";
	int **dataArray = (int **)malloc(sizeof(int*)*MAXN);
	int rows=DealTxt(fname,dataArray);
	FILE *fp;
	int returnSize;
	if((fp=fopen(fname,"r"))==NULL) {
		printf("打开文件%s错误\n",fname);
		return NULL;
	}
	for (int i=0; i<rows; i++) {
		printf("%d\n",trap(&dataArray[i][1],dataArray[i][0]));
	}
	return 0;
}

// 思路错误 
//int areaBetweenAdjacent(int * height,int start,int end) {
//	int area=0;
//	int maxMin = height[start]<height[end]
//	             ?height[start]:height[end];
//	area = maxMin * (end-start-1);
//	for(int j=start+1; j<end; j++)
//		area -= min(maxMin,height[j]);
//	return area;
//}
//int trap(int* height, int heightSize) {
//	// 取面积左右两个 
//	if(heightSize<3) return 0;
//    int index = 0,sumTrap =0,count=0;
//    int start=0,end =0; 
//	while(index<heightSize){
//	    if(count==0) {
//            if(index+1<heightSize&&height[index]>height[index+1]){
//                start = index;
//                count++;
//                index++;
//                continue;
//            }
//                
//        } // start 
//        if(count ==1){
//            if(height[index]>height[index-1])
//                end = index,count++; 
//        }// end
//        if(count==2) {
//            sumTrap += areaBetweenAdjacent(height,start,end);
//            count = 0;//重新归零
//            index --; 
//        }
//        index++;
//    }
//	return sumTrap;
//}
