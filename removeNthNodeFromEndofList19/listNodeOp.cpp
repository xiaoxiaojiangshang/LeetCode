/*
    Author: jgz
    Date: 2018/7/6 10:42:04
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXN 1000

struct ListNode {
	int val=0;
	struct ListNode *next=NULL;
};
struct ListNode* creatList(int *array ,int len,ListNode* ret){
	int i;
	for(i=0;i<len-1;i++){
		ret[i].val=array[i];
		ret[i].next=&ret[i+1];
	}
	ret[i].val=array[i];
	ret[i].next=NULL;
	return ret;
}
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    int count=0;
    struct ListNode* P1=head,*P2=NULL;// pre delete Node
    while(count!=n&&P1!=NULL){
    	P1=P1->next;
    	count++;
	}
	if(P1==NULL) return head->next;// delete first node
	P2 = head;
	while(P1->next!=NULL){
		P1=P1->next;
		P2=P2->next;
	}
	// delete
	P2->next=P2->next->next;	
}
int main() {
	const char *fname="dataIn.txt";
	FILE *fp;
	int array[MAXN];
	if((fp=fopen(fname,"r"))==NULL) {
		printf("打开文件%s错误\n",fname);
		return NULL;
	}
	int len,N;
	while(fscanf(fp,"%d %d",&len,&N)==2) {
		for(int i=0; i<len; i++)
			fscanf(fp,"%d",&array[i]);
		struct ListNode ret[len+1];
		struct ListNode* head=creatList(array,len,ret);
		removeNthFromEnd(head,N);
		while(head!=NULL){
			printf("%d",head->val);
			head = head->next;
		}
	}
	return 0;
}

