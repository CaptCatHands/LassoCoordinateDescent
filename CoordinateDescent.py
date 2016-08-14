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
import scipy as sp

from xlrd import open_workbook

class CoordinateDescent(object):

    def readData(self, dataFile):
        '''
            Reads in an MS Excel files and parses the data into a list (array)
        '''
        wb = open_workbook(dataFile)
        observations=[[0 for x in range(57)] for y in range(200)]
        for sheet in wb.sheets():
            number_of_rows = sheet.nrows
            number_of_columns = sheet.ncols
            items = []
            rows = []
            for row in range(0, number_of_rows):
                for col in range(number_of_columns):
                    value = (sheet.cell(row, col).value)
                    value = str(value)
                    if value=="":
                        value="null"
                    observations[row][col]=value
        return observations

    def homeOwnershipAnnualSalaryX(self, observations):
        '''
            Get x matrix.  This is composed of the home ownership and salary
        '''
        x = [[0 for x in range(3)] for y in range(199)]
        for i in range(0,200):
            if i>0:
                x[i-1][0] = 1
                if observations[i][12] =="RENT":
                    x[i-1][1] = 0
                elif observations[i][12] =="MORTGAGE":
                    x[i-1][1] = 1
                else:
                    x[i - 1][1] = 2
                x[i-1][2] = observations[i][13]
        #for i in range(0, 199):
            #print str(x[i][0]) + "\t" + str(x[i][1]) + "\t" + str(x[i][2])
        return x

    def findOLSBeta(self, x, y):
        '''
            (xT dot x)-1(xT dot y)
        '''
        x = np.array(x, dtype=float)
        y = np.array(y, dtype=float)
        xTranspose = np.transpose(x)
        firstPart= np.linalg.inv(np.dot(xTranspose, x))
        secondPart = np.dot(xTranspose, y)

        return np.dot(firstPart, secondPart)


    def leastSquares(self, xmatrix, ymatrix):
        '''
        Reads in attributes and results to calculate coefficients using least squares
        :param xmatrix: matrix of attribute values
        :param ymatrix: matrix of results
        :return: a matrix of coefficients beta
        '''
        #Initializing coefficient matrix of zeroes. Need to figure out dimensions from inputs.
        bmatrix = np.zeros()
        #only does 3 passes through the coordinate descent algorithm. Need to make it smarter
        for i in range(0, 3):
            #Algorithm requires matrix with current i removed
            xtemp = sp.delete(xmatrix, i, 1)
            btemp = sp.delete(bmatrix, i, 0)
            #The following line is a mess. Need to fix with numpy matrix methods
            numA = xmatrix.transpose()
            numB = np.matmul(xtemp, btemp)
            numC = np.subtract(ymatrix, numB)
            numerator = np.matmul(numA, numB)
            denominator = np.matmul(xmatrix, numA)
            bmatrix[i,0] = np.divide(numerator, denominator)

def main(self):
    yValues=[0 for x in range(199)]
    cd = CoordinateDescent()
    observations=cd.readData('Loan.xlsx')

    # Case 1: Does home ownership and salary affect the loan grade?
    xValues=cd.homeOwnershipAnnualSalaryX(observations)

    for i in range(0,200):
        if i>0:
            yValues[i-1]=float(observations[i][6])
    betas = cd.findOLSBeta(xValues, yValues)
    for i in range(len(betas)):
        print(betas[i])


if __name__ == '__main__':
    main(object)
