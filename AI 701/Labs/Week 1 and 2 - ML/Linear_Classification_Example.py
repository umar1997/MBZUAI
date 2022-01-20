#Credits: Percy Liang, Dorsa Sadigh



import numpy as np


# Lets define an optimization problem

trainExamples = [
    # (x, y) pairs
    ((0, 2), 1),
    ((-2, 0), 1),
    ((1, -1), -1),
]

def phi(x):
    return np.array(x)

def initialWeightVector():
    return np.zeros(2)

def trainLoss(w):
    
    sum1=0
    for x,y in trainExamples:
        sum1 = sum1 + max(1 - w.dot(phi(x)) * y, 0) # hinge loss per training example

    loss_val = 1.0 / len(trainExamples) * sum1 # np.mean(sum1) average of all per-example training losses

    return loss_val

def gradientTrainLoss(w):
    
    sum1=0
    for x,y in trainExamples:
        if 1 - w.dot(phi(x)) * y > 0: # if 1 - margin > 0
            sum1 = sum1 + -phi(x) * y  
        else:
            sum1 = sum1 + 0 # all other cases 

    gd_val = 1.0 / len(trainExamples) * sum1

    return gd_val


# Now, we define our optimization algorithm

def gradientDescent(F, gradientF, initialWeightVector):
    w = initialWeightVector()
    eta = 0.1
    for t in range(500):
        value = F(w) # Train loss 
        gradient = gradientF(w) # Gradient 
        w = w - eta * gradient # update w based on gradient of loss function w.r.t. w
        print("epoch {}: w = {}, F(w) = {}, gradientF = {}".format(t, w, value, gradient)) # printing epoch #, weight, Loss, gradient  

gradientDescent(trainLoss, gradientTrainLoss, initialWeightVector)
