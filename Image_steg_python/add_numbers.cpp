#include <iostream>
using namespace std;

int main()
{
	//declare the variables
	int num_one, num_two, result;
	
	//get user input
	cout<<"Enter First Number: ";
	cin>>num_one;
	
	cout<<"\nEnter Second Number: ";
	cin>>num_two;
	
	//add the two numbers
	result=num_one+num_two;
	
	//display result
	cout<<"The Total is: "<<result<<endl;
	
	//terminate the program
	return 0;
}

