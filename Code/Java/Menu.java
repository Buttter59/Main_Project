import java.util.Scanner;

public class Menu {
    public static void main(String []args){
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("===== Menu Driven Program =====");
        System.out.println("1. Grade Checker\n2. Age Checker\n3. College Plan\n4. Exit");

        System.out.print("Enter selected option: ");
        int choice = scanner.nextInt();
        
        switch (choice){

            case 1:
            System.out.println("===== Grade Checker =====");
            System.out.print("Enter Grade: ");
            int grade = scanner.nextInt();
            if (grade >= 98){
                System.out.println(grade + " - Outstanding");
            }
            else if (grade >= 95){
                System.out.println(grade + " - Very Good");
            }
            else if (grade >= 90){
                System.out.println(grade + " - Outstanding");
            }
            else if (grade >= 80){
                System.out.println(grade + " - Satisfactory");
            }
            else if (grade >= 75){
                System.out.println(grade + " - Needs Improvement");
            }
            else{
                System.out.println(grade + " - Failed");
            }
            break;

            case 2:
            System.out.println("====== Age Checker =====");
            System.out.print("Enter Age: ");
            int age = scanner.nextInt();
            if (age >= 60){
                System.out.println(age + " - You are a Senior Citizen"); 
            }
            else if (age >= 18){
                System.out.println(age + " - You are an Adult"); 
            }
            else if (age >= 13){
                System.out.println(age + " - You are a Teenager"); 
            }
            else {
                System.out.println(age + " - You are a Child"); 
            }
            break;

            case 3:
            System.out.println("====== College Plan =====\n");
            System.out.println("\t\tCollege Requirements:");
            System.out.println("Full Scholarship: Grade 90 and above, Income of 50,000 above");
            System.out.println("Partial Scholarship: Grade 90 and above, Income of 30,000 above");
            System.out.println("Discount: Grade 95 and above, Income of 20,000 below");
            System.out.println("----------------------------------------------------------------");


            System.out.print("Enter Grade: ");
            int grades = scanner.nextInt();
            System.out.print("Enter Income: ");
            int income = scanner.nextInt();
            System.out.println("");

            if (grades >= 90 && income >= 50000) {
                System.out.println("Qualified for Full Scholarship");
            } 
            else if (grades >= 85 && income >= 30000) {
                System.out.println("Qualified for Partial Scholarship");
            } 
            else if (grades >= 95 && income <= 20000) {
                System.out.println("Qualified for Tuition Discount");
            }
            else {
                System.out.println("Not Qualified");
            }
            break;
            
            case 4:
            System.out.println("Exiting program...");
            break;

            default:
            System.out.println("Invalid input! Enter a valid input.");

        }
    

    }

}
