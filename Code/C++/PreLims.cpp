#include <iostream>
using namespace std;

int main() {
    cout << "Enter number of customers: ";
    int num_customers;
    cin >> num_customers;
    
    int num_items;
    double price = 0;
    double f_price = 0; 
    double num1,num2,num3;
    double total3;
    double grandtotal;
    double average;
    
    for(int i = 1; i <= num_customers; i++){
        cout << "\nCustomer " << i << endl;
        cout << "Enter number of items: ";
        cin >> num_items;
        
        double ttl_percustomer = 0;
        
        for (int x = 1; x <= num_items; x++){
            cout << "Enter price for item "<<x<<": ";
            cin >> price;
            
            ttl_percustomer = ttl_percustomer + price; 
            if(ttl_percustomer >= 1000){f_price = ttl_percustomer * 0.90;}
            else{f_price = ttl_percustomer;}
            
        }
        grandtotal += f_price;
        average = grandtotal / num_customers;
        
        cout << "Total price: "<< ttl_percustomer << endl;
        if(ttl_percustomer >= 1000){cout<< "Discount: 10%" << endl;}
        else{cout << "Discount: N/A" << endl;}
        cout << "Final Price: " << f_price << endl;
        
        if (i == 1){num1 = num1 + f_price;}
        if (i == 2){num2 = num2 + f_price;}
        if (i == 3){num3 = num3 + f_price;}
        total3 = num1 + num2 + num3;
    }
    cout << "\nTotal price of first 3 customers: " << total3 << endl;
    cout << "Grand total: " << grandtotal << endl;
    cout << "Average: " << average << endl;
    
}
