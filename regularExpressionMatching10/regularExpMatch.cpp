/*
	Name: 
	Copyright: jgz
	Author: jgz 
	Date: 27/06/18 21:59
	Description: 
*/
#include<stdio.h>
#define MAXN 100
#include<string.h>


// 动态规划 
bool isMatch(char *s, char* p) {
	int m=strlen(s);
	int n=strlen(p);
	if (m== 0 && n== 0) {
		return true;
	}
	int  dp[m+1][n+1]={0};
	dp[0][0] = 1;
	for (int i = 0; i < n; i++) {
		if (p[i] == '*' && dp[0][i-1]) {
			dp[0][i+1] = 1;
		}
	}
	for (int i = 0 ; i < m; i++) {
		for (int j = 0; j < n; j++) {
			if (p[j] == '.') {
				dp[i+1][j+1] = dp[i][j];
			}
			if (p[j] == s[i]) {
				dp[i+1][j+1] = dp[i][j];
			}
			if (p[j] == '*') {
				if (p[j-1] != s[i] && p[j-1] != '.') {
					dp[i+1][j+1] = dp[i+1][j-1];
				} else {
					dp[i+1][j+1] = (dp[i+1][j] || dp[i][j+1] || dp[i+1][j-1]);
				}
			}
		}
	}
	return dp[m][n]==1;
}

// 递归方法 
//bool match(char a,char b){
//	return a==b||b=='.';
//}
//char getChar(char *str,int p){
//	int sLen=strlen(str);
//	if(sLen>p)return str[p];
//	else return '0';
//}
//bool isMatch(char *s, char* p) {
//	int sLen=strlen(s);
//	int pLen=strlen(p);
//	if(sLen==0&&pLen==0) return true;
//	char s0=getChar(s,0);
//	char p0=getChar(p,0),p1=getChar(p,1);
//	if(match(s0,p0)||p1=='*')
//	{
//		if (p1!='*'){
//			if(sLen==0)return false;
//			return isMatch(&s[1],&p[1]);
//		}
//		bool flag = isMatch(s,&p[2]);// 不匹配情况 
//		if (flag) return flag;
//		int i=0;
//		while(i<sLen&&match(getChar(s,i),p0)){
//			flag=isMatch(&s[i+1],&p[2]);
//			if (flag) return flag;
//			i++;
//		}
//	}
//	return false;	
//}

int main() {
	char *fname="dataIn.txt";
	FILE *fp;
	char s[MAXN],p[MAXN];
	if((fp=fopen(fname,"r"))==NULL) {
		printf("打开文件%s错误\n",fname);
		return NULL;
	}
	while(fscanf(fp,"%s %s",s,p)==2) {
		printf("%d\n",isMatch(s,p));
//		printf("%s\n%s\n",&s[2],&p[0]);
	}
	return 0;
}
