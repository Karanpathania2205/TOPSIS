# TOPSIS
TOPSIS is a method of compensatory aggregation that compares a set of alternatives by identifying weights for each criterion, normalising scores for each criterion and calculating the geometric distance between each alternative and the ideal alternative, which is the best score in each criterion.<br />
In this project I have developed a command line python program to implement the Topsis and have uploaded it at https://pypi.org/project/TOPSIS-KARAN-101903072/  <br />

Result file contains all the columns of input file and two additional columns having Topsis Score and Rank.<br />
 The program checks for:<br />
• Correct number of parameters (inputFileName, Weights, Impacts, resultFileName).<br />
• Show the appropriate message for wrong inputs.<br />
• Handling of “File not Found” exception<br />
• Input file must contain three or more columns.<br />
• From 2nd to last columns must contain numeric values only (Handling of non-numeric values)<br />
• Number of weights, number of impacts and number of columns (from 2nd to last columns) must be same.<br />
• Impacts must be either +ve or -ve.<br />
• Impacts and weights must be separated by ‘,’ (comma).<br />


This package can be downloaded using the following command <br />
pip install TOPSIS-KARAN-101903072  <br />

Run the program through command line as: <br />
Usages: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName> <br />
Example: python karan.py topsis-data.csv “1,1,1,2” “+,+,-,+” topsis-result.csv<br />
