
//This is just a guideline for doing your asg. You need to decide which functions will be passed by ref,
// and which will be passed by value. Note that you are not allowed to use global variables.
// That is why I have declared everything in main program. 

// Dr. Rohitash Chandra - hope you remove my name when u submit this work ;-)

#include <iostream>
#include <math.h>
#include <string>

using namespace std;
 


//--------------------

  void ShowMenu(){

  
  }

 void MakeSelection(){


 }

 int ReturnChange(int change,int Coins[],int NumCoins[]){

 int i=0;
 //while (change !=0){
       
     //  }
 
 
 }

void DisplayErrorMessage(){


}

void PrintConfidentialInformation(int Denominations, int Items, int Coins[], int NumCoins[], int ItemPrice[] , int NumItems[]){ 
//just to check if machine is working well

   cout<<" coins"<<endl;
  for(int i = 0; i < Denominations; i++){
    cout<< Coins[i]<<" ";
  }
    cout<<endl;

  for(int i = 0; i < Denominations; i++){
    cout<< NumCoins[i]<<" ";
  }
    cout<<endl;

   cout<<" Items"<<endl;

  for(int i = 0; i < Items; i++){
    cout<< ItemPrice[i]<<" ";
  }
    cout<<endl;

  for(int i = 0; i < Items; i++){
    cout<< NumItems[i]<<" ";
  }
    cout<<endl;

}

int main ()
{ 

//declare nd initialise the items and coin stacks

  int Denominations = 5;

  int Coins[] = {100, 50, 20, 10, 5};
  int NumCoins[] = {10, 10, 10, 10, 10}; //assume we have 10 coins of each denomination

  const int Items = 9;

  int ItemPrice[ ] = { 75, 120, 120, 100, 150, 95, 110, 50, 120 }; //price in cents
  int    NumItems[ ] = { 10, 10, 10, 10, 10, 10, 10, 10, 10 }; 
 
//ask for input of coins -- you can ask the user to enter something like 2.75, and then you should assume
// that it has 2 1 dollar coins, 1 50 cents, 1 20 cents and 1 5 cents. 
  //Need to write a while loop and use % and / operators to find how many of those coins are present.
  // Later you would need to increment the coins in NumCoins[]. You should also give appropriate error messages if the input is illegal. 

//make selection -- you will ask user for input, like if the user wants 2 x water and 4 x candy, then the user can enter "224444".
// call this function and pass this encoded  information eg. "224444" (either string or int), then decode it- meaning that you will need 
  //to separate the values - calculate the total cost from ItemPrice[ ] and update your NumItems[ ].

//do the rest

 

//repeat 

        ReturnChange(155,Coins,NumCoins);

    





//just checking the items and coins:_ Not needed in Asg, but I wanted to show you how to pass Arrays as Parameter to functions. Note that in C++, Arrays are passed by REFERENCE by default. 

     PrintConfidentialInformation(Denominations,Items, Coins, NumCoins, ItemPrice, NumItems); //see the style, how the arrays are passed as parameters...








 // system ("pause");
  return 0;

 //system("pause");

}
