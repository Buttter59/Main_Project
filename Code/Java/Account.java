import java.util.Scanner;

public class Account{
    public static void main(String[]args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("----- Gmail -----");


        System.out.println("----- Register to Gmail -----");
        System.out.print("Register username: ");
        String username = scanner.nextLine();

        System.out.print("Register password: ");
        String password = scanner.nextLine();


        System.out.println("----- Login to Gmail -----");
        System.out.print("Enter username: ");
        String inputuser = scanner.nextLine();

        System.out.print("Enter password: ");
        String inputpass = scanner.nextLine();

        if (password.equals(inputpass) && username.equals(inputuser)){
            System.out.println("Successfully Loged In.");
        }

        else{
            System.out.println("Incorrect password or username!");
        }
    }
}