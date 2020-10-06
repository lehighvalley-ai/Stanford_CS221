# SU CS221 Lecture 1
# Gradient Descent Example
# Finding the best fit line using gradient descent 

# Finding the error
def F(w):
    return sum((w * x - y)**2 for x, y in points)
    
# Find the derivative
def dF(w):
    return sum(2*(w * x - y) * x for x, y in points)   

if __name__ == "__main__":

    points = [(2, 4), (4, 2)]
    w = 0
    eta = 0.01

    for t in range(100):
        value = F(w)
        gradient = dF(w)
        w = w - eta * gradient
        print('iteration {}: w = {}, F(w) = {}'.format(t, w, value))   