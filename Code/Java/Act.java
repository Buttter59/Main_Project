import java.util.Scanner;

public class Act{
    public static void main (String[]args){
        System.out.println("-----Acttivity------");
        System.out.println("1. number checker\n2. age checker");
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter selected option: ");
        int choice = scanner.nextInt();
        switch (choice){
            case 1:
            System.out.println("======Number Checker=====");
            System.out.print("Enter a nuber: ");
            int num = scanner.nextInt();

            if (num >0){
                System.out.println("number is a positive");

            }
            else if (num <0){
                System.out.println("number is a negative");
            }
            else{
                System.out.println("Number is a zero");
            }

            break;
            case 2:
            System.out.println("=======Age Checker======");
            System.out.print("Enter age: ");
            int age = scanner.nextInt();

            if (age >0 && age <= 17){
                System.out.println("You are a minor");

            }
            else if (age >= 18){
                System.out.println("You are an adult");
            }
            else {
                System.out.println("Invalid input! please enter a valid age.");

            }
            break;

            default:
            System.out.println("Invalid input! Please enter a valid choice.");
        }
    }
}