import java.util.Scanner;

public class Atm {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int choice;
        int balance = 1000;

        do {
            System.out.println("----- ATM MENU -----");
            System.out.println("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit");
            System.out.print("Enter choice: ");

            choice = scanner.nextInt();
            switch(choice){
                case 1:
                System.out.print("Enter amount to deposit: ");
                int deposit = scanner.nextInt();
                balance = balance + deposit;
                System.out.println("Deposit successfull New balnce: " + balance);
                break;

                case 2:
                System.out.print("Enter amount to withdraw: ");
                int withdraw = scanner.nextInt();
                if (withdraw <= balance){
                    balance = balance - withdraw;
                    System.out.println("Withdrawal successfull New balance: " + balance); 
                }
                else{
                    System.out.println("Insufficient balance. Please enter a valid amount.");
                }
                break;

                case 3:
                System.out.println("Your balance is: " + balance);
                break;

                case 4:
                System.out.println("Exiting atm...");
                break;

                default:
                System.out.println("Invalid input! Enter a valid input");
            }
        } while (choice != 4);
    }
}