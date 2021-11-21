# Simple function to compute the average of a list of numbers.

def compute_average_function(l):
    n = len(l)
    
    if n == 0:
        return 0.0 
    
    return float(sum(l)/n)

