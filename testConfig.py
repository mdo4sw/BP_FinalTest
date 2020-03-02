# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 15:18:20 2020

@author: mdo
"""

class testConfigInfo():
    def __init__(self):

        self.source_file_path = ""
        self.col_names = []
        
        self.data_all = []
        self.raw_data_all = []
        self.coefficient_multiRegression = []
        
        self.totalDataNumber = []
        # the mainVars and calculatingVars will be dictonary . 
        
        # mainVars will have an array containing two items for each of its key
        # the first item is the index column of the data in the raw data
        # the second item is an array containing data for the its key 
        
        # calculatingVars will have one item for each key.
        # the item is an array containing data for the key 
        
        self.mainVars = {} 
        self.calculatingVars = {}
        
        self.dependentVar_List = []
        self.independentVar_List = []
        
        self.invertingVar = 1      
      
        
        #self.UTIL = utilities()
        
        
        #self.set_source_file_path()
    
    def set_mainVars(self,varName):
        self.mainVars.update({varName:[]})

    def get_mainVars(self):
        return self.mainVars

    def set_calculatingVarList(self,varName):
        self.calculatingVars.update({varName:[]})
        
    def get_calculatingVarList(self):
        return self.calculatingVars
    
    def set_dependentVarList(self,varName):
        self.dependentVar_List.append(varName)
    
    def get_dependentVarList(self):
        return self.dependentVar_List
    
    def set_independentVarList(self,varName):
        self.independentVar_List.append(varName)
        
    def get_independentVarList(self):
        return self.independentVar_List
    
    def set_invertingTerm(self,var):
        self.invertingVar = float(var)
    def get_invertingTerm(self):
        return self.invertingVar