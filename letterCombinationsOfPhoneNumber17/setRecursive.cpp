/*
    Author: jgz
    Date: 2018/7/2 20:45:10
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXN 100
const char* key[10]={ "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz" };
void combination(char** ret,char *digits,int offset,int* returnSize,char *prefix){
	if(offset==strlen(digits)){
		ret[*returnSize]=(char *)malloc(sizeof(char)*offset);
		memset(ret[*returnSize],0,sizeof(char)*offset);
		memcpy(ret[*returnSize],prefix,offset);
		(*returnSize)++;
		return ;
	}
	char letters[5]={0};
	memcpy(letters,key[digits[offset]-'0'],strlen(key[digits[offset]-'0']));
	for(int i=0;i<strlen(letters);i++){
		prefix[offset]=letters[i];
		combination(ret,digits,offset+1,returnSize,prefix);
	}
}
char** letterCombinations(char* digits, int* returnSize) {	
    *returnSize=0;
    if (strlen(digits)==0) return NULL;
    int digitsLen=strlen(digits);
    char **ret=(char**)malloc(20000*sizeof(char*));
    char *prefix=(char *)malloc(9*sizeof(char));
    memset(prefix,0,sizeof(prefix));
    combination(ret,digits,0,returnSize,prefix);
    return ret;
}

// awesome ,very clever;
//char** letterCombinations(char* digits, int* returnSize) {
//    int len=strlen(digits);
//    char map[10][5]={" "," ","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
//    
//    *returnSize=1;
//    for(int i=0;i<len;i++){
//        int num=digits[i]-'0';
//        *returnSize*=strlen(map[num]);
//    }
//    if(len==0)
//        *returnSize=0;
//    
//    char** result=malloc(*returnSize*sizeof(char*));
//    
//    for(int i=0;i<*returnSize;i++){
//        result[i]=malloc((len+1)*sizeof(char));
//        result[i][len]='\0';
//    }
//    int size=*returnSize;
//    for(int i=0;i<len;i++){
//        int num=digits[i]-'0';
//        size/=strlen(map[num]);
//        for(int j=0;j<*returnSize;j++){
//            result[j][i]=map[num][(j/size)%strlen(map[num])];
//        }
//    }
//    return result;
//}
int main() {
   const char *fname="dataIn.txt";
	FILE *fp;
	char s[MAXN];
	if((fp=fopen(fname,"r"))==NULL) {
		printf("打开文件%s错误\n",fname);
		return NULL;
	}
	int returnSize;
	while(fscanf(fp,"%s",s)==1) {
	char **ret=letterCombinations(s,&returnSize);
		for(int j=0; j<returnSize;j++){
			printf("%s\n",ret[j]);
		}
	}
	return 0;
}

