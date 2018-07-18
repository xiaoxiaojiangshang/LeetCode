/*
    Author: jgz
    Date: 2018/7/10 14:32:17
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXN 10000

struct ListNode {
	int val;
	struct ListNode *next;
};
struct ListNode* creatList(int *array ,int len,ListNode* ret) {
	int i;
	for(i=0; i<len-1; i++) {
		ret[i].val=array[i];
		ret[i].next=&ret[i+1];
	}
	ret[i].val=array[i];
	ret[i].next=NULL;
	return ret;
}
struct ListNode* reverse(struct ListNode* first,struct ListNode* last) {
	struct ListNode* pre = last;
	while( first != last) {
		struct ListNode* temp = first->next;
		if(pre!=last)
			first->next = pre;
		pre = first;
		first = temp;
	}
	first->next = pre;
	return last;
}
struct ListNode* reverseKGroup(struct ListNode* head, int k) {
	if(k==1) return head;
	if(head==NULL) return NULL;
	struct ListNode* kNode = head;
	int i;
	for(i=0; i<k-1&&kNode; i++) {
		kNode = kNode->next;
	}
	if(!kNode) return head;
	struct ListNode* nextHead = kNode->next;
	struct ListNode* newHead = reverse(head,kNode);
	head->next = reverseKGroup(nextHead,k);
	return newHead;
}

int main() {
	const char *fname="dataIn.txt";
	FILE *fp;
	int array[MAXN],N,k;
	if((fp=fopen(fname,"r"))==NULL) {
		printf("打开文件%s错误\n",fname);
		return NULL;
	}
	while(fscanf(fp,"%d %d",&N,&k)==2) {
		for(int i=0; i<N; i++)
			fscanf(fp,"%d",&array[i]);
		struct ListNode ret[N+1];
		struct ListNode *l1=creatList(array,N,ret);
		struct ListNode* head=reverseKGroup(l1,k);
		while(head!=NULL) {
			printf("%d ",head->val);
			head = head->next;
		}
	}
	return 0;
}

