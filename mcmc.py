# MCMC
# Atomistic Modeling of Materials - Tutorial 3
#
# Markus Schoeberl
# m.schoeberl@tum.de
# Professur fuer Kontinuumsmechanik
# Technische Universitaet Muenchen
#
# February 2017
#




import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

def evalPDF(z):
  pdf =  0.25*mlab.normpdf(z, -3., np.sqrt(2.)) + 0.75*mlab.normpdf(z,2.,1.)
  return pdf

# mcmc

# initialize current and proposed state
q = 0.
q_prime = 0.

# set the variance of the proposal distribution
sigmaSq = 9.0
sigma = np.sqrt(sigmaSq)

# set the amount of samples
N = 100000
# store the samples
q_store = np.zeros(N)


count_accept = 0.0

for i in range(0,N):
  # make proposal move given the predecessor
  q_prop = np.random.normal(q, sigma)
  
  # calculate acceptance ratio
  a = np.log(evalPDF(q_prop)) - np.log(evalPDF(q))
  a = np.exp(a)
  
  if a >=1:
    q = q_prop
    count_accept = count_accept + 1
  elif np.random.rand() < a:
    q = q_prop
    count_accept = count_accept + 1
  
  # store the sample
  q_store[i] = q


print 'acceptance ratio'
print count_accept/N


# plot the true solution

x = np.linspace(-10,10,1000)
y = 0.25*mlab.normpdf(x, -3., np.sqrt(2.)) + 0.75*mlab.normpdf(x,2.,1.)
plt.plot(x,y, lw=2, ls='--', c='r', label='Truth')
plt.hist(q_store, normed=True, bins=100, histtype='step', color='k', lw='2', label='MCMC', alpha=0.7)
plt.legend()
plt.grid()
plt.savefig('mcmc.pdf')
plt.show()
