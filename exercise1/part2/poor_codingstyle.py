

# the goal here is to create some arrays so that you can do run some operations. 

# can you fix this and think of strategies to make this more creative, i.e generate some data and run some matrix operations and try to make some plots such as heatmaps and histograms?




import numpy as np 

samples = 20


weight_array = np.zeros(samples)
weight_array1 = np.zeros(samples)
weight_array2 = np.zeros(samples)
weight_array3 = np.zeros(samples)
weight_array4 = np.zeros(samples)
weight_array5 = np.zeros(samples)
weight_array6 = np.zeros(samples)
weight_array7 = np.zeros(samples)
weight_array8 = np.zeros(samples)
weight_array9 = np.zeros(samples)
weight_array10 = np.zeros(samples)
weight_array11 = np.zeros(samples)
weight_array12 = np.zeros(samples)




weight_array[0] = 0
weight_array1[0] = 0
weight_array2[0] = 0
weight_array3[0] = 0
weight_array4[0] = 0
weight_array5[0] = 0
weight_array6[0] = 0
weight_array7[0] = 0
weight_array8[0] = 0
weight_array9[0] = 0
weight_array10[0] = 0
weight_array11[0] = 0
weight_array12[0] = 0

temperature = 22



file_name =  'weight[0]_' + str(temperature) + '.txt'
np.savetxt(file_name, weight_array, fmt='%1.2f')

file_name =  'weight[100]_' + str(temperature) + '.txt'
np.savetxt(file_name, weight_array1, fmt='%1.2f')

file_name =   'weight[10000]_' + str(temperature) + '.txt'
np.savetxt(file_name, weight_array2, fmt='%1.2f')

file_name =  'weight[5000]_' + str(temperature) + '.txt'
np.savetxt(file_name, weight_array3, fmt='%1.2f')

file_name =  'weight[2000]_' + str(temperature) + '.txt'
np.savetxt(file_name, weight_array4, fmt='%1.2f')

file_name =  'weight[3000]_' + str(temperature) + '.txt'
np.savetxt(file_name, weight_array5, fmt='%1.2f') 


