#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<limits.h>
#include <stdbool.h>
#define MAXN 10001

int myAtoi(char* s) {
    long long num=0;
	int temp=0;
    bool flag=true;
    while(s[temp]==' ') 
	 {temp++;}
    if(s[temp]=='-')
    		temp++,flag=false;
    else if(s[temp]=='+') temp++;
    else if (s[temp]<'0'||s[temp]>'9')
        return 0;
    while(s[temp]>='0'&&s[temp]<='9'){
    	num=num*10+s[temp]-'0';
    	temp++;
    	if (num>INT_MAX) 
           {num=(flag==true?INT_MAX:INT_MAX+1);break;}
	}
   return flag==true?num:-num;
}

int main() {
	FILE *fp;
	char s[MAXN];
	int num,answer;
	char *fname="F:\\leetcode\\StringtoInteger8\\dataIn.txt";
	if((fp=fopen(fname,"r"))==NULL) {
		printf("打开文件%s错误\n",fname);
		return NULL;
	}
	while(fgets(s,MAXN,fp)!=NULL) {
	   printf("%s  ",s);
//	   fscanf(fp,"%d",&answer);
	   num=myAtoi(s);
	   printf("num= %d\n ",num);
//	   if(num==answer)
//	     printf("right\n");
//	    else printf("Wrong!");
	}
	return 0;
}
