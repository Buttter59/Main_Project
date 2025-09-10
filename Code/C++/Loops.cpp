#include <iostream>

using namespace std;

int main (){


    int num;
    while (true){
        cout << "Enter a number: ";
        cin >> num;

        if (num < 0 ) {
            cout << "You entered a negative number";
            break;
        }
    }
    cout << "\nout";

    
}