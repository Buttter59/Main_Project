#include <iostream>
using namespace std;
int main (){
    cout << "Enter number of Customer: ";
    int num_customer;
    cin >> num_customer;

    int num_items;
    double price_percustomer = 0;
    double grand_total = 0;
    double final_price = 0;
    
    double num1 = 0;
    double num2 = 0;
    double num3 = 0;
    double totalof3 = 0;

    double grandtotal = 0;
    double average = 0;

    for(int i = 1; i <= num_customer; i++){
        cout << "\nCustomer number " << i << endl;
        cout << "Enter number of items: ";
        cin >> num_items;

        double ttl_percustomer = 0;

        for (int x = 1; x <= num_items; x++){
            cout << "Enter price of item "<<x<<": ";
            cin >> price_percustomer;

        ttl_percustomer = ttl_percustomer + price_percustomer; 

        if (ttl_percustomer >= 1000){final_price = ttl_percustomer * 0.9;} 
        else{final_price = ttl_percustomer;}

        

        }
        grandtotal += final_price;
        average = grandtotal / num_customer;
        cout << "Total Price: " << (ttl_percustomer) << endl;   
        if (ttl_percustomer >= 1000){
            cout << "Discount: 10%"<<endl;;
            cout << "Final Price: "<<final_price<<endl;
        } 
        else{
            cout << "Discount: N/A"<<endl;
            cout << "Final Price: "<<final_price<<endl;
        } 

        if(i == 1){num1 += final_price;}
        if(i == 2){num2 += final_price;}
        if(i == 3){num3 += final_price;}
        totalof3 = num1 + num2 + num3;
    }
    
    cout << "\nTotal of first 3 customers: "<< totalof3 <<endl;
    cout << "Grand Total: " << grandtotal << endl;
    cout << "Average total price: " << average<<endl;
    



}
