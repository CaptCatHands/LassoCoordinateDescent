'''
    Dimitri Ambrazis
    Jones Devlin

    Final Project August 2016

    The Coordinate Descent class takes in an excel file, parses it, and performs coordinate descent on the data
    per prior-determined specifications.  The goal is to see what betas are produced.
    We will then use Orange to check the betas

    Data Key:
         observation[0] = id
         observation[1] = member_id
         observation[2] = loan_amnt
         observation[3] = funded_amnt
         observation[4] = funded_amnt_inv
         observation[5] = term
         observation[6] = int_rate
         observation[7] = installment
         observation[8] = grade
         observation[9] = sub_grade
         observation[10] = emp_title
         observation[11] = emp_length
         observation[12] = home_ownership
         observation[13] = annual_inc
         observation[14] = verification_status
         observation[15] = issue_d
         observation[16] = loan_status
         observation[17] = pymnt_plan
         observation[18] = url
         observation[19] = desc
         observation[20] = purpose
         observation[21] = title
         observation[22] = zip_code
         observation[23] = addr_state
         observation[24] = dti
         observation[25] = delinq_2yrs
         observation[26] = earliest_cr_line
         observation[27] = inq_last_6mths
         observation[28] = mths_since_last_delinq
         observation[29] = mths_since_last_record
         observation[30] = open_acc
         observation[31] = pub_rec
         observation[32] = revol_bal
         observation[33] = revol_util
         observation[34] = total_acc
         observation[35] = initial_list_status
         observation[36] = out_prncp
         observation[37] = out_prncp_inv
         observation[38] = total_pymnt
         observation[39] = total_pymnt_inv
         observation[40] = total_rec_prncp
         observation[41] = total_rec_int
         observation[42] = total_rec_late_fee
         observation[43] = recoveries
         observation[44] = collection_recovery_fee
         observation[45] = last_pymnt_d
         observation[46] = last_pymnt_amnt
         observation[47] = next_pymnt_d
         observation[48] = last_credit_pull_d
         observation[49] = collections_12_mths_ex_med
         observation[50] = mths_since_last_major_derog
         observation[51] = policy_code
         observation[52] = application_type
         observation[53] = annual_inc_joint
         observation[54] = dti_joint
         observation[55] = verification_status_joint
         observation[56] = acc_now_delinq


'''

import numpy as np

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
            for row in range(0, number_of_rows-1):
                for col in range(number_of_columns):
                    value = (sheet.cell(row, col).value)
                    value = str(value)
                    if value=="":
                        value="null"
                    observations[row][col]=value
        return observations

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
            xtemp = scipy.delete(xmatrix, i, 1)
            btemp = scipy.delete(bmatrix, i, 0)
            #The following line is a mess. Need to fix with numpy matrix methods
            numA = xmatrix.transpose()
            numB = np.matmul(xtemp, btemp)
            numC = np.subtract(ymatrix, numB)
            numerator = np.matmul(numA, numB)
            denominator = np.matmul(xmatrix, numA)
            bmatrix[i,0] = np.divide(numerator, denominator)

def main(self):
    cd = CoordinateDescent()
    observations=cd.readData('Loan.xlsx')
    print(observations[0])


if __name__ == '__main__':
     main(object)