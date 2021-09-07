# Rohitash Chandra, 2017 c.rohitash@gmail.conm

#https://github.com/rohitash-chandra
 

# ref: http://iamtrask.github.io/2015/07/12/basic-python-network/  
 

#Sigmoid units used in hidden and output  

# Numpy used: http://cs231n.github.io/python-numpy-tutorial/#numpy-arrays
 

 

import matplotlib.pyplot as plt
import numpy as np 
import random
import time
 
class Network:

	def __init__(self, Topo, Train, Test, MaxTime, Samples, MinPer, learnRate): 
		self.Top  = Topo  # NN topology [input, hidden, output]
		self.Max = MaxTime # max epocs
		self.TrainData = Train
		self.TestData = Test
		self.NumSamples = Samples

		self.learn_rate  = learnRate
 

		self.minPerf = MinPer
		
		#initialize weights ( W1 W2 ) and bias ( b1 b2 ) of the network
		np.random.seed() 
		self.W1 = np.random.uniform(-0.5, 0.5, (self.Top[0] , self.Top[1]))  
		#print(self.W1,  ' self.W1')
		self.B1 = np.random.uniform(-0.5,0.5, (1, self.Top[1])  ) # bias first layer
		#print(self.B1, ' self.B1')
		self.BestB1 = self.B1
		self.BestW1 = self.W1 
		self.W2 = np.random.uniform(-0.5, 0.5, (self.Top[1] , self.Top[2]))   
		self.B2 = np.random.uniform(-0.5,0.5, (1,self.Top[2]))  # bias second layer
		self.BestB2 = self.B2
		self.BestW2 = self.W2 
		self.hidout = np.zeros(self.Top[1] ) # output of first hidden layer
		self.out = np.zeros(self.Top[2]) #  output last layer

		self.hid_delta = np.zeros(self.Top[1] ) # output of first hidden layer
		self.out_delta = np.zeros(self.Top[2]) #  output last layer




	def sigmoid(self,x):
		return 1 / (1 + np.exp(-x))

	
	def softmax(self, x):
		# Numerically stable with large exponentials
		exps = np.exp(x - x.max())
		return exps / np.sum(exps, axis=0)

	def sampleEr(self,actualout):
		error = np.subtract(self.out, actualout)
		sqerror= np.sum(np.square(error))/self.Top[2] 
		 
		return sqerror

	def ForwardPass(self, X ): 
		z1 = X.dot(self.W1) - self.B1  
		self.hidout = self.sigmoid(z1) # output of first hidden layer   
		z2 = self.hidout.dot(self.W2)  - self.B2 
		self.out = self.sigmoid(z2)  # output second hidden layer

 



	def BackwardPass(self, input_vec, desired):   
		out_delta =   (desired - self.out)*(self.out*(1-self.out))  
		hid_delta = out_delta.dot(self.W2.T) * (self.hidout * (1-self.hidout)) #https://www.tutorialspoint.com/numpy/numpy_dot.htm  https://www.geeksforgeeks.org/numpy-dot-python/
  
		self.W2+= self.hidout.T.dot(out_delta) * self.learn_rate
		self.B2+=  (-1 * self.learn_rate * out_delta)

		self.W1 += (input_vec.T.dot(hid_delta) * self.learn_rate) 
		self.B1+=  (-1 * self.learn_rate * hid_delta) 

			
 
	
	def TestNetwork(self, Data, testSize, tolerance):
		Input = np.zeros((1, self.Top[0])) # temp hold input
		Desired = np.zeros((1, self.Top[2])) 
		nOutput = np.zeros((1, self.Top[2]))
		clasPerf = 0
		sse = 0  
		self.W1 = self.BestW1
		self.W2 = self.BestW2 #load best knowledge
		self.B1 = self.BestB1
		self.B2 = self.BestB2 #load best knowledge
 
		for s in range(0, testSize):
							
			Input  =   Data[s,0:self.Top[0]] 
			Desired =  Data[s,self.Top[0]:] 

			self.ForwardPass(Input ) 
			sse = sse+ self.sampleEr(Desired)  


			pred_binary = np.where(self.out > (1 - tolerance), 1, 0)
			
			if( (Desired==pred_binary).all()):
				clasPerf =  clasPerf +1   

			#if(np.isclose(self.out, Desired, atol=erTolerance).any()):
				#clasPerf =  clasPerf +1  

		return ( sse/testSize, float(clasPerf)/testSize * 100 )




	def saveKnowledge(self):
		self.BestW1 = self.W1
		self.BestW2 = self.W2
		self.BestB1 = self.B1
		self.BestB2 = self.B2  

	def BP_GD(self):  


		Input = np.zeros((1, self.Top[0])) # temp hold input
		Desired = np.zeros((1, self.Top[2])) 
 
  
		Er = [] 
		epoch = 0
		bestmse = 10000 # assign a large number in begining to maintain best (lowest RMSE)
		bestTrain = 0
		while  epoch < self.Max and bestTrain < self.minPerf :
			sse = 0
			for s in range(0, self.NumSamples):
		
				Input[:]  =  self.TrainData[s,0:self.Top[0]]  
				Desired[:]  = self.TrainData[s,self.Top[0]:]  

				self.ForwardPass(Input)  
				self.BackwardPass(Input ,Desired)
				sse = sse+ self.sampleEr(Desired)
			 
			mse = np.sqrt(sse/self.NumSamples*self.Top[2])

			if mse < bestmse:
				 bestmse = mse
				 print(bestmse, epoch, ' bestmse epoch')
				 self.saveKnowledge() 
				 (x,bestTrain) = self.TestNetwork(self.TrainData, self.NumSamples, 0.2)

			Er = np.append(Er, mse)
			
			epoch=epoch+1  

		return (Er,bestmse, bestTrain, epoch) 



