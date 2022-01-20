import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import ShuffleSplit, train_test_split


def dict_extractor(filepath):
    fb = open(filepath, 'r')
    line = fb.readline()
    rv_dict = {}
    nfeas = 0
    while line:
        words = line.split()
        for w in words[1:]:
            if w not in rv_dict:
                rv_dict[w] = nfeas
                nfeas += 1
        line = fb.readline()
    fb.close()
    return rv_dict


def feature_extractor(filepath, fea_dict):
    nfeas = len(fea_dict)
    data = np.empty([0, nfeas])
    target = np.empty([0, 1])
    fb = open(filepath, 'r')
    line = fb.readline()

    while line:
        tmp = np.zeros([1, nfeas])
        words = line.split()
        target = np.append(target, int(words[0]))
        for w in words[1:]:
            tmp[0, fea_dict[w]] += 1
        data = np.append(data, tmp, axis=0)
        line = fb.readline()

    fb.close()
    target = np.array(target).reshape(len(target), 1)

    return data, target


# def LinearSVM_SGD(X, Y, iteration):
    # [n, ndim] = X.shape
    # mu = np.mean(X, 0)
    # X = X - mu
    # sigma = np.std(X, 0)
    # sigma[sigma == 0] = 1e-6
    # X = X / sigma

    # w = np.zeros(ndim)
    # eta = 0.5
    # for epoch in range(1, iteration):
        # loss = 0.0
        # for i, x in enumerate(X):
            # l = Y[i] * np.dot(X[i], w)
            # if l < 1:
                # w = w + eta * ((X[i] * Y[i]) + (-2 * (1 / epoch) * w))
                # loss += 1 - l[0]
            # else:
                # w = w + eta * (-2 * (1 / epoch) * w)

        # yp = np.dot(X, w.transpose())
        # yp[yp > 0] = 1
        # yp[yp < 0] = -1
        # # print(epoch, 'loss:', loss, ' acc:', sum(yp == Y.reshape(n)) / n, ' weight:', w)
        # if epoch % 5 == 0:
            # print(epoch, 'loss:', loss, ' acc:', sum(yp == Y.reshape(n)) / n, ' weight:', w)

    # return np.sum(loss), w, mu, sigma


def test_hingloss(Xtest, Ytest, mu, sigma, w):
    x = (Xtest - mu) / sigma
    yp = np.dot(Xtest, w)
    yp[yp > 0] = 1
    yp[yp < 0] = -1
    acc = sum(yp == Ytest) / len(Ytest)
    print('test acc:', acc)
    print(yp, Ytest)
    return acc


def main_sent():
    dict_train = dict_extractor(r"./review_train.txt")
    xtrain, ytrain = feature_extractor(r"./review_train.txt", dict_train)
    print(xtrain)
    print(ytrain)
    print(dict_train)

    loss, w, mu, sigma = LinearSVM_SGD(xtrain, ytrain, 10)
    xtest, ytest = feature_extractor(r"./review_test.txt", dict_train)
    acc = test_hingloss(xtest, ytest.reshape(len(ytest)), mu, sigma, w)


def main_iris():
    iris = load_iris()
    data = iris.data
    target = iris.target[:100]
    target[target == 0] = -1
    data = iris.data[:100, :]

    # rs = ShuffleSplit(n_splits=1, test_size=.20, random_state=42, )
    # for train_index, test_index in rs.split(data):
    #     Xtrain, Xtest = data[train_index], data[test_index]
    #     Ytrain, Ytest = target[train_index], target[test_index]

    Xtrain, Xtest, Ytrain, Ytest = train_test_split(data, target, test_size=.20, random_state=42, )

    loss, w, mu, sigma = LinearSVM_SGD(Xtrain, Ytrain.reshape(len(Ytrain), 1), 500)
    acc = test_hingloss(Xtest, Ytest.reshape(len(Ytest)), mu, sigma, w)


if __name__ == '__main__':
    # main_iris()
    main_sent()
