/*
    Author: jgz
    Date: 2018/7/12 8:41:00

*/

/*
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */


/*Solutions
solution1 step1����һ���ʵ䣬����ÿһ�����ʶ�����words���汻������������python�ֵ�
	   step2: �����ַ���i=0��strlen-len*N(����len*����N),����ÿһ��i������ַ��������N��
	   substr��words��������һһƥ�䣬��ƥ�䣬����i ���� continue
	   ʱ�临�Ӷȣ� O(N*w*L) Ĭ��hashƥ��
solution2: ���ô��ڻ������������len����ص�
		   step1�� ��ʼ��һ������Ϊ0�Ĵ��ڣ�begin ��tail���tail����һ��������word���棬tail+len��
	   ���ڣ�begin����tail+len�����¿�ʼ��������ҳ��ִ������ڴ����ֵ�,begin=tail ��
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXN 1024*4 // 1000������bug 
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
		memset(substr,0,wordLen*wordsSize+1);// memset ��Ҫ��stlen
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
		printf("���ļ�%s����\n",fname);
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

