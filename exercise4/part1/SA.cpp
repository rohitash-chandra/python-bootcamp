/*******************************************************************************************
 
 Lab  :  Dr. Rohitash Chandra
 Desc :  Random number from Normal Distribution, using Box Muller Transform
	and Fitness Function implemented code is from the URLs below:
 Ref  : http://en.wikipedia.org/wiki/Box%E2%80%93Muller_transform
	http://elearn.usp.ac.fj
********************************************************************************************/

#include <stdio.h> 
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <math.h>
#include <vector>

using namespace::std;

int MCL = 100;

typedef vector<double> Layer;


double Prob(double ChangeInEnergy, double Tempr );
 
double FitnessFunc(Layer x, int ProbNum);
Layer GenerateNewSol(Layer Solution);
void SimulatedAnnealing(Layer SearchSpace,int MCL, double Tempr, double MinEnergy);

double RandNumberLimit(double Limit)
{

        int chance; 
      chance =rand()%2;

      if(chance ==0) 
      return  drand48() * Limit * -1;

      if(chance ==1) 
       return  drand48() * Limit;

}


int main ()
{
	srand (time(NULL)); //getting different # each time the prog is run

	//test random num
	//for (double num = 0; num < 10;num++)
		//cout << RandNormalDistri(num, 1) << endl;

	Layer SearchSpace(10);

	for (int i = 0 ; i < SearchSpace.size(); i++)
		SearchSpace[i] = RandNumberLimit(5);


	SimulatedAnnealing(SearchSpace,500,0.01,0.01);

	return 0;
}

//Random Number from Normal Distribution 

double FitnessFunc(Layer x, int ProbNum)
{

	double Fit = 0;

	//Ellipsoidal function
	if(ProbNum == 1)
	{
		for(int j = 0; j < x.size(); j++)
    		Fit += ((j+1) * (x[j] * x[j]));
	}

	//Schwefel's function
	else if(ProbNum == 2)
	{
		for(int j = 0; j < x.size(); j++)
		{
			double sumSCH = 0;
			for(int i = 0; i < j; i++)
				sumSCH += x[i];
			Fit += sumSCH * sumSCH;
		}
	}

	//Rosenbrock's function
	else if(ProbNum == 3)
	{
		for(int j = 0; j < x.size() - 1; j++)
			Fit += 100.0 * (x[j] * x[j] - x[j+1]) * (x[j] * x[j] - x[j+1]) + (x[j] - 1.0) * (x[j] - 1.0);
	}

	return Fit;

}

Layer GenerateNewSol(Layer Solution)
{

	int i;

	for(i = 0; i < Solution.size(); i++)
	{
		Solution[i] = Solution[i] +   RandNumberLimit(0.01); 
	}

	return Solution;

}

double Prob(double ChangeInEnergy, double Tempr ){

return min(1.0, (exp(-ChangeInEnergy / Tempr)));

}

void SimulatedAnnealing(Layer Solution, int MCL, double CoolingRate, double MinEnergy)
{

       ofstream out("out.txt");

        double  Tempr = 1000;

	double Energy; // give large energy value as it is compared in begining....
	Layer NewSolution;
	 
	double NewEnergy = 0;
	double ChangeInEnergy;

         int i = 0;

      Energy = FitnessFunc(Solution, 2);
      out<< Tempr<< " " <<Energy<< endl;


	while (Tempr>0.01)
	{
		 i = 0;

		while (i < MCL)
		{
			Energy = FitnessFunc(Solution, 2);
                     //     out<<Energy<<endl;
			NewSolution = GenerateNewSol(Solution);
                       
	                 

			NewEnergy = FitnessFunc(NewSolution, 2);

			ChangeInEnergy = NewEnergy - Energy;

			if (ChangeInEnergy <= 0)
			{
				Solution = NewSolution;
				Energy = NewEnergy;
			}
			
			if (Prob(ChangeInEnergy, Tempr) > drand48())
			{
				Solution = NewSolution;
				Energy = NewEnergy;
			}
			
			i++ ;
                       
               //   cout<< Tempr<< " " <<Energy<< endl;
		}
                 
                  cout<< Tempr<< " " <<Energy<< endl;

                    out<< Tempr<< " " <<Energy<<" " <<Prob(ChangeInEnergy, Tempr)<< endl;
               
                       for(int x = 0; x < Solution.size(); x++)
		        cout<< Solution[x] <<" ";
                       cout<<endl;
		 
		
		Tempr = Tempr - (Tempr * CoolingRate);// - cool/reduce the temp!
	}

 out.close();

}

