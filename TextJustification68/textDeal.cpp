/*
    Name:
    Copyright:jgz
    Author: jgp
    Date: 2018/9/29 12:55:14
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "F:\\leetcode\\DealTxt\\preDealTxt.cpp"

char** fullJustify(char** words, int wordsSize, int maxWidth, int* returnSize) {
	char *blackTemp = (char*)malloc(sizeof(char)*100);
	memset(blackTemp,' ',sizeof(char)*100);
	int wordPerLine = 0,sumLen=0,startPosition=0;
	char **ret = (char**) malloc(sizeof(char*)*MAXN);
	memset(ret,0,sizeof(char*)*MAXN);
	for(int i=0; i<wordsSize; i++) {
		sumLen += strlen(words[i]);
		if(sumLen+wordPerLine<=maxWidth) {
			// 最后一行规则,不满也开始结束
			//last words
			if(i==wordsSize-1) {
				ret[*returnSize] = (char*) malloc(sizeof(char)*(maxWidth+10));
				memset(ret[*returnSize],0,sizeof(char)*(maxWidth+10));
				int start = 0;
				memcpy(&(ret[*returnSize][start]),words[startPosition],strlen(words[startPosition]));
				start +=strlen(words[startPosition]);
				for(int j=startPosition+1; j<=i; j++) {
					memcpy(&(ret[*returnSize][start]),blackTemp,1);
					start ++;
					memcpy(&(ret[*returnSize][start]),words[j],strlen(words[j]));
					start +=strlen(words[j]);
				}
				memcpy(&(ret[*returnSize][start]),blackTemp,maxWidth-strlen(ret[*returnSize]));
				(*returnSize)++ ;
			}
			wordPerLine ++ ;
		}
		// 计算空格，左边多，有变少
		else {
			int black = maxWidth - sumLen + strlen(words[i]);
			ret[*returnSize] = (char*) malloc(sizeof(char)*(maxWidth+1));
			memset(ret[*returnSize],0,sizeof(char)*(maxWidth+1));
			int start = 0,blackNum=0;
			memcpy(&(ret[*returnSize][start]),words[startPosition],strlen(words[startPosition]));
			start +=strlen(words[startPosition]);
			for(int j=startPosition+1; j<i; j++) {
				blackNum = (black+wordPerLine-2)/(wordPerLine-1);
				memcpy(&(ret[*returnSize][start]),blackTemp,blackNum);
				start += blackNum;
				memcpy(&(ret[*returnSize][start]),words[j],strlen(words[j]));
				start +=strlen(words[j]);
				black -= blackNum;
				wordPerLine--;
			}
			memcpy(&(ret[*returnSize][start]),blackTemp,maxWidth-strlen(ret[*returnSize]));
			(*returnSize)++ ;
			startPosition = i;
			wordPerLine = 0,sumLen=0;
			i = i-1;
		}
	}
	return ret;
}
int main() {
	const char *fname="dataIn.txt";
	char **dataArray = (char**)malloc(sizeof(char*)*MAXN);
	int wordsSize=dealTxtChar(fname,dataArray);
	int  returnSize=0,maxWidth = 16;
//	for(int i=0; i<wordsSize; i++)
//		printf("%s\n",dataArray[i]);
	char **ret = fullJustify(dataArray,wordsSize,maxWidth,&returnSize);
	for(int i=0; i<returnSize; i++)
		printf("%s\n",ret[i]);
	return 0;
}

