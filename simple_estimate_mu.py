# -*- coding: utf-8 -*- 
import numpy as np
import matplotlib.pyplot as plt

"""periodic boundary condition"""
K = 10; L = 15; sample_size = 10000 

#-------- given Data ---------#
data_vacancy = []; data_location = [] 
conjugat_mu = []; mu_tru = np.zeros(K)

#-------- parameter ---------#
mu_model = np.zeros(K) 

def read_data_file():
    global data_vacancy,data_location, mu_tru

    fname_vacancy = "simple_vacancy_K"+str(K)+"_L"+str(L)+"_N"+str(sample_size)+"_every_T1step.dat"
    fname_trans_coeff = "simple_trans_coeff_K"+str(K)+"_L"+str(L)+"_N"+str(sample_size)+"_every_T1step.dat"

    f_vacancy = open(fname_vacancy,"r")
    f_trans_coeff = open(fname_trans_coeff,"r")
    
    #----------- mu_tru -----------#
    coeff_line = f_trans_coeff.readlines()
    coeff_line = np.copy( coeff_line[0].split(" ") )
    mu_tru = np.copy(map(float, coeff_line[:K]))

    #----------- data_vacancy -----------#
    i = 0
    for line in f_vacancy:
        item = line.split(' ')
        del item[-1]

        vacancy_single_sample = np.copy(map(int,item) ) 
        if(i==0):
            data_vacancy = vacancy_single_sample
        if(i==1):
            data_vacancy = np.append([np.copy(data_vacancy)],[vacancy_single_sample],axis = 0)
        if(i>1):
            data_vacancy = np.append(np.copy(data_vacancy),[vacancy_single_sample],axis = 0)
        i += 1
    
    f_vacancy.close()
    f_trans_coeff.close()

def calc_mu_model():
    global data_vacancy, mu_model
    
    for k in range(sample_size):
        mu_model = mu_model + data_vacancy[k]
    mu_model = mu_model / float(sample_size)

def plot_model_and_true(mu_tru,mu_model):
    x = np.linspace(0,0.4,100)
    y = np.linspace(0,0.4,100)
    plt.plot(x,y)
    plt.scatter(mu_tru,mu_model)
    plt.xlabel("true parameter")
    plt.ylabel("model parameter")
    
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    read_data_file()
    calc_mu_model()
    
    mu_model = np.copy(mu_model) / np.sum(mu_model)
    
    print "\n"
    print "mu_tru=\n", mu_tru
    print "mu_model/sum(abs(mu_model)=\n",mu_model
    
    plot_model_and_true(mu_tru,mu_model) 
