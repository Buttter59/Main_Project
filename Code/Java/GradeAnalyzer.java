import java.util.Scanner;

public class GradeAnalyzer {
    public static void main (String []args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("-----Grade Analyzer-----");
        System.out.print("Enter number of students: ");
        int num_students = scanner.nextInt();

        int excell = 0;
        int pass = 0;
        int fail = 0;
        double sum = 0;
        int highest = -1;
        int lowest = 101;  

        for (int i = 1; i <= num_students; i++){
            System.out.print("Enter grade for student "+ i + ": ");
            double grade = scanner.nextDouble();
            
    

            if (grade >= 90){
                System.out.println("Excellent");
                excell +=1;
                sum = sum + grade;
            }
            else if (grade >= 75){
                System.out.println("Passed");
                pass += 1;
                sum = sum + grade;
            }
            else {
                System.out.println("Failed");
                fail += 1;
                sum = sum + grade;
            }

        if (grade > highest) highest = (int)grade;
        if (grade < lowest ) lowest = (int)grade;

        }
    double average = sum / num_students;
    
    System.out.println("====== Result ======");
    System.out.println("Excellent: "+ excell);
    System.out.println("Passed: "+ pass);
    System.out.println("Failed: "+ fail+ "\n");
    System.out.println("Average Grade: "+ average);   
    System.out.println("Highest Grade: " + highest);
    System.out.println("Lowest Grade: "+ lowest); 
    }
}