def normalisedata(data, inputsize, outsize): # normalise the data between [0,1]
	traindt = data[:,np.array(range(0,inputsize))]	
	dt = np.amax(traindt, axis=0)
	tds = abs(traindt/dt) 
	return np.concatenate(( tds[:,range(0,inputsize)], data[:,range(inputsize,inputsize+outsize)]), axis=1)

def main(): 
					
		
	problem = 1 # [1,2,3] choose your problem (Iris classfication or 4-bit parity or XOR gate)
				

	if problem == 1:
		TrDat  = np.loadtxt("data/train.csv", delimiter=',') #  Iris classification problem (UCI dataset)
		TesDat  = np.loadtxt("data/test.csv", delimiter=',') #  
		Hidden = 6
		Input = 4
		Output = 2 #https://stats.stackexchange.com/questions/207049/neural-network-for-binary-classification-use-1-or-2-output-neurons
		TrSamples =  TrDat.shape[0]
		TestSize = TesDat.shape[0]
		learnRate = 0.1  
		TrainData  = normalisedata(TrDat, Input, Output) 
		TestData  = normalisedata(TesDat, Input, Output)
		MaxTime = 500


		 

	elif problem == 2:
		TrainData = np.loadtxt("data/4bit.csv", delimiter=',') #  4-bit parity problem
		TestData = np.loadtxt("data/4bit.csv", delimiter=',') #  
		Hidden = 6
		Input = 4
		Output = 1 #  https://stats.stackexchange.com/questions/207049/neural-network-for-binary-classification-use-1-or-2-output-neurons
		TrSamples =  TrainData.shape[0]
		TestSize = TestData.shape[0]
		learnRate = 0.9 
		MaxTime = 1000

	elif problem == 3:
		TrainData = np.loadtxt("data/xor.csv", delimiter=',') #  XOR  problem
		TestData = np.loadtxt("data/xor.csv", delimiter=',') #  
		Hidden = 3
		Input = 2
		Output = 2  # one hot encoding: https://machinelearningmastery.com/how-to-one-hot-encode-sequence-data-in-python/
		TrSamples =  TrainData.shape[0]
		TestSize = TestData.shape[0]
		learnRate = 0.5
		MaxTime = 500
 


	Topo = [Input, Hidden, Output] 
	MaxRun = 3 # number of experimental runs 
	 
	MinCriteria = 95 #stop when learn 95 percent

	trainTolerance = 0.2 # [eg 0.15 would be seen as 0] [ 0.81 would be seen as 1]
	testTolerance = 0.49
 

	trainPerf = np.zeros(MaxRun)
	testPerf =  np.zeros(MaxRun)

	trainMSE =  np.zeros(MaxRun)
	testMSE =  np.zeros(MaxRun)
	Epochs =  np.zeros(MaxRun)
	Time =  np.zeros(MaxRun)

	for run in range(0, MaxRun  ):
		print(run, ' is experimental run') 

		fnn = Network(Topo, TrainData, TestData, MaxTime, TrSamples, MinCriteria, learnRate)
		start_time=time.time()
		(erEp,  trainMSE[run] , trainPerf[run] , Epochs[run]) = fnn.BP_GD()   

		Time[run]  =time.time()-start_time
		(testMSE[run], testPerf[run]) = fnn.TestNetwork(TestData, TestSize, testTolerance)
	print(' print classification performance for each experimental run') 
	print(trainPerf)
	print(testPerf)
	print(' print RMSE performance for each experimental run') 
	print(trainMSE)
	print(testMSE)
	print(' print Epocs and Time taken for each experimental run') 
	print(Epochs)
	print(Time)
	print(' print mean and std of training performance') 
	

	print(np.mean(trainPerf), np.std(trainPerf))
	print(np.mean(testPerf), np.std(testPerf))

	print(' print mean and std of computational time taken') 
	
	print(np.mean(Time), np.std(Time))
	
	
				 
	plt.figure()
	plt.plot(erEp )
	plt.ylabel('error')  
	plt.savefig('out.png')
			 
 
if __name__ == "__main__": main()

