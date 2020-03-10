

# Neural networks pedagogical materials
# The following code is free to use and modify to any extent 
# (with no responsibility of the original author)

# Reference to the author is a courtesy
# Author : David Cornu => david.cornu@utinam.cnrs.fr



import numpy as np
from ext_module import *


nb_epochs = 100
control_interv = 1
hid_dim = 8
learn_rate = 0.2
out_dim = 7
beta = 1.0

nb_train = 1015 # over 1115


######################### ##########################
#          Loading data and pre process
######################### ##########################

raw_data = np.loadtxt("../../data/stellar_spectra/train.dat")
raw_target = np.loadtxt("../../data/stellar_spectra/target.dat")


nb_dat = np.shape(raw_data)[0]
in_dim = np.shape(raw_data)[1]

input = np.append(raw_data[:,:in_dim], -1.0*np.ones((nb_dat,1)), axis=1)
output = np.zeros(out_dim)
hidden = np.zeros(hid_dim+1)

targ = raw_target


input[:,:-1] -= np.mean(input[:,:-1], axis = 0)
input[:,:-1] /= np.max(np.abs(input[:,:-1]), axis = 0)

# split training and test dataset
input_test = input[nb_train:,:]
targ_test = targ[nb_train:,:]

input = input[0:nb_train,:]
targ = targ[0:nb_train,:]

nb_dat = nb_train


index = np.arange(0,nb_dat)

######################### ##########################
#          Initialize network weights
######################### ##########################

weights1 = np.random.rand(in_dim+1,hid_dim)*(0.02)-0.01
weights2 = np.random.rand(hid_dim+1,out_dim)*(0.02)-0.01


######################### ##########################
#                Main training loop
######################### ##########################
######################### ##########################

for t in range(0,nb_epochs):

	if (((t%control_interv) == 0)):
		print("\n#########################################################################")
		print("\nIteration :", t)
		confmat(input_test, targ_test, weights1, weights2, beta)

	np.random.shuffle(index)
	input = input[index,:]
	targ = targ[index,:]

	quad_error = 0.0
	######################### ##########################
	#             Training on all data once
	######################### ##########################
	for i in range(0,nb_dat):
		#Forward phase
		forward(input[i,:], hidden, output, weights1, weights2, beta)
		
		#Back-propagation phase
		backprop(input[i,:], hidden, output, targ[i,:], weights1, weights2, learn_rate, beta)

		quad_error += 0.5*sum((output[:] - targ[i,:])**2)
	
	if((t%control_interv) == 0):
		print("\nAverage training dataset quadratic error :", quad_error/nb_dat)


######################### ##########################
######################### ##########################














