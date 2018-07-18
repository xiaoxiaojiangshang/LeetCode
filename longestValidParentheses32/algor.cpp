/*
    Author: jgz
    Date: 2018/7/17 9:49:20
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXN 1000


//algorithm,can use stack,dp,briliant solution
int longestValidParentheses(char* s) {
	//solution1  dp
	/*
	d[i]==')'&&d[i-1]=='(': d[i]=d[i-2]+2
	d[i]==')'&&d[i-1]==')' &&d[i-d[i-1]-1]=='(',匹配:
	d[i] = d[i-1] +2 + d[i-d[i-1]-2] -->()(()) 此时i-d[i-1]-2 =1 i=5
	*/
	int slen = strlen(s);
	int *dp = (int*) malloc(sizeof(int)*slen) ;
	memset(dp,0,sizeof(int)*slen);
	int maxMatch = 0;
	if(s[1]==')'&&s[0]=='(') maxMatch=dp[1] = 2;
	for(int i= 2; i<slen; i++) {
		if(s[i]==')'&&s[i-1]=='(') {
			dp[i]=dp[i-2]+2;
		} else if(s[i]==')'&&s[i-1]==')'&&s[i-dp[i-1]-1]=='(')
			dp[i] = dp[i-1] +2 + dp[i-dp[i-1]-2];
		maxMatch = maxMatch<dp[i]?dp[i]:maxMatch;
	}
	return maxMatch;
	    //solution2 
	    /*
	    same as solution 1,but it is use stack;
		 if()match -->pop , size = i -peek
		 else push (i) 因为从零开始，刚开始push(-1) 
		*/ 
//	    using namespace std;
//	    stack<char> sta;
	    

	    //solution3 双向扫，取最大，充分利用匹配特点。
		 
	    
	    
}
int main() {
	const char *fname="dataIn.txt";
	FILE *fp;
	char s[MAXN];
	if((fp=fopen(fname,"r"))==NULL) {
		printf("打开文件%s错误\n",fname);
		return NULL;
	}
	while(fscanf(fp,"%s",s)==1) {
		printf("ans=%d\n",longestValidParentheses(s));
	}
	return 0;
}

