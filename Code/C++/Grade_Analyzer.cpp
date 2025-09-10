#include <iostream>
#include <vector>
using namespace std;

int main () {

    cout << "-----Grade Analyzer-----\n";
    int num_students;
    cout << "Enter number of students: ";
    cin >> num_students;
    cout << "\n";

    double average;
    double sum = 0;
    int pass = 0;
    int fail = 0;
    int excell = 0;
    double grade = 0;

    double highest = -1;
    double lowest = 101;

    for (int i = 1; i <= num_students; i++){
        double grade;
        cout << "Enter grade for student "<<i<<": ";
        cin >> grade;

        if (grade > highest) highest = grade;
        if (grade < lowest) lowest = grade;

        if (grade >= 90) {
            cout << "Excellent\n";
            excell += 1;
        }
        else if (grade >= 75) {
            cout << "Passed\n";
            pass += 1;
        }
        else {
            cout<< "Failed\n";
            fail += 1;
        }
    sum += grade;
    average = sum / num_students;

    }




    cout << "===== RESULT =====\n";
    cout << "Excellent: "<< excell << endl;
    cout << "Passed: " << pass << endl;
    cout << "Failed: " << fail << endl;
    cout << "______________________________________________\n";
    cout << "Average of: "<< average <<endl;
    cout << "Highest Grade: " << highest << endl;
    cout << "Lowest Grade: " << lowest << endl;

    

    
}