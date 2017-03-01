import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import math

def get_proposal(qold,mu,sigma):
    return qold+np.random.normal(mu, sigma,1)[-1]

def gaussian(mu,sigma,x):
    return 1/math.sqrt(2*math.pi*sigma*sigma)*math.exp(-pow((x-mu),2)/(2*sigma*sigma))

def eval_target(q):
    return 0.25*gaussian(-3,2,q)+0.75*gaussian(2,1,q)

q0=.1
sigma = .1
mu = 0
numsteps = 1000000

# store all values for q in a list
q=[q0]

for i in range(numsteps):
    q_prop=get_proposal(q[-1],mu,sigma)
    a=min(1,eval_target(q_prop)/eval_target(q[-1])  )
     
    # accept with ratio a
    if np.random.uniform()<a:
        q.append(q_prop)
    else:
        q.append(q[-1])


num_bins = 100;
fig, ax = plt.subplots()

# histogram of the data
n, bins, patches = ax.hist(np.array(q), num_bins, normed=1)

ax.set_xlabel('Value')
ax.set_ylabel('Probability density')
ax.set_title(r'Random Walk metropolis with $\sigma='+str(sigma)+'$')

x=np.linspace(-10,10,1000)
plt.plot(x,[eval_target(item) for item in x],'r--',linewidth=2.0)
plt.show()

