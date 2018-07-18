/*
    Author: jgz
    Date: 2018/7/9 9:18:26
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXN 1000

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

struct ListNode* splitLists(struct ListNode** lists,int low,int high ) {
	if(low<high) {
		if(low+1==high) return mergeTwoLists(lists[low],lists[high]);
		int mid = (low+high)/2;
		struct ListNode* l1 = splitLists(lists,low,mid);
		struct ListNode* l2 = splitLists(lists,mid+1,high);
		return mergeTwoLists(l1,l2);
	}
	else return lists[low];
}
struct ListNode* mergeKLists(struct ListNode** lists, int listsSize) {
	if (listsSize==0) return NULL;
	return splitLists(lists,0,listsSize-1);
}
int main() {
	const char *fname="dataIn.txt";
	FILE *fp;
	char Nlist;
	if((fp=fopen(fname,"r"))==NULL) {
		printf("打开文件%s错误\n",fname);
		return NULL;
	}
	while(fscanf(fp,"%d",&Nlist)==1) {
		int len[Nlist];
		struct ListNode **lists =(struct ListNode **)malloc(sizeof(struct ListNode *)*Nlist);
		for(int i=0; i<Nlist; i++) {
			fscanf(fp,"%d",&len[i]);
		}
		struct ListNode ret[Nlist][MAXN];
		int array[Nlist][MAXN]= {0};
		for(int i=0; i<Nlist; i++) {
			for(int j=0; j<len[i]; j++)
				fscanf(fp,"%d",&array[i][j]);
			lists[i] = creatList(array[i],len[i],ret[i]);
		}
		struct ListNode* merList = mergeKLists(lists,Nlist);
		struct ListNode *head=merList;
		while(head!=NULL) {
			printf("%d ",head->val);
			head = head->next;
		}
	}
	return 0;
}

