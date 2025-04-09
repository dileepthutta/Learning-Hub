import java.util.*;
public class InsertionSort {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("Enter Number of Elements :");
        int n = s.nextInt();
        int [] arr = new int[n];
        System.out.println("Enter Array values :");
        for(int i=0; i<n; i++){
            arr[i] = s.nextInt();
        }
        for(int i=1; i<n; i++){
            int key = arr[i];
            int j = i-1;
            //Move Elements That are Greater than key in one posotion ahead.
            while (j>=0&&arr[j]>key) {
                arr[j+1] = arr[j];
                j = j -1;
            }
            arr[j+1] = key;
        }
        System.out.println("Sorted Array :");
        for(int i=0; i<n; i++){
            System.out.println(arr[i]+" ");
        }
    }
}
