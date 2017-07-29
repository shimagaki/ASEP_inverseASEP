# -*- coding: utf-8 -*- 
import numpy as np
import matplotlib.pyplot as plt
"""periodic boundary condition"""
K = 5; L = 10

class Particle_Class:
    """particles class 
    """
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
    global particles 
    for i in range(K):
        if(particles[i].n>0):
            if( np.random.uniform() < particles[i].get_mu() ):
    
                x = particles[i].get_x() 
                n = particles[i].get_n() 
                n_minus = particles[ (i-1+K)%K ].get_n() 
    
                particles[i].set_x( (x+1)%L )
                
                particles[i].set_n( n-1 )
                particles[ (i-1+K)%K ].set_n( n_minus + 1  )
    
def print_state():
    for i in range(K): 
        print i, ",", particles[i].id, ",",particles[i].x, ",", particles[i].mu, ",", particles[i].n

def output_state_to_file():
    global f_location, f_vacancy
    for i in range(K):
        f_location.write( str(particles[i].x) + " " )
        f_vacancy.write( str(particles[i].n) + " " )
    f_location.write("\n")
    f_vacancy.write("\n")

if __name__ == "__main__":
    particles = []
    init_particles()
    
    fname_location = "location_K10_L15_N1000000_Twait10.dat"
    fname_vacancy = "vacancy_K10_L15_N1000000_Twait10.dat"
    fname_trans_coeff = "trans_coeff_.dat"
    f_location = open(fname_location,"w")
    f_vacancy = open(fname_vacancy,"w")
    f_trans_coeff = open(fname_trans_coeff,"w")
    
    for i in range(K):f_trans_coeff.write( str(particles[i].mu) + " " )
    f_trans_coeff.close()
    
    sample_size =  100
    t_wait = 10
    for t in range(sample_size*t_wait):
        update()
        if(t%t_wait == 0):
            output_state_to_file()
    """  
    print_state() 
    print ""
    update()
    print_state() 
    """  

    f_location.close()
    f_vacancy.close()
