import java.util.*;
public class SelectionSort {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter Number of Elements :");
        int n = scanner.nextInt();
        int [] arr = new int[n];
        System.out.println("Enter array Elements :");
        for(int i=0; i<n; i++){
            arr[i] = scanner.nextInt();
        }
        for(int i =0; i<n-1; i++){
            int minIndex = i;
            for(int j=i; j<n; j++){
                if(arr[j]<arr[minIndex]){
                    minIndex = j;
                }
            }
            int temp = arr[minIndex];
            arr[minIndex] = arr[i];
            arr[i] = temp;
        }
        System.out.println("Sorted Array :");
        for(int i=0;i<n; i++){
            System.out.println(arr[i]+" ");
        }
    }
}