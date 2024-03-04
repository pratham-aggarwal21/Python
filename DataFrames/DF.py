import pandas as pd
import numpy as np

s1 = {'Marks': {'ABC':90, 'DEF':60, 'GHI':40, 'JKL':20}}

d1 = pd.DataFrame(s1)
#d1.indexname = 'Name'

l1 = []
for a,j in d1.iterrows():
##    print(j)  'Stores the complete data of the row except index
##    print(a)  'Stores index (in this case: 'ABC', 'DEF'....)
    for i in j:
        if i>=90:
            l1.append('Grade A+')
        elif i>70 and i<=90:
            l1.append('Grade A')
        elif 60<i<=70:  
            l1.append('Grade B')
        elif 50<i<=60:
            l1.append('Grade C')
        elif 40<i<=50:
            l1.append('Grade D')
        else:
            l1.append('Grade F')

d1['Grades'] = l1
        
print(d1)
