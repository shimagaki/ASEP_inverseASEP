# -*- coding: utf-8 -*- 
import numpy as np
import matplotlib.pyplot as plt
"""periodic boundary condition"""
K = 10; L = 15 

class Particle_Class:
    def __init__(self,i,x,mu,n):
        self.id = i 
        self.x=x
        self.mu = mu 
        self.n = n 
    
    def set_x(self,x):
        self.x = x 
    
    def get_x(self):
        return self.x
    
    def set_n(self,n):
        self.n = n

    def get_n(self):
        return self.n
    
    def get_mu(self):
        return self.mu
    
    
def init_particles():
    global particles
    
    #------ location -------#
    location = np.arange(L)
    np.random.shuffle(location)
    location = np.sort( np.copy(location[:K]) )   #ex. 0,1,2,3,4,5 -> 0,2,3,5
    
    #------ transfer coefficient -------#
    trans_coeff = np.random.uniform(0,1,K)
    trans_coeff = np.copy(trans_coeff) / np.sum(trans_coeff)
    for i in range(K):
        vacancy_i = ( location[(i+1)%K]-location[i] + L ) % L - 1 
        particles.append( Particle_Class( i, location[i], trans_coeff[i], vacancy_i ) )

def update():
    global particles,f_vacancy 
    for i in range(K):
        if( np.random.uniform() < particles[i].get_mu() ):
             f_vacancy.write( str(1)+" " )   
        else:
             f_vacancy.write( str(0)+" " )   
    f_vacancy.write("\n")   

if __name__ == "__main__":
    particles = []
    init_particles()
    
    sample_size =  10000
    #fname_location = "location_K"+str(K)+"_L"+str(L)+"_N"+str(sample_size)+"_every_T1step.dat" 
    fname_vacancy = "simple_vacancy_K"+str(K)+"_L"+str(L)+"_N"+str(sample_size)+"_every_T1step.dat"
    fname_trans_coeff = "simple_trans_coeff_K"+str(K)+"_L"+str(L)+"_N"+str(sample_size)+"_every_T1step.dat"
    #f_location = open(fname_location,"w")
    f_vacancy = open(fname_vacancy,"w")
    f_trans_coeff = open(fname_trans_coeff,"w")
    
    for i in range(K):f_trans_coeff.write( str(particles[i].mu) + " " )
    f_trans_coeff.close()
    
    t_wait = 10
    for t in range(sample_size*t_wait):
        update()
    
    f_vacancy.close()
