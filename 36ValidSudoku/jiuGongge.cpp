/*
    Author: jgz
    Date: 2018/7/18 13:49:58
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXN 100
bool isValidSudoku(char** board, int boardRowSize, int boardColSize) {
	int i,j,temp[10];
	// row
	for(i=0; i<boardRowSize; i++) {
		memset(temp,0,sizeof(int)*10);
		for(j=0; j<boardColSize; j++) {
			if(board[i][j]=='.')
				continue;
			else if(temp[board[i][j]-'0']==1)
				return false;
			else temp[board[i][j]-'0']=1;
		}
	}
	//column
	for(i=0; i<boardColSize; i++) {
		memset(temp,0,sizeof(int)*10);
		for(j=0; j<boardRowSize; j++) {
			if(board[j][i]=='.')
				continue;
			else if(temp[board[j][i]-'0']==1)
				return false;
			else temp[board[j][i]-'0']=1;
		}
	}
	// 9 units
	for(i=0; i<9; i++) {
		int row1 = i/3*3;
		int col1 = i%3*3;
		memset(temp,0,sizeof(int)*10);
		for(j=0; j<9; j++) {
			int row2 = j/3;
			int col2 = j%3;
			if(board[row1+row2][col1+col2]=='.')
				continue;
			else if(temp[board[row1+row2][col1+col2]-'0']==1)
				return false;
			else temp[board[row1+row2][col1+col2]-'0']=1;

		}
	}
	return true;
}
void predealStr(char *str,char *ret) {
	int count = 0,temp=0;
	while(str[temp]!=']') {
		if(str[temp]=='.'||(str[temp]>='0'&&str[temp]<='9'))
			ret[count++]=str[temp];
		temp++;
	}
}
int main() {
	const char *fname="dataIn.txt";
	FILE *fp;
	int size;
	char s[MAXN];
	if((fp=fopen(fname,"r"))==NULL) {
		printf("打开文件%s错误\n",fname);
		return NULL;
	}
	while(fscanf(fp,"%d",&size)==1) {
		char **board =(char **)malloc(sizeof(char*)*size);
		for(int i =0; i<size; i++) {
			fscanf(fp,"%s",s);
			board[i] = (char *)malloc(sizeof(char)*(size+1));
			memset(board[i],0,sizeof(char)*(size+1));
			predealStr(s,board[i]);
			printf("%s\n",board[i]);
		}
		printf("%d\n",isValidSudoku(board,size,size));
	}
	return 0;
}

