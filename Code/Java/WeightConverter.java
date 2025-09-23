import java.util.Scanner;

public class WeightConverter {
    public static void main(String[]args){
        Scanner scanner = new Scanner(System.in);
        int choice;
            
        do{System.out.println("----- Weight Converter -----");
            System.out.println("1. Kilogram to Pound\n2. Pound to Kilogram\n3. Exit Program");
            System.out.print("Enter choice: ");
            choice = scanner.nextInt();
  
            
            switch(choice){
            case 1:
            System.out.println("----- Kilogram to Pound -----");
            System.out.print("Enter weight in kg: ");
            double kilo = scanner.nextFloat();
            double kgtolb = kilo * 2.205;
            System.out.println("Converting your number...");
            System.out.println("Your number "+kilo+"kg is converted to "+kgtolb + "lbs");
            break;

            case 2:
            System.out.println("----- Pound to Kilogram -----");
            System.out.print("Enter weight in lbs: ");
            double lbs = scanner.nextFloat();
            double lbtokg = lbs / 2.205;
            System.out.println("Converting your number...");
            System.out.println("Your number "+lbs+"lbs is converted to "+lbtokg + "kg");
            break;

            case 3:
            System.out.println("Exiting Program...");

            break;
            
            default:
            System.out.println("Invalid Input. Enter a valid input.");
            break;
        }
    }while(choice != 3);

    }
}