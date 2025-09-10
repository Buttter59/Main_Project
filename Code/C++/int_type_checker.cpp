#include <iostream>
using namespace std;
int main () {
    cout << "-----Number & Age Checker-----\n";
    cout << "1. Check a number\n2. Check your age\n";
    
    char option;
    cout << "Enter the number of selected option (1 or 2): ";
    cin >> option;

    int num;

    switch (option) {
        case '1': {
        cout << "-----Number Checker-----\n";
        cout << "Enter your number: ";
        cin >> num;
        if (num == 0){
            cout << num << " Your number is a zero";
        }
        else if (num >= 1) {
            cout << num << " Your number is a positive";
        }
        else {
            cout << num << " Your number is a negative";
        }
        break;
        }


        case '2':{
        cout << "-----Age Checker-----";
        int age;
        cout << "Enter your age: ";
        cin >> age;
        if (age <= 17  && age > 0) {
            cout << "You are " << age << ", so you are a minor";
        }

        else if (age >= 18) {
            cout << "You are "<< age << ", so your are an adult";
        }
        else {
            cout << "Wtf are you";
        }   
        break;
        }

        default:{
        cout << "Invalid Input. Please Enter either 1 or 2";
        }

    }
}