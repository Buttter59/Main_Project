public class code2 {
    public static void main(String[] args){
        System.out.println("-----Java Basics-----");
        
        //Basic Math 
        int num1 = 89;
        int num2 = 32;
        double num3 = 5;
        int sum = num1 + num2;
        int subs = num1 - num2;
        double mult = num1 * num3;
        double div = num1 / num3;

        
        System.out.println("The number is: " + num1 + " and " + num2);
        System.out.println("The sum of " + num1 + " and " + num2 + " is " + sum);
        System.out.println("The difference of " + num1 + " and " + num2 + " is " + subs);
        System.out.println("The multiplication of " + num1 + " and " + num3 + " is " + mult);
        System.out.println("The division of " + num1 + " and " + num3 + " is " + div);

        // Student info
        String name = "Alland Obciana";
        int age = 19;
        double gpa = 1.52;
        float idstud =  (float) 2123.3144;
        char middle_initial = 'S';
        boolean IsStudent = true;
    
        System.out.println("\n------Student Info-----");
        System.out.println("Name: \t\t\t"+ name);
        System.out.println("Age: \t\t\t" + age);
        System.out.println("Grades: \t\t" + gpa);
        System.out.println("Middle Initial: \t" + middle_initial);
        System.out.println("Enrolled: \t\t" + IsStudent);
        System.out.println("Student Id: \t\t" + idstud);
    }

}