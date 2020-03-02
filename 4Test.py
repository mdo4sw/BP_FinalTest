# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:23:06 2020

@author: mdo
"""

from main import main_supervisor


m = main_supervisor()
data_path = "R://crd_G2000//_Coordinators//NomardR//DEV//scripts//dataAnalysis//v1//data/"
file_name = "Combined_20200212_102932.csv"
setupFilepath = "R://crd_G2000//_Coordinators//NomardR//DEV//scripts//dataAnalysis//v1/config/"
setupFileName = "setupInfo.ini"
testName = "1D_CH4_1"

m.set_data_path(data_path,file_name)
m.set_setupFilePath(setupFilepath)
m.set_setupFileName(setupFileName)
m.set_testName(testName)
m.set_setupInfo()
m.set_data()
m.multiregression_cal()



