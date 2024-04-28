// import java.util.Scanner; Optional import originally used with Scanner code. 

public class task2 {
    public static void main(String[] args){
        /*
         * Optional Scanner code to read input from user
         * Removed due to worries over constraints as to not utilize built-in java classes or methods
         */
        // Scanner reader = new Scanner(System.in);
        // System.out.println("Enter the amount of numbers you would like to print: \n");
        // final int fibNumCount = reader.nextInt(); 

        final int fibNumCount = 10; // Adjust this value to change the amount of fibonacci numbers to print, If using Scanner code remove this line.
        int prev1 = 0; // Initialize variable for first previous value
        int prev2 = 1; // Initialize variable for second previous value
        int next = 0; // Initialize the next value

        System.out.println("Fibonacci Sequence: "); // Base fibonacci sequence output loop, comment out if scanner code is in use. 
        for (int i = 0; i < fibNumCount; i++) {
            System.out.println(" " + prev1);
            next = prev1 + prev2;
            prev1 = prev2;
            prev2 = next;
        }

        /* 
         * Removed if statement checks as Scanner code is no longer used, uncomment if Scanner code is in use. 
        if (fibNumCount <= 0) { // Check for invalid integer
            System.out.println("Invalid integer");
        }
        else if (fibNumCount == 1) { // Case for single print of fib sequence 
            System.out.println("Fibonacci Sequence: ");
            System.out.println(" " + prev1);
        }
        else { // Everything else
            System.out.println("Fibonacci Sequence: ");
            for (int i = 0; i < fibNumCount; i++) {
                System.out.println(" " + prev1);
                next = prev1 + prev2;
                prev1 = prev2;
                prev2 = next;
            }
        }
        */
        // reader.close(); Removed due to Scanner code no longer being used, uncomment if scanner code is in use. 
    }
}
