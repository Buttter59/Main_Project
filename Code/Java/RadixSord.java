import java.util.Arrays;
class Main {
    public static void main(String[] args) {
        
        int[] arr = {141, 392, 749, 100, 10, 0, 1404};
        System.out.println("Original: " + Arrays.toString(arr) + "\n");
        radixSort(arr);
        
    }
    static void radixSort(int[] arr) { 
        int max = Arrays.stream(arr).max().getAsInt();
        
        for (int exp = 1; max/exp > 0; exp *= 10) {
            System.out.println("Pass Unit Digit (" + exp + "s)");
            System.out.println("Before: " + Arrays.toString(arr));
            countingSort(arr, exp);
            System.out.println("After: " + Arrays.toString(arr) + "\n");
        }
    }
    static void countingSort(int[] arr, int exp) {
        boolean cond = false;
        
        
        int n = arr.length;
        int[] output = new int[n];
        int[] count = new int[10];
        for (int i = 0; i < n; i++) count[(arr[i]/exp) % 10]++;
        
            
        for (int i = 1; i < 10; i++) count[i] += count[i-1];
        
        if (cond == true) {
        for (int i = 0; i < n; i++) {
            output[n - count[(arr[i] / exp) % 10]] = arr[i];
            count[(arr[i] / exp) % 10]--;
        }} 
        
        else if (cond == false){
            for (int i = n - 1; i >= 0; i--) {
                output[count[(arr[i] / exp) % 10] - 1] = arr[i];
                count[(arr[i] / exp) % 10]--;
            }
        }
        
        for (int i = 0; i < n; i++) arr[i] = output[i];
        
    }
    
}
