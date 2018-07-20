/*
    Author: jgz
    Date: 2018/7/19 13:56:18
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXN 100

bool isValidSudoku(char** board,char c, int row,int col) {
	int j;
	//  units &&col && row
	int row1 = row/3*3;
	int col1 = col/3*3;
	for(j=0; j<9; j++) {
		if(board[row][j]==c)return false;
		if(board[j][col]==c)return false;
		int row2 = j/3;
		int col2 = j%3;
		if(board[row1+row2][col1+col2]==c)
			return false;
	}
	return true;
}

bool findSudoku(char** board, int row, int col) {
	if(row==9) return true;
	if(col==9) return findSudoku(board,row+1,0);
	if(board[row][col]=='.') {
		for(char c='1'; c<='9'; c++) {
			if(isValidSudoku(board,c,row,col)) {
				board[row][col] = c;
//				return findSudoku(board,row,col+1);
				if(findSudoku(board,row,col+1)) return true;
			}
		}
		//backtracking
		board[row][col]='.';
	} else return findSudoku(board,row,col+1);
	return false;
}
void solveSudoku(char** board, int boardRowSize, int boardColSize) {
//	if(board==NULL||strlen(board[0])!=boardRowSize) return ;
	findSudoku(board,0,0);
}

void predealStr(char *str,char *ret) {
	int count = 0,temp=0;
	while(str[temp]!=']') {
		if(str[temp]=='.'||(str[temp]>='0'&&str[temp]<='9'))
			ret[count++]=str[temp];
		temp++;
	}
}
void show(char**board,int size) {
	for(int i=0; i<size; i++) {
		for(int j=0; j<size; j++) {
			printf("%c ",board[i][j]);
			if(j%3==2)printf("   ");
		}
		printf("\n");
		if(i%3==2)printf("\n");
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
		}
		solveSudoku(board,size,size);
		show(board,size);
	}
	return 0;
}

