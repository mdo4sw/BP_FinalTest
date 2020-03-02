# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 15:35:51 2019

@author: mdo

Revise:
    20190820 : change at line 141 by MD
    #change from data[1:] to data[2:] to process data without the first two rows 
"""
import csv
import os
from utilities import utilities
from testConfig import testConfigInfo

class data_parsing():
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
        self.correctionTerms = {}
        
        
        self.UTIL = utilities()
        self.testConfigInfo = testConfigInfo()
        
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
    
    def set_correctionTerms(self,termName):
        
        self.correctionTerms.update({termName:0.0})
        
    def get_correctionTerms(self):
        return self.correctionTerms
        
    def set_source_file_path(self,raw_data_output_dir, name):
        temp_source_file_path = raw_data_output_dir + "/" + name
        if os.path.exists(temp_source_file_path):
            self.source_file_path = temp_source_file_path 
            return True
        else:
            return False
    def get_sourceFilePath(self):
        return self.source_file_path
    
    
       
    def get_rawData(self):    
        return self.data_all
    
    def set_data(self):
        file_header = []
        data = []

        #f = main_data_process.get_source_file_path()

        f = self.get_sourceFilePath()
        with open(f) as csvfile:
            reader = csv.DictReader(csvfile)
            #put data in regsiter    
            for row in reader:
                data.append(row)
            
            file_header = data[0].keys()
            
        
        #set data
        self.data_all = data[2:]
        
        #set col_names
        self.col_names = file_header
        
        #the folllowing loop is to set location of the main variable in the data
        for j in self.mainVars:
            print(j)
            index = 0
            for i in self.col_names:
                if i.strip() == j:    
                    #print(i)
                    self.mainVars[j].append(index)
                    #print(index)
                index = index + 1
        
          
        #the following loop is to set data for main variables 
        for j in self.mainVars:
            #the if condition is to add an empty array for the variable if it does not have one yet
            if len(self.mainVars[j]) ==1:
                self.mainVars[j].append([])
            
            for i in self.data_all:   # this for condition is to go through each line of the data
                for k in i:           # Because each line is a dictonary , the condition is to go through the keys of the dictionary  
                    if j == k.strip(): # the condition is to match the main variable to the key and get the data
                        self.mainVars[j][1].append(float(i[k]))
        
        
        
        #calculate quad term, quadLinear term and cross temr
        for i in self.calculatingVars:
            temp_varName = i.split("-")[0]
            calculation = i.split("-")[1]
            if  calculation == 'quad':
                temp_data = self.UTIL.square(self.mainVars[temp_varName][1])
                self.calculatingVars[i] = temp_data
            elif calculation == 'cube':
                temp_data = self.UTIL.cube(self.mainVars[temp_varName][1])
                self.calculatingVars[i] = temp_data
                
            elif calculation == 'cross':
                temp_data = self.UTIL.cross(self.mainVars[temp_varName][1])
                self.calculatingVars[i] = temp_data 
    
    def multiregression(self):
        x_vstack = []
        dependent_data = []
        independent_data =[]
        
        #temp_length = 0
        
        for i in self.totalDataNumber:
            temp = i
            if temp != i:
                return -999
                
        for i in self.dependentVar_List:
            dependent_data = self.mainVars[i][1]
            
        #for i in range(temp_length):
        #    x_vstack.append([])
            
        #for i in range(temp_length):
        for j in self.independentVar_List:
            if j in self.mainVars:
                independent_data.append(self.mainVars[j][1])
        
        for h in self.calculatingVars:
            independent_data.append(self.calculatingVars[h])
                
        x_vstack = self.UTIL.transpose(independent_data)    
            
        self.coefficient_multiRegression = self.UTIL.leastSquare(x_vstack,dependent_data)
        
        tempInvertingVar = self.get_invertingTerm()
        #the coefficient will be return as an array
        # the first element is the linear term
        # the second element is the quad term
        # the third element is the cub term
        for i in self.correctionTerms:
            if "linear" in i:
                self.correctionTerms[i] = self.coefficient_multiRegression[0]*tempInvertingVar
            elif "quadratic" in i:
                self.correctionTerms[i] = self.coefficient_multiRegression[1]*tempInvertingVar
            elif "cube" in i:
                self.correctionTerms[i] = self.coefficient_multiRegression[2]*tempInvertingVar
        return 1
        
    def get_coefficient(self):
        return self.coefficient_multiRegression
    
                    
        
        
        
        
        
    