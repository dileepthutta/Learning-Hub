#include<stdio.h>
#include<stdlib.h>
void selectSort(int arr[], int n) {
    for(int i = 0; i < n - 1; i++) {
        int min = i;
        for(int j = i + 1; j < n; j++) {
            if(arr[j] < arr[min]) {
                min = j;
            }
        }
        // Swap outside the inner loop
        int temp = arr[i];
        arr[i] = arr[min];
        arr[min] = temp;
    }
}

void printArray(int arr[],int n){
    for(int i = 0; i < n; i++){
        printf("%d\t",arr[i]);
    }
}
int main(){
    int arr[10],n;
    printf("Enter array size :");
    scanf("%d",&n);
    for(int i = 0;i < n; i++){
        scanf("%d",&arr[i]);
    }
    selectSort(arr,n);
    printArray(arr,n);
    return 0;
}
