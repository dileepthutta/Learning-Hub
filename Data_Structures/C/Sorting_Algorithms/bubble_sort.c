#include<stdio.h>
#include<stdlib.h>
void bubbleSort(int a[] ,int n){
    for(int i=0;i<n-1;i++){
        for(int j=0;j<n-i-1;j++){
            if(a[j]>a[j+1]){
                int temp = a[j];
                a[j] = a[j+1];
                a[j+1] = temp;
            }
        }
    }
}
void printArray(int a[], int n){
    for(int i=0;i<n;i++){
        printf("%d ",a[i]);
    }
}
int main(){
    int n;
    printf("Enter array size :");
    scanf("%d",&n);
    int a[n];
    printf("Enter array values :");
    for(int i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    bubbleSort(a,n);
    printf("Array after Sorting :");
    printArray(a,n);
    return 0;
}
