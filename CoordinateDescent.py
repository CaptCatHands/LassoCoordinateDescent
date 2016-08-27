'''
    Dimitri Ambrazis
    Jones Devlin
    Final Project August 2016

    The Coordinate Descent class takes in an excel file, parses it, and performs coordinate descent on the data
    per prior-determined specifications.  The goal is to see what betas are produced.

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


class CoordinateDescent(object):


    def coordDescent(self, xmatrix, yvalues, lamb, step):
        n = yvalues.size
        p = xmatrix.shape[1]
        global betas
        betas = np.zeros(shape=(n, 1))
        betasOld = np.zeros(shape=(n, 1))
        maxStep = step
        while maxStep >= step:
            for j in range(0, p):
                if j == 0:
                    betasOld[0,0] = betas.item(0, 0)
                    betas[0, 0] = self.bnot(xmatrix, yvalues, n, p)
                else:
                    betasOld[j, 0] = betas.item(j, 0)
                    betas[j, 0] = self.bother(xmatrix, yvalues, n, p, j, lamb)
            maxStep = np.amax(abs(betas - betasOld))
        return betas

    def bnot(self, xmatrix, yvalues, n, p):
        outersum = 0
        for i in range(0, n-1):
            innersum = 0
            for k in range(0, p-1):
                innersum += xmatrix[i, k] * betas[k, 0]
            outersum += yvalues[i] - innersum
        return outersum / n

    def bother(self, xmatrix, yvalues, n, p, j, lamb):
        denom = 0
        for i in range(1, n):
            denom += (xmatrix[i, j])**2
        t = lamb / (2 * denom)
        outersum = 0
        for i in range(1, n):
            innersum = 0
            for k in range(1, p):
                if k != j:
                    innersum += xmatrix[i, k] * betas[k, 0]
            outersum += xmatrix[i, j] * (yvalues[i] )
        x = outersum / denom
        s = self.shrinkage(x, t)

        return s


    def shrinkage(self, x, t):
        if x < -t:
            s = x + t
        elif x > t:
            s = x - t
        else:
            s = 0
        return s



def main(self):

    prostate = pd.read_csv("./prostate.csv")
    X_df = prostate[["lcavol", "lweight", "age", "lbph", "svi", "lcp", "gleason", "pgg45"]]
    Y_df = prostate["lpsa"]

    x_matrix = np.array(X_df)
    y_vector = np.array(Y_df)

    cd = CoordinateDescent()
    observations = cd.coordDescent(x_matrix, y_vector, 1, 1)

    print(observations)





if __name__ == '__main__':
    main(object)
