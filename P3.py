#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 01:30:37 2018

@author: gjwills
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
#                           MAIN() FUNCTION
# =============================================================================

def main():
    filename = "output.txt"
    
    myFile = "batting.csv"
    df = pd.read_csv(myFile, sep=",")

    
    print("The data in the first column:\n",df.iloc[:,0] )

    print("\nThe data in the third row:\n", df.iloc[2,:])
    print("\nThe value in the first row and 4th column:", df.iloc[0,3])
    print("\nThe data in rows 1 (the second row), 2 (third row), and 5", sep=" ")
    print("(sixth row) and columns 0 (first column) and 3 (fourth column))", df.iloc[[1,2,5],[0,3]])

    print("\nThe mean OBP for all teams is: ", np.round(np.mean(df.iloc[:,13]),3))
    print("The median OBP for all teams is: ", np.round(np.median(df.iloc[:,13]),3))
    print("The max OBP for all teams is: ", np.round(np.max(df.iloc[:,13]),3))
    print("The min OBP for all teams is: ", np.round(np.min(df.iloc[:,13]),3))
    print("The variance of OBP for all team is: ", np.round(np.var(df.iloc[:,13]),3))
    
    print("The mean RBI for all teams is: ", np.round(np.mean(df.loc[:,'RBI']),3))
    print("The median RBI for all teams is: ", np.round(np.median(df.loc[:,'RBI']),3))
    print("The max RBI for all teams is: ", np.round(np.max(df.loc[:,'RBI']),3))
    print("The min RBI for all teams is: ", np.round(np.min(df.loc[:,'RBI']),3))
    print("The variance of RBI for all teams is: ", np.round(np.var(df.loc[:,'RBI']),3))
    
    print("The mean OPS for all teams is: ", np.round(np.mean(df.loc[:,'OPS']),3))
    print("The median OPS for all teams is: ", np.round(np.median(df.loc[:,'OPS']),3))
    print("The max OPS for all teams is: ", np.round(np.max(df.loc[:,'OPS']),3))
    print("The min OPS for all teams is: ", np.round(np.min(df.loc[:,'OPS']),3))
    print("The variance of OPS for all teams is: ", np.round(np.var(df.loc[:,'OPS']),3))

    with open(filename, "w") as file:
        file.write("This is output.txt file...\n\n")
        # write OBP statistics to output.txt using with open
        # I rounded to 3 decimal place because these statistics are presented
        # as decimal numbers rounded to 3 decimal places. In the batting.csv file,
        # you can see that the statistics are presented as such. (Note that RBI is
        # a regular integer number, so is rounded to 2 decimal places)
        file.write("The mean OBP for all teams is: ")
        val = np.round(np.mean(df.iloc[:,13]),3)
        val = str(val)
        file.write(val)
        file.write("\nThe median OBP for all teams is: ")
        val = np.round(np.median(df.iloc[:,13]),3)
        val = str(val)
        file.write(val)
        file.write("\nThe max OBP for all teams is: ")
        val = np.round(np.max(df.iloc[:,13]),3)
        val = str(val)
        file.write(val)
        file.write("\nThe min OBP for all teams is: ")
        val = np.round(np.min(df.iloc[:,13]),3)
        val = str(val)
        file.write(val)
        file.write("\nThe variance of the OBP for all teams is: ")
        val = np.round(np.var(df.iloc[:,13]),3)
        val = str(val)
        file.write(val)
        
        #write RBI statistics to output.txt using with open
        file.write("\n\nThe mean RBI for all teams is: ")
        val = np.round(np.mean(df.loc[:,'RBI']),2)
        val = str(val)
        file.write(val)
        file.write("\nThe median RBI for all teams is: ")
        val = np.round(np.median(df.loc[:,'RBI']),2)
        val = str(val)
        file.write(val)
        file.write("\nThe max RBI for all teams is: ")
        val = np.round(np.max(df.loc[:,'RBI']),2)
        val = str(val)
        file.write(val)
        file.write("\nThe min RBI for all teams is: ")
        val = np.round(np.min(df.loc[:,'RBI']),2)
        val = str(val)
        file.write(val)
        file.write("\nThe variance of the RBI for all teams is: ")
        val = np.round(np.var(df.loc[:,'RBI']),2)
        val = str(val)
        file.write(val)
        
        # write OPS statistics to output.txt using with open
        file.write("\n\nThe mean OPS for all teams is: ")
        val = np.round(np.mean(df.loc[:,'OPS']),3)
        val = str(val)
        file.write(val)
        file.write("\nThe median OPS for all teams is: ")
        val = np.round(np.median(df.loc[:,'OPS']),3)
        val = str(val)
        file.write(val)
        file.write("\nThe max OPS for all teams is: ")
        val = np.round(np.max(df.loc[:,'OPS']),3)
        val = str(val)
        file.write(val)
        file.write("\nThe min OPS for all teams is: ")
        val = np.round(np.min(df.loc[:,'OPS']),3)
        val = str(val)
        file.write(val)
        file.write("\nThe variance of the OPS for all teams is: ")
        val = np.round(np.var(df.loc[:,'OPS']),3)
        val = str(val)
        file.write(val)
        file.write("\n\n")
    
    # call summary function to print out summary of all statistics
    summary(df)
    # call to appendDF returns a list of lengths and total characters in file
    lengthList, totalChars = appendDF(filename, df)
    # for/in loop will print out the number of characters in each line of the file
    i = 1
    for length in lengthList:
        print("Line " + str(i) + " has length of " + str(length))
        i+=1
    print("The total number of characters in the output file, called output.txt, is " + str(totalChars))
    # call to make graphs will make 4 graphs with different statistics
    makeGraphs(filename, df)
    # call to userGraph will ask user to enter a statistics, will print stats,
    # and print out box plot for the specified column
    userGraph(filename, df)

