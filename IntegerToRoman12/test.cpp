/*
    Author: jgz
    Date: 2018/6/29 14:35:38
*/

#include<stdio.h>
#include<string.h>
int main()
{
 char destination[25];
 const char  *zhang="zhang ",*er="",*xiong="xiong";
 strcpy(destination,zhang);//这相当于初始化
 strcat(destination,er);
 strcat(destination,xiong);
int value[90]={0};
	value['I']=1;
	printf("%d",value[73]);
 printf("%s\n",destination);
 printf("M=%d,D=%d,C=%d,L=%d,X=%d,V=%d,I=%d\n",'M','D','C','L','X','V','I');
 return 0;
}

