import sklearn.datasets as skl
import numpy as np
from math import pi, sqrt, exp
from sklearn.model_selection import train_test_split


class Classifier:
    def __init__(self):
        self.mean = []
        self.variance = []

    def prepareStats(self, data, target):
        self.mean = data.groupby(target).apply(np.mean).to_numpy()
        self.variance = data.groupby(target).apply(np.var).to_numpy()

    def probDensity(self, mean, var, x):
        density = 1/(sqrt(2*pi)*var) * exp((-(x-mean)**2)/(2*sqrt(var)))
        return density

    def priorProb(self, data, target):
        prior = data.groupby(target).apply(lambda x: len(x)/len(data))
        return prior.values

    def postProb(self, target, row):
        prob = []
        for i in range(len(target.unique())):
            post = 0
            for j in range(len(row)):
                post += self.probDensity(self.mean[i][j], self.variance[i][j], row[j])
            prob.append(post)
        return prob

    def fit(self, data, target):
        self.prepareStats(data, target)
        self.prior = self.priorProb(data, target)

    def predict(self, data, target):
        pred = []
        for i in range(len(data)):
            post = self.postProb(target, data.iloc[i, :-1])
            prob = self.prior + post
            idx = np.argmax(prob)
            pred.append(idx)
        return pred

    def verify(self, pred, target):
        correct = 0
        for i in range(len(pred)):
            if pred[i] == target[i]:
                correct += 1
        return correct/len(pred)


if __name__ == "__main__":
    data = skl.load_wine(as_frame=True).data
    target = skl.load_wine(as_frame=True).target
    train_data, test_data, train_target, test_target = train_test_split(data, target, test_size=0.5)
    cls = Classifier()
    cls.fit(train_data, train_target)
    pred = cls.predict(test_data, test_target)
    print(cls.verify(pred, target))
