import java.util.*;
public class BubbleSort {
    public static void main(String[] args) {
    Scanner s = new Scanner(System.in);
    System.out.println("Enter number of Elements");
    int n = s.nextInt();
    int [] arr = new int[n];
    System.out.println("Enter array values :");
    for(int i=0; i<n; i++){
        arr[i] = s.nextInt();
    }
    for(int i=0; i<n-1; i++){
        for(int j =0; j<n-i-1; j++){
            if(arr[j]>arr[j+1]){
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
    System.out.println("Array After Sorting :");
    for(int i=0; i<n; i++){
        System.out.println(arr[i]+" ");
    }
  }
}