try:
    import pandas as pd
    import numpy as np
    import sys 
    import matplotlib as plt
    n=len(sys.argv)
    if n<3:
        raise ValueError("Kindly provide the input in the correct format which is {python <program.py> <InputDataFile>} {weights} {impacts}")
     
    data=pd.read_csv(sys.argv[1])
    if data.shape[1]<3:
        raise ValueError("The input file must have 3 or more coloumns")
    
    weights=[]

    weights=sys.argv[2].split(",")
    impacts=[]
    impacts=sys.argv[3].split(",")
    #print(weights)
    #print(impacts)
    print(data.shape[1])
    print(len(weights))
    if data.shape[1]!=len(weights)+1 or data.shape[1]!=len(impacts)+1 or len(impacts)!=len(weights):
        raise ValueError("Number of weights, number of impacts and number of columns (from 2nd to last columns) must be same")
    for i in range(len(impacts)):
        if(impacts[i]!='+' and impacts[i]!='-'):
            #print(i)
            raise ValueError("Impacts should be either positive or negative")
     
except ValueError as ve:
    print(ve)
else:
    for i in range(data.shape[1]-1):
        data.iloc[:,i+1]=(data.iloc[:,i+1])/sum(data.iloc[:,i+1]**2)
    weights=[0.25,0.25,0.25,0.25,0.25]
    for i in range(len(weights)):
        data.iloc[:,i+1]=(data.iloc[:,i+1])*weights[i]


    data2=data
    ideal_best=[]
    ideal_worst=[]
    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(max(data.iloc[:,i+1]))
            ideal_worst.append(min(data.iloc[:,i+1]))
        elif impacts[i] == '-':
            ideal_best.append(min(data.iloc[:,i+1]))
            ideal_worst.append(max(data.iloc[:,i+1]))

    ideal_best1=[]
    ideal_worst1=[]
    index=data.index
    for j in range(len(index)):
        sum1=0
        sum2=0
        for i in range(len(ideal_best)):
            sum1+=(ideal_best[i]-data.iloc[j][i+1])**2
            sum2+=(ideal_worst[i]-data.iloc[j][i+1])**2
            
        ideal_best1.append(sum1**0.5)
        ideal_worst1.append(sum2**0.5)

    topsis_score=[]
    for i in range(len(ideal_best1)):
        topsis_score.append(ideal_worst1[i]/(ideal_best1[i]+ideal_worst1[i]))

    data["Topsis Score"]=topsis_score
    data['Rank'] = data['Topsis Score'].rank()
    data.to_csv("101903072-result",index=False)






