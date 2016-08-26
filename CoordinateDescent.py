'''
    Dimitri Ambrazis
    Jones Devlin
    Final Project August 2016

    The Coordinate Descent class takes in an excel file, parses it, and performs coordinate descent on the data
    per prior-determined specifications.  The goal is to see what betas are produced.
    We will then use Orange to check the betas.

    Data Key:
         observations[0] = id
         observations[1] = member_id
         observations[2] = loan_amnt
         observations[3] = funded_amnt
         observations[4] = funded_amnt_inv
         observations[5] = term
         observations[6] = int_rate
         observations[7] = installment
         observations[8] = grade
         observations[9] = sub_grade
         observations[10] = emp_title
         observations[11] = emp_length
         observations[12] = home_ownership
         observations[13] = annual_inc
         observations[14] = verification_status
         observations[15] = issue_d
         observations[16] = loan_status
         observations[17] = pymnt_plan
         observations[18] = url
         observations[19] = desc
         observations[20] = purpose
         observations[21] = title
         observations[22] = zip_code
         observations[23] = addr_state
         observations[24] = dti
         observations[25] = delinq_2yrs
         observations[26] = earliest_cr_line
         observations[27] = inq_last_6mths
         observations[28] = mths_since_last_delinq
         observations[29] = mths_since_last_record
         observations[30] = open_acc
         observations[31] = pub_rec
         observations[32] = revol_bal
         observations[33] = revol_util
         observations[34] = total_acc
         observations[35] = initial_list_status
         observations[36] = out_prncp
         observations[37] = out_prncp_inv
         observations[38] = total_pymnt
         observations[39] = total_pymnt_inv
         observations[40] = total_rec_prncp
         observations[41] = total_rec_int
         observations[42] = total_rec_late_fee
         observations[43] = recoveries
         observations[44] = collection_recovery_fee
         observations[45] = last_pymnt_d
         observations[46] = last_pymnt_amnt
         observations[47] = next_pymnt_d
         observations[48] = last_credit_pull_d
         observations[49] = collections_12_mths_ex_med
         observations[50] = mths_since_last_major_derog
         observations[51] = policy_code
         observations[52] = application_type
         observations[53] = annual_inc_joint
         observations[54] = dti_joint
         observations[55] = verification_status_joint
         observations[56] = acc_now_delinq
'''

import numpy as np
import pandas as pd


class CoordinateDescent(object):

    def coordDescent(self, xmatrix, yvalues, lamb, step):
        n = yvalues.size
        p = len(xmatrix)
        betas = np.zeros(n, 1)
        betasOld = np.zeros(n, 1)
        maxStep = step
        while maxStep >= step:
            for j in range(0, p):
                if j = 0:
                    betasOld.item(0,0) = betas.item(0, 0)
                    betas.item(0, 0) = bnot(xmatrix, yvalues, n, p)
                else
                    betasOld.item(j, 0) = betas.item(j, 0)
                    betas.item(j, 0) = bother(xmatrix, yvalues, n, p, j, lamb)
            maxStep = np.amax(abs(betas - betasOld))
        return betas

    def bnot(self, xmatrix, yvalues, n, p):
        outersum = 0
        for i in range(1, n):
            innersum = 0
            for k in range(1, p):
                innersum += xmatrix.item(i, k) * betas.item(k, 0)
            outtersum += yvalues(i, 0) - innersum
        return outersum / n

    def bother(self, xmatrix, yvalues, n, p, j, lamb):
        denom = 0
        for i in range(1, n):
            denom += (xmatrix(i, j))**2
        t = lamb / (2 * denom)
        outersum = 0
        for i in range(1, n):
            innersum = 0
            for k in range(1, p:)
                if k != j:
                    innersum += xmatrix(i, k) * betas.item(k, 0)
            outersum += xmatrix(i, j) * (yvalues(i, 0) )
        x = outersum / denom
        return x

    def coeff(self, lamb, )
      #move denom from bother to here

    def shrinkage(self, x, t):
        if x < -t:
            s = x + t
        else if x > t:
            s = x - t
        return s



def main(self):

    prostate = pd.read_csv("../prostate/prostate.csv")
    X_df = prostate[["lcavol", "lweight", "age", "lbph", "svi", "lcp", "gleason", "pgg45"]]
    Y_df = prostate["lpsa"]





if __name__ == '__main__':
    main(object)
