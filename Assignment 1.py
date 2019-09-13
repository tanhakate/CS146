from scipy.stats import norm

sample_size = 100000 #we want a large sample to generate simulated values
parameter_values = [[0,1],[5,2],[-5,2]] #storing mu and sigma paramaters using list of lists

for par in parameter_values: #for each set of parameter values
    distribution = norm(loc=par[0], scale=par[1]) #create a Gaussian distribution with parameters in the set
    sample = distribution.rvs(size=sample_size) #sample from the distribution depending on pre-defined sample_size
    count = 0 #variable to store number of times we satisfy the inequality
    for idx in range(0,sample_size): #for each element in our sample
        if sample[idx]*sample[idx]*sample[idx] + 2*sample[idx] + 1 > 1: #check if f(x) is strictly greater than 1
            count = count + 1 #each time we satisfy the inequality, increment the value of count by 1
    print(count/float(sample_size)) #return the simulated probability


