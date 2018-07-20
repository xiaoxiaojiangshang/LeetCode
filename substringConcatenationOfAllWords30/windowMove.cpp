/*
    Author: jgz
    Date: 2018/7/12 8:41:00

*/

/*
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */


/*Solutions
solution1 step1：做一个词典，对于每一个单词都能在words里面被索引，类似于python字典
	   step2: 对于字符串i=0：strlen-len*N(单词len*个数N),对于每一个i后面的字符串，拆成N个
	   substr与words里面索引一一匹配，都匹配，保留i 否则 continue
	   时间复杂度： O(N*w*L) 默人hash匹配
solution2: 采用窗口滑动，充分利用len相等特点
		   step1： 初始化一个长度为0的窗口，begin 和tail如果tail后面一个单词在word里面，tail+len；
	   不在，begin等于tail+len，重新开始，如果在且出现次数大于大于字典,begin=tail ；
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXN 1024*4 // 1000好像有bug 
#define TABLE_SIZE 1024*8

struct node {
	char *word;
	int count ;
	struct node * next;
};
unsigned int hash_33(char *str) {
	unsigned int hashValue = 0;
	while(*str) {
		hashValue= hashValue<<5+hashValue + *str++;//time 33
	}
	return hashValue;
}
struct node** creatHashTable() {
	struct node** ret = (struct node**)malloc(sizeof(struct node*)*TABLE_SIZE);
	if(ret==NULL)
		return NULL;// malloc failed
	memset(ret,0,sizeof(struct node*)*TABLE_SIZE);
	return ret;
}

struct node*  hashTablePut(struct node **table,char *str) {
	unsigned int key = hash_33(str)%TABLE_SIZE;
	struct node *p = table[key];
	struct node *prep = p;
	while(p) {
		if(strcmp(p->word,str)==0) {
			p->count ++;
			return p;
		} else prep =p;
		p=p->next;
	}

	if(p==NULL) { // new
		struct node *temp = (struct node *)malloc(sizeof(struct node));
		if(temp==NULL)
			return NULL;
		temp->next = NULL;
		temp->count=0;
		temp->word = (char *)malloc(sizeof(char)*strlen(str)+1);
		memset(temp->word,0,sizeof(char)*strlen(str)+1);
		memcpy(temp->word,str,sizeof(char)*strlen(str)+1);
		temp->count=1;
		if(prep==NULL)
			table[key] = temp;
		else prep->next = temp;
		return temp;
	}
}
struct node* hashTableGet(struct node **table,char *str) {
	unsigned key = hash_33(str)%TABLE_SIZE;
	struct node *p = table[key];
	while(p) {
		if(strcmp(p->word,str)==0) {
			return p;
		}
		p=p->next;
	}
	return NULL;
}
// hashTable campare
bool hashTableCampare(struct node **table1,struct node **table2,char *s,int wordLen) {
	char *temp=(char *)malloc(sizeof(char)*(wordLen+1));
	memset(temp,0,wordLen+1);
	for(int i=0; i<strlen(s); i=i+wordLen) {
		memcpy(temp,&s[i],wordLen);
		struct node* node1=hashTableGet(table1,temp);
		struct node* node2=hashTableGet(table2,temp);
		if(node1->count!=node2->count)
			return false;
	}
	return true;
}
/* delete a HashTable instance */
void hashTableDelete(struct node **table) {
	for (int i = 0; i<TABLE_SIZE; i++) {
		struct node* p = table[i];
		struct node* q;
		while (p) {
			q = p->next;
			free(p);
			p = q;
		}
	}
	free(table);
}
int* findSubstring(char* s, char** words, int wordsSize, int *returnSize) {
	if(strlen(s)==0||wordsSize==0) return NULL;
	* returnSize=0;
	struct node** table1= creatHashTable();
	for(int i=0; i<wordsSize; i++) {
		hashTablePut(table1,words[i]);
	}
	int wordLen = strlen(words[0]);
	int i,j;
	char *temp=(char *)malloc(sizeof(char)*(wordLen+1));
	memset(temp,0,wordLen+1);
	char *substr = (char *)malloc(sizeof(char)*(wordLen*wordsSize+1));
	struct node** table2= creatHashTable();
	struct node *index;
	int *result=(int*)malloc(sizeof(int)*1000);
//solution1
	for(i=0; i<strlen(s)-wordsSize*wordLen+1; i++) {
		memset(table2,0,sizeof(struct node*)*TABLE_SIZE);
		bool flag=true; //true mean probable mathc
		memset(substr,0,wordLen*wordsSize+1);// memset 不要用stlen
		for(j=i; j<wordsSize*wordLen+i; j=j+wordLen) {
			memcpy(temp,&s[j],wordLen);
			index = hashTableGet(table1,temp);
			if(index==NULL) {
				flag=false;
				break;
			} else hashTablePut(table2,temp);
		}
		if(!flag) continue;
		memcpy(substr,&s[i],wordLen*wordsSize);
		if(hashTableCampare(table1,table2,substr,wordLen)) {
			result[(*returnSize)++]=i;
		}
	}
//	free(table1);
//	free(table2);
	hashTableDelete(table1);
	hashTableDelete(table2);
	return result;
	//
}
int main() {
	const char *fname="dataIn.txt";
	FILE *fp;
	char s[MAXN];
	if((fp=fopen(fname,"r"))==NULL) {
		printf("打开文件%s错误\n",fname);
		return NULL;
	}
	int N,returnSize;
	while(fscanf(fp,"%s",s)==1) {
		fscanf(fp,"%d",&N);
		char **words =(char**)malloc(sizeof(char*)*N);
//char **words = NULL;
		for(int i=0; i<N; i++) {
			words[i]=(char*)malloc(sizeof(char)*MAXN);
			memset(words[i],0,sizeof(char)*MAXN);
			fscanf(fp,"%s",words[i]);
		}
		int *indexs = findSubstring(s,words,N,&returnSize);
		for(int j=0; j<returnSize; j++)
			printf("%d ",indexs[j]);
		printf("\n");
	}
	return 0;
}

