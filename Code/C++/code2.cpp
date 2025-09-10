#include <iostream>

int main(){ 
    bool cond = true;
    while (cond == true){

    
    std::cout <<"\n-----Basic Calculator-----\n\n";
    std::cout <<"1.Addition\n2.Substraction\n3.Division\n4.Multiplication" << "\n\n";
    std::cout <<"Type the number of your selected operations: ";
    int select;
    std::cin >> select;

    if (select == 1){
        std::cout <<"\n-----Addition-----   \n " << std::endl;
        double anum1;
        double anum2;
        std::cout << "Enter first number: ";
        std::cin >> anum1;
        std::cout << "Enter second number: ";
        std::cin >> anum2;
        double sum = anum1 + anum2;
        std::cout << "The sum of "<< anum1 << " and " << anum2<< " is "<<sum; 
    }

    else if (select == 2){
        std::cout <<"\n-----Subtraction-----   \n " << std::endl;
        double snum1;
        double snum2;
        std::cout << "Enter first number: ";
        std::cin >> snum1;
        std::cout << "Enter second number: ";
        std::cin >> snum2;
        double subs = snum1 - snum2;
        std::cout << "The substracted number of "<< snum1 << " and " << snum2<< " is "<<subs;     
    }

    else if (select == 3){
        std::cout <<"\n-----Division-----   \n " << std::endl;
        double dnum1;
        double dnum2;
        std::cout << "Enter first number: ";
        std::cin >> dnum1;
        std::cout << "Enter second number: ";
        std::cin >> dnum2;
        double div = dnum1 / dnum2;
        std::cout << "The division of "<< dnum1 << " and " << dnum2<< " is "<<div; 
    }

    else if (select == 4){
        std::cout <<"\n-----Multiplication-----   \n " << std::endl;
        double mnum1;
        double mnum2;
        std::cout << "Enter first number: ";
        std::cin >> mnum1;
        std::cout << "Enter second number: ";
        std::cin >> mnum2;
        double mult = mnum1 * mnum2;
        std::cout << "The multiplication of "<< mnum1 << " and " << mnum2<< " is "<<mult<<"\n"; 
    }

    else{
        std::cout <<"Invalid choice. Please enter a number above.\n";
    }

    std::string choice;
    std::cout << "\nWould you like to use the calculator again? (yes or no): ";
    std::cin >> choice;

    if (choice == "yes"){
        cond = true;
    }
    else if (choice == "no"){
        cond = false;
    }
    else {
        std::cout << "Invalid input. will now exit out of calculator.";
          cond = false;
        }
        
    }
    
        return 0;
    


}