# =============================================================================
#                           SUMMARY FUNCTION    
# =============================================================================
def summary(df):
    print(df.describe().transpose())
    
# =============================================================================
#                           APPENDDF FUNCTION
# =============================================================================
    
def appendDF(filename, df):
    totalChars = 0
    with open(filename, "a") as file:
        df.to_csv(filename, sep=',', mode='a')
    
    with open(filename, "r") as file:
        lines = file.readlines()
        lengthList = []
        for line in lines:
            lengthList.append(len(line))
            totalChars += len(line)
    return lengthList, totalChars

# =============================================================================
#                           MAKEGRAPHS FUNCTION
# =============================================================================

def makeGraphs(filename,df):
    imagefilename="Project3GRAPH1.jpg"
    fig=plt.figure()
    plt.scatter(df["OBP"], df["OPS"])
    title ="Scatterplot for OBP and OPS"
    fig.suptitle(title, fontsize=20)
    plt.xlabel("On-base Percentage", fontsize=18)
    plt.ylabel("On-base plus slugging", fontsize=16)
    plt.savefig(imagefilename)
    plt.show()
    
    imagefilename="Project3GRAPH2.jpg"
    fig=plt.figure()
    plt.boxplot(df["RBI"],0)
    title ="Boxplot for League RBI"
    fig.suptitle(title, fontsize=20)
    plt.ylabel("Runs Batted In", fontsize=16)
    plt.savefig(imagefilename)
    plt.show()
    
    imagefilename="Project3GRAPH3.jpg"
    fig=plt.figure()
    plt.plot(df["Team"],df["Hits"])
    title ="Hits by team"
    fig.suptitle(title, fontsize=20)
    plt.xticks(fontsize=8, rotation=90)
    plt.xlabel("Team", fontsize=18)
    plt.ylabel("Number of Hits", fontsize=16)
    plt.savefig(imagefilename)
    plt.show()
    
    imagefilename="Project3GRAPH4.jpg"
    fig=plt.figure()
    plt.bar(df["Team"],df["SO"])
    title ="SO by team"
    fig.suptitle(title, fontsize=20)
    plt.xticks(fontsize=8, rotation=90)
    plt.xlabel("Team", fontsize=18)
    plt.ylabel("Number of SOs", fontsize=16)
    plt.savefig(imagefilename)
    plt.show()
    
# =============================================================================
#                           USERGRAPH FUNCTION    
# =============================================================================

def userGraph(filename, df):
    print("The variable names in the dataframe are: ", df.columns.values)
    result = input("Choose one of the variables. It must be numeric. : ")
    print("The mean for", result, "is", np.round(np.mean(df[result]),2))
    print("The max for", result, "is", np.round(np.max(df[result]),2))
    print("The std dev for", result, "is", np.round(np.std(df[result]),2))
    
    with open(filename, "a") as file:
        file.write("The mean for ")
        result = str(result)
        file.write(result)
        file.write(" is ")
        mean = np.round(np.mean(df[result]),2)
        file.write(str(mean))
        
        file.write("\nThe max for ")
        result = str(result)
        file.write(result)
        file.write(" is ")
        maxm = np.round(np.max(df[result]),2)
        file.write(str(maxm))
        
        file.write("\nThe std dev for ")
        result = str(result)
        file.write(result)
        file.write(" is ")
        dev = np.round(np.std(df[result]),2)
        file.write(str(dev))
        
    imagefilename="UserGraph.jpg"
    fig=plt.figure()
    plt.boxplot(df[result])
    title ="Box Plot for " + result
    fig.suptitle(title, fontsize=20)
    plt.ylabel(result, fontsize=18)
    plt.savefig(imagefilename)
    plt.show()

# call main  
main()