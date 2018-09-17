/*
    Author: jgz
    Date: 2018/7/6 16:11:08
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXN 1024
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

//struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2) {
//	struct ListNode* mergeList=(struct ListNode*)malloc(sizeof(struct ListNode)*20000);
////struct ListNode mergeList[20000];
//	int temp=0;
//	while(l1!=NULL&&l2!=NULL) {
//		if(l1->val<l2->val) {
//			mergeList[temp].val=l1->val;
//			l1=l1->next;
//		} else {
//			mergeList[temp].val=l2->val;
//			l2=l2->next;
//		}
//		mergeList[temp].next=&mergeList[temp+1];
//		temp++;
//	}
//	while(l1!=NULL) {
//		mergeList[temp].val=l1->val;
//		mergeList[temp].next=&mergeList[temp+1];
//		l1=l1->next;
//		temp++;
//	}
//	while(l2!=NULL) {
//		mergeList[temp].val=l2->val;
//		mergeList[temp].next=&mergeList[temp+1];
//		l2=l2->next;
//		temp++;
//	}
//	mergeList[temp-1].next=NULL;
//	return mergeList;
//}
struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2) {
	struct ListNode* mergeList=(struct ListNode*)malloc(sizeof(struct ListNode));
	mergeList->next = NULL;
	struct ListNode* temp=mergeList;
	while(l1!=NULL&&l2!=NULL) {
		if(l1->val<l2->val) {
			temp->next = l1;
			temp=temp->next;
			l1 = l1->next;
		} else {
			temp->next = l2;
			temp=temp->next;
			l2 = l2->next;
		}

	}
	while(l1!=NULL) {
		temp->next = l1;
		temp=temp->next;
		l1 = l1->next;
	}
	while(l2!=NULL) {
		temp->next = l2;
		temp=temp->next;
		l2 = l2->next;
	}
	return mergeList->next;
}
int main() {
	const char *fname="dataIn.txt";
	FILE *fp;
	int M,N;
	int array1[MAXN],array2[MAXN];
	if((fp=fopen(fname,"r"))==NULL) {
		printf("打开文件%s错误\n",fname);
		return NULL;
	}
	while(fscanf(fp,"%d %d",&M,&N)==2) {
		for(int i=0; i<M; i++)
			fscanf(fp,"%d",&array1[i]);
		for(int i=0; i<N; i++)
			fscanf(fp,"%d",&array2[i]);
		struct ListNode ret1[M+1],ret2[N+1];
		struct ListNode* l1=creatList(array1,M,ret1);
		struct ListNode* l2=creatList(array2,N,ret2);
		struct ListNode* head=mergeTwoLists(l1,l2);
		while(head!=NULL) {
			printf("%d ",head->val);
			head = head->next;
		}
	}
	return 0;
}

