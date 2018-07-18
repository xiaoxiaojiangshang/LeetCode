/*
    Author: jgz
    Date: 2018/7/6 15:09:31
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include<stack>
# define MAXN 1000
using namespace std;

bool isValid(char* s) {
  stack<char> sta;
  int i,len=strlen(s);
  for(i=0;i<len;i++){
  	if(s[i]=='{'||s[i]=='['||s[i]=='(')
  		sta.push(s[i]);
  	else if(!sta.empty()&&s[i]=='}'&&sta.top()=='{')
  		sta.pop();
  	else if(!sta.empty()&&s[i]==']'&&sta.top()=='[')
  		sta.pop();
  	else if(!sta.empty()&&s[i]==')'&&sta.top()=='(')
  		sta.pop();
  	else return false;
  }
  
  return sta.empty();
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
		printf("%d",isValid(s));
	}
	return 0;
}

