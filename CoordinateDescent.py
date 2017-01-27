'''
    Dimitri Ambrazis
    Jones Devlin

    The Coordinate Descent class takes in an excel file, parses it, and performs coordinate descent
    on the data per prior-determined specifications.  The goal is to see what betas are produced.

    Data Key:
         observations[0] = lcavol
         observations[1] = lweight
         observations[2] = age
         observations[3] = lbph
         observations[4] = svi
         observations[5] = lcp
         observations[6] = gleason
         observations[7] = pgg45
         observations[8] = lpsa

'''

import pandas as pd
import numpy as np
from sklearn import linear_model


class CoordinateDescent(object):

    def __init__(self, xmatrix, yvalues, lamb, step):
        self.xmatrix = xmatrix
        self.yvalues = yvalues
        self.lamb = lamb
        self.step = step

    def coordDescent(self):
        n = self.yvalues.size
        p = self.xmatrix.shape[1]
        betas = np.zeros(shape=(p, 1))
        betasOld = np.zeros(shape=(p, 1))
        maxStep = self.step

        while maxStep >= self.step:
            for j in range(p):
                betasOld = betas
                if j == 0:
                    betasOld[0] = betas[0]
                    betas[0] = self.bnot(self.xmatrix, self.yvalues, betas, n, p)
                else:
                    betasOld[j] = betas[j]
                    betas[j] = self.bother(self.xmatrix, self.yvalues, betas, n, p, j, lamb)
            maxStep = self.maxDif(betas, betasOld, p)
        return betas

    #Calculates the beta for j = 0
    def bnot(self, xmatrix, yvalues, betas, n, p):
        outersum = 0
        for i in range(n):
            innersum = 0
            for k in range(p):
                innersum += self.xmatrix[i, k] * betas[k, 0]
            outersum += yvalues[i] - innersum
        return outersum / n

    #Calculates the beta for j = 1,2,...p
    def bother(self, xmatrix, yvalues, betas, n, p, j, lamb):
        #The next for lines need to be moved out of the loop to improve speed
        denom = 0
        for i in range(n):
            denom += (xmatrix[i, j])**2
        t = lamb / (2 * denom)
        outersum = 0
        for i in range(n):
            innersum = 0
            for k in range(p):
                if k != j:
                    innersum += xmatrix[i, k] * betas[k, 0]
            outersum += xmatrix[i, j] * (yvalues[i] - innersum)
        x = outersum / denom
        s = self.shrinkage(x, t)

        return s

    #The shrinkage function
    def shrinkage(self, x, t):
        if x < -t:
            s = x + t
        elif x > t:
            s = x - t
        else:
            s = 0
        return s

    #Finds the maximum absolute difference between two vectors
    def maxDif(self, betas, betasOld, p):
        betadelta = np.zeros(shape=(p, 1))
        for i in range(p):
            betadelta[i] = abs(betas[i] - betasOld[i])
        return np.amax(betadelta)



def main(self):

    prostate = pd.read_csv("./prostate.csv")
    X_df = prostate[["lcavol", "lweight", "age", "lbph", "svi", "lcp", "gleason", "pgg45"]]
    Y_df = prostate["lpsa"]

    x_matrix = np.array(X_df)
    y_vector = np.array(Y_df)

    observations = CoordinateDescent(x_matrix, y_vector, 1, 0.000001)
    


    print("Lasso coefficients using our implementation")
    #print(observations.coordDescent.transpose())
    print(observations.coordDescent())
    _lambda = 1.0

    clf = linear_model.Lasso(alpha=_lambda, fit_intercept=True, max_iter=50000, tol=0.000001)
    clf.fit(X_df, Y_df)
    print("Lasso coefficients using sklearn.linear_model.Lasso")
    print(np.append(clf.intercept_, clf.coef_))







if __name__ == '__main__':
    main(object)
