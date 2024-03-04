import pandas as pd
import numpy as np

##
##print(s1*100)
##print(s1>0)
##s2 = pd.Series(s1)
##s3 = pd.Series(s2)+3
##print(s3)
##     

##s1 = pd.Series([0.430271, 0.617328, -0.265421, -0.836113])
##s1.index=['Amzn', 'Apple', 'Microsoft', 'Google']
##print(s1)
##print(s1['Amzn'])
##s1['Amzn'] = 1.5
##print(s1['Amzn'])
##print(s1)

##Temp1 = pd.Series([100,90,80,70,100,200,250])
##Temp2 = pd.Series([101,92,83,75,140,100,200])
##Temp3 = pd.Series([102,91,85,70,107,102,240])
##Temp4 = pd.Series([120,95,80,75,110,200,170])
##print("Average temp of week 1: ",sum(Temp1)/len(Temp1))
##print("Average temp of week 2: ",Temp2.mean())
##print("Average temp of week 3: ",sum(Temp3)/len(Temp3))
##print("Average temp of week 4: ",sum(Temp4)/len(Temp4))
##Temp5 = Temp1+Temp2+Temp3+Temp4
##print("Average temp of month: ",Temp5.mean())


##s1 = pd.Series([{'Item1':10, 'Item2':20, 'Item3':30, 'Item4':40, 'Item5':50},
##               {'Item1':100, 'Item2':50, 'Item3':20, 'Item4':50, 'Item5':10},
##               {'Item1':90, 'Item2':60, 'Item3':40, 'Item4':30, 'Item5':20},
##               {'Item1':70, 'Item2':70, 'Item3':10, 'Item4':20, 'Item5':50},
##               {'Item1':10, 'Item2':100, 'Item3':70, 'Item4':10, 'Item5':10}])
##
##
##dict1 = {'Item1':0, 'Item2':0, 'Item3':0, 'Item4':0, 'Item5':0}
##for i in s1:
##    s = pd.Series(i)
##    dict1['Item1']+=s['Item1']
##    dict1['Item2']+=s['Item2']
##    dict1['Item3']+=s['Item3']
##    dict1['Item4']+=s['Item4']
##    dict1['Item5']+=s['Item5']
##print(dict1)
##
##dict1 = {'Item1':0, 'Item2':0, 'Item3':0, 'Item4':0, 'Item5':0}
##for i in s1:
##    s = pd.Series(i)
##    if dict1['Item1']<=s['Item1']:
##        dict1['Item1']=s['Item1']
##    if dict1['Item2']<=s['Item2']:
##        dict1['Item2']=s['Item2']
##    if dict1['Item3']<=s['Item3']:
##        dict1['Item3']=s['Item3']
##    if dict1['Item4']<=s['Item4']:
##        dict1['Item4']=s['Item4']
##    if dict1['Item5']<=s['Item5']:
##        dict1['Item5']=s['Item5']
##print(dict1)

term1 = pd.Series({1:100, 2:90, 3:80, 4:70, 5:85, 6:75, 7:100, 8:90, 9:65, 10:90})
term2 = pd.Series({1:90, 2:100, 3:85, 4:65, 5:55, 6:95, 7:80, 8:95, 9:100, 10:70})
term3 = pd.Series({1:95, 2:80, 3:85, 4:85, 5:75, 6:85, 7:90, 8:95, 9:100, 10:90})
FinalMarks = 0.25*term1 + 0.25*term2 + 0.50*term3
print(FinalMarks)
