#include<stdio.h>
#include<stdlib.h>
void insertionSort(int arr[],int n){
    for(int i=0; i<n; i++){
        int key = arr[i];
        int  j=i-1;
        while(j>=0&&arr[j]>key){
            arr[j+1] = arr[j];
            j=j-1;
        }
        arr[j+1]=key;
    }
}
void printArray(int arr[],int n){
    for(int i=0; i<n ;i++){
        printf("%d ",arr[i]);
    }
}
int main(){
    int n;
    printf("Enter Array Size  :");
    scanf("%d",&n);
    int arr[n];
    printf("Enter Array Elements :");
    for(int i=0; i<n; i++){
        scanf("%d",&arr[i]);
    }
    insertionSort(arr,n);
    printArray(arr,n);
    return 0;
}
