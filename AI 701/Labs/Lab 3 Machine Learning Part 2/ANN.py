import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))
    # Creating the Feed forward neural network
    # 1 Input layer(1, 30)
    # 1 hidden layer (1, 5)
    # 1 output layer(3, 3)


def f_forward(x, w1, w2):
    z1 = x.dot(w1)  # input from layer 1
    a1 = sigmoid(z1)  # out put of layer 2 # Output layer
    z2 = a1.dot(w2)  # input of out layer
    a2 = sigmoid(z2)  # output of out layer
    return a2


# initializing the weights randomly

def generate_wt(x, y):
    l = []
    for i in range(x * y):
        l.append(np.random.randn())
    return np.array(l).reshape(x, y)
    # for loss we will be using mean square error(MSE)


def loss(out, Y):
    s = (np.square(out - Y))
    s = np.sum(s) / len(Y)
    return s
    # Back propagation of error


def back_prop(x, y, w1, w2, alpha):
    z1 = x.dot(w1)  # input from layer 1
    a1 = sigmoid(z1)  # output of layer 2 # Output layer
    z2 = a1.dot(w2)  # input of out layer
    a2 = sigmoid(z2)  # output of out layer # error in output layer
    d2 = (a2 - y)
    d1 = np.multiply((w2.dot((d2.transpose()))).transpose(), (np.multiply(a1, 1 - a1)))  # Gradient for w1 and w2
    w1_adj = x.transpose().dot(d1)
    w2_adj = a1.transpose().dot(d2)
    w1 = w1 - (alpha * (w1_adj))
    w2 = w2 - (alpha * (w2_adj))
    return (w1, w2)


def train(x, Y, w1, w2, alpha=0.01, epoch=10):
    acc = []
    losss = []
    for j in range(epoch):
        l = []
        for i in range(len(x)):
            out = f_forward(x[i], w1, w2)
            l.append((loss(out, Y[i])))
            w1, w2 = back_prop(x[i], Y[i], w1, w2, alpha)
        if (j + 1) % 50 == 0:
            print("epochs:", j + 1, "======== acc:", (1 - (sum(l) / len(x))) * 100)
        acc.append((1 - (sum(l) / len(x))) * 100)
        losss.append(sum(l) / len(x))
    return acc, losss, w1, w2


def predict(x, w1, w2):
    Out = f_forward(x, w1, w2)
    maxm = 0
    k = 0
    for i in range(len(Out[0])):
        if maxm < Out[0][i]:
            maxm = Out[0][i]
            k = i
    if k == 0:
        print("Image is of letter A.")
    elif k == 1:
        print("Image is of letter B.")
    else:
        print("Image is of letter C.")
    plt.imshow(x.reshape(5, 6))
    plt.show()


def main_nn():
    # Step1: Creating a dataset
    a = [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1]
    b = [0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0]
    c = [0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0]
    y = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    # Step 2: Dataset visualization
    plt.imshow(np.array(a).reshape(5, 6))

    x = [np.array(a).reshape(1, 30), np.array(b).reshape(1, 30),
         np.array(c).reshape(1, 30)]
    y = np.array(y)
    print(x, "\n\n", y)

    # Step 6
    w1 = generate_wt(30, 5)
    w2 = generate_wt(5, 3)
    print(w1, "\n\n", w2)
    acc, losses, w1, w2 = train(x, y, w1, w2, 0.1, 200)

    plt.figure()
    plt.plot(acc)
    plt.ylabel('Accuracy')
    plt.xlabel("Epochs:")

    plt.figure()
    plt.plot(losses)
    plt.ylabel('Loss')
    plt.xlabel("Epochs:")

    # print(w1, "\n", w2)

    plt.figure()

    # Step 8 inference
    print(r"inference letter ")
    predict(x[0], w1, w2)
    plt.show()


if __name__ == '__main__':
    main_nn()
