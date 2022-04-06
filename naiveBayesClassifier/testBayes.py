from bayes import Classifier
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, KFold
import numpy as np


def testKFold():
    data = load_wine(as_frame=True).data
    target = load_wine(as_frame=True).target
    splitResults = []
    for splits in [3, 4, 5, 10]:
        kf = KFold(n_splits=splits, shuffle=True)
        results = []
        for trainIndex, testIndex in kf.split(data):
            trainData, testData = data.iloc[trainIndex], data.iloc[testIndex]
            trainTarget, testTarget = target.iloc[trainIndex], target.iloc[testIndex]
            cls = Classifier()
            cls.fit(trainData, trainTarget)
            pred = cls.predict(testData, testTarget)
            results.append(cls.verify(pred, target))
        splitResults.append(np.mean(results))
    return splitResults


def testStandard():
    data = load_wine(as_frame=True).data
    target = load_wine(as_frame=True).target
    results = []
    for ts in [0.2, 0.5, 0.8]:
        trainData, testData, trainTarget, testTarget = train_test_split(data, target, test_size=ts)
        cls = Classifier()
        cls.fit(trainData, trainTarget)
        pred = cls.predict(testData, testTarget)
        results.append(cls.verify(pred, target))
    return results


if __name__ == "__main__":
    print(testStandard())
    print(testKFold())
