# TOPSIS
TOPSIS is a method of compensatory aggregation that compares a set of alternatives by identifying weights for each criterion, normalising scores for each criterion and calculating the geometric distance between each alternative and the ideal alternative, which is the best score in each criterion.
In this projected I have developed a command line python program to implement the Topsis and have uploaded it at https://pypi.org/project/TOPSIS-KARAN-101903072/

Result file contains all the columns of input file and two additional columns having Topsis Score and Rank.
 The program checks for:
• Correct number of parameters (inputFileName, Weights, Impacts, resultFileName).
• Show the appropriate message for wrong inputs.
• Handling of “File not Found” exception
• Input file must contain three or more columns.
• From 2nd to last columns must contain numeric values only (Handling of non-numeric values)
• Number of weights, number of impacts and number of columns (from 2nd to last columns) must be 
same.
• Impacts must be either +ve or -ve.
• Impacts and weights must be separated by ‘,’ (comma).


This package can be downloaded
pip install TOPSIS-KARAN-101903072

