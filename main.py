# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:13:47 2020

@author: mdo
"""

from data_supervisor import data_parsing
from utilities import utilities
class main_supervisor:
    def __init__(self):
        
        
        # declare objects including DUT, MFC and GOLDEN  
        self.dataSup = data_parsing()
        self.UTIL = utilities()
        
        self.data_path = ""
        self.dataFileName = ""
        self.testName = ""
        self.setupFilePath = ""
        self.setupFileName = ""
        
    def set_setupFilePath(self,setupFilePath):
        self.setupFilePath = setupFilePath
    def get_setupFilePath(self):
        return self.setupFilePath
    
    def set_setupFileName(self,setupFileName):
        self.setupFileName = setupFileName
    def get_setupFileName(self):
        return self.setupFileName
    
        
    def set_testName(self,testName):
        self.testName = testName
    
    def get_testName(self):
        return self.testName
    
    def set_data_path(self,path,fileName):
        try:
            if not self.dataSup.set_source_file_path(path,fileName):
                raise ValueError("Can't set path")
        except (ValueError):
            print("Can't set path")
    
    def get_dataPath(self):
        return self.dataSup.get_sourceFilePath()
    
    def set_setupInfo(self):
        setupInfoFile = self.get_setupFilePath() + "/" + self.get_setupFileName()
        
        setupInfo_Obj = self.UTIL.get_setupInfo(setupInfoFile)
        for i in setupInfo_Obj:
            if i == self.get_testName():
                testInfo = setupInfo_Obj[i]
                for j in testInfo["mainVars"]:
                    self.dataSup.set_mainVars(j)
                for h in testInfo["calculatingVars"]:
                    self.dataSup.set_calculatingVarList(h)
                for w in testInfo["dependentVars"]:
                    self.dataSup.set_dependentVarList(w)
                for k in testInfo["independentVars"]:
                    self.dataSup.set_independentVarList(k)
                for m in testInfo["invertingVar"]:
                    self.dataSup.set_invertingTerm(m)
                for c in testInfo["correctionTerms"]:
                    self.dataSup.set_correctionTerms(c)
                    
    def get_mainVars(self):
        return self.dataSup.get_mainVars()
    def get_calculatingVarList(self):
        return self.dataSup.get_calculatingVarList()
    
    def get_dependentVarList(self):
        return self.dataSup.get_dependentVarList()
    def get_independentVarList(self):
        return self.dataSup.get_independentVarList()
    
    def get_invertingTerm(self):
        return self.dataSup.get_invertingTerm()
    def get_correctionTerms(self):
        return self.dataSup.get_correctionTerms()
    

    def set_data(self):
        self.dataSup.set_data()
    def get_data(self):
        return self.dataSup.get_rawData()
    
    def multiregression_cal(self):
        self.dataSup.multiregression()
    
    def get_multiregression_coeff(self):
        return self.dataSup.get_coefficient()
    
        
        
        
        
        
        