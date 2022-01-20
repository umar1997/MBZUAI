#Credits: Percy Liang, Dorsa Sadigh




import numpy as np # import numpy

############################################################
############################################################


# Lets define an Optimization problem

trainExamples = [   
    (1, 1),
    (2, 3),
    (4, 3),
]    # Some training examples (in this case they are three)                 

def phi(x): # Feature extractor
    return np.array([1, x])

def initialWeightVector(): # Initialize the weights 
    return np.zeros(2)

def trainLoss(w): # Squared loss 
    
    sum1=0
    for x,y in trainExamples:
        sum1 = sum1 + (w.dot(phi(x)) - y)**2 # residual squared loss

    loss_val = 1.0 / len(trainExamples) * sum1

    return loss_val


def gradientTrainLoss(w): # Computing the gradient of the loss w.r.t weights

    sum1=0
    for x,y in trainExamples:
        sum1 = sum1 + 2 * (w.dot(phi(x)) - y) * phi(x) # gradient of loss function w.r.t w

    gd_val = 1.0 / len(trainExamples) * sum1

    return gd_val

############################################################
############################################################




# Now we define our Optimization algorithm to find the weight vector

def gradientDescent(F, gradientF, initialWeightVector):
    w = initialWeightVector()
    eta = 0.1
    
    for t in range(10000):
        value = F(w) # loss compuatation
        gradient = gradientF(w) # gradient over w
        w = w - eta * gradient # update of w using gradient
        print("epoch {}: w = {}, F(w) = {}, gradientF = {}".format(t, w, value, gradient))

gradientDescent(trainLoss, gradientTrainLoss, initialWeightVector)
