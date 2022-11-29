import sys

import matplotlib
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
import networkx as nx
from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import palettable
migrate=[]
nonMigrate=[]

if __name__ == '__main__':

    selfLess0=0
    selfLess1000=0
    selfLess10000=0
    selfLess100000=0
    selfLess1000000=0

    wageLess0=0
    wageLess1000=0
    wageLess10000=0
    wageLess100000=0
    wageLess1000000=0

    noHigherThanK12Less0=0
    higherThanK12Less0=0
    noHigherThanK12Less1000=0
    higherThanK12Less1000=0
    noHigherThanK12Less10000=0
    higherThanK12Less10000=0
    noHigherThanK12Less100000=0
    higherThanK12Less100000=0
    noHigherThanK12Less1000000=0
    higherThanK12Less1000000=0

    # with open("migrate_2019.csv","r") as file:
    #     for lines in file:
    #         lines=lines.split(",")
    #         if(len(lines))>2:
    #             income=lines[7].strip()
    #             if(lines[7][0]=='"'):
    #                 income=lines[7][1:]
    #             if(lines[0]=="BPL"):
    #                 print("start")
    #             elif (int(lines[5])>0):
    #                 if income=='9999999':
    #                     print("This value is null")
    #                 elif int(income)<int(9999999):
    #                     income=int(income)
    #                     lines[7]=income
    #
    #                     educ=lines[3].strip()
    #                     classWork=lines[5].strip()
    #                     if(educ[0]=='"'):
    #                         educ=educ[1:]
    #                     educ=int(educ)
    #                     if(classWork[0]=='"'):
    #                         classWork=classWork[1:]
    #                     classWork=int(classWork)
    #
    #                     if income < 0:
    #                         if classWork==1:
    #                             selfLess0 += 1
    #                         else:
    #                             wageLess0+=1
    #                         if educ>1 and educ<7:
    #                             noHigherThanK12Less0+=1
    #                         else:
    #                             higherThanK12Less0+=1
    #                     elif income < 1000:
    #                         if classWork == 1:
    #                             selfLess1000 += 1
    #                         else:
    #                             wageLess1000 += 1
    #                         if educ > 1 and educ < 7:
    #                             noHigherThanK12Less1000 += 1
    #                         else:
    #                             higherThanK12Less1000 += 1
    #
    #                     elif income < 10000:
    #                         if classWork == 1:
    #                             selfLess10000 += 1
    #                         else:
    #                             wageLess10000 += 1
    #                         if educ > 1 and educ < 7:
    #                             noHigherThanK12Less10000 += 1
    #                         else:
    #                             higherThanK12Less10000 += 1
    #                     elif income < 100000:
    #                         if classWork == 1:
    #                             selfLess100000 += 1
    #                         else:
    #                             wageLess100000 += 1
    #                         if educ > 1 and educ < 7:
    #                             noHigherThanK12Less100000 += 1
    #                         else:
    #                             higherThanK12Less100000 += 1
    #
    #                     elif income < 1000000:
    #                         if classWork == 1:
    #                             selfLess1000000 += 1
    #                         else:
    #                             wageLess1000000 += 1
    #                         if educ > 1 and educ < 7:
    #                             noHigherThanK12Less1000000 += 1
    #                         else:
    #                             higherThanK12Less1000000 += 1
    #
    #
    # file.close()
    #
    #
    # columnName=['<0','<1000','<10000','<100000','<1000000']
    # rowName=['<=K12','>K12','self','wage']
    # values=[[noHigherThanK12Less0,higherThanK12Less0,selfLess0,wageLess0],[noHigherThanK12Less1000,higherThanK12Less1000,selfLess1000,wageLess1000],[noHigherThanK12Less10000,higherThanK12Less10000,selfLess10000,wageLess10000],[noHigherThanK12Less100000,higherThanK12Less100000,selfLess100000,wageLess100000],[noHigherThanK12Less1000000,higherThanK12Less1000000,selfLess1000000,wageLess1000000]]
    # d=pd.DataFrame(values,columnName,rowName)
    # plt.figure(figsize=(11,9),dpi=100)
    # sns.heatmap(data=d,annot=True,fmt='.20g',cmap=matplotlib.cm.Spectral)
    # plt.title("Effects of Educational Level and Job Type on Non-citizen Income",fontdict={'fontsize':20})
    # plt.show()

    with open("nonMigrate_2019.csv","r") as file:
        for lines in file:
            lines=lines.split(",")
            if(len(lines))>2:
                income=lines[7].strip()
                if(lines[7][0]=='"'):
                    income=lines[7][1:]
                if(lines[0]=="BPL"):
                    print("start")
                elif (int(lines[5])>0):
                    if income=='9999999':
                        print("This value is null")
                    elif int(income)<int(9999999):
                        income=int(income)
                        lines[7]=income

                        educ=lines[3].strip()
                        classWork=lines[5].strip()
                        if(educ[0]=='"'):
                            educ=educ[1:]
                        educ=int(educ)
                        if(classWork[0]=='"'):
                            classWork=classWork[1:]
                        classWork=int(classWork)

                        if income < 0:
                            if classWork==1:
                                selfLess0 += 1
                            else:
                                wageLess0+=1
                            if educ>1 and educ<7:
                                noHigherThanK12Less0+=1
                            else:
                                higherThanK12Less0+=1
                        elif income < 1000:
                            if classWork == 1:
                                selfLess1000 += 1
                            else:
                                wageLess1000 += 1
                            if educ > 1 and educ < 7:
                                noHigherThanK12Less1000 += 1
                            else:
                                higherThanK12Less1000 += 1

                        elif income < 10000:
                            if classWork == 1:
                                selfLess10000 += 1
                            else:
                                wageLess10000 += 1
                            if educ > 1 and educ < 7:
                                noHigherThanK12Less10000 += 1
                            else:
                                higherThanK12Less10000 += 1
                        elif income < 100000:
                            if classWork == 1:
                                selfLess100000 += 1
                            else:
                                wageLess100000 += 1
                            if educ > 1 and educ < 7:
                                noHigherThanK12Less100000 += 1
                            else:
                                higherThanK12Less100000 += 1

                        elif income < 1000000:
                            if classWork == 1:
                                selfLess1000000 += 1
                            else:
                                wageLess1000000 += 1
                            if educ > 1 and educ < 7:
                                noHigherThanK12Less1000000 += 1
                            else:
                                higherThanK12Less1000000 += 1


    file.close()


    columnName=['<0','<1000','<10000','<100000','<1000000']
    rowName=['<=K12','>K12','self','wage']
    values=[[noHigherThanK12Less0,higherThanK12Less0,selfLess0,wageLess0],[noHigherThanK12Less1000,higherThanK12Less1000,selfLess1000,wageLess1000],[noHigherThanK12Less10000,higherThanK12Less10000,selfLess10000,wageLess10000],[noHigherThanK12Less100000,higherThanK12Less100000,selfLess100000,wageLess100000],[noHigherThanK12Less1000000,higherThanK12Less1000000,selfLess1000000,wageLess1000000]]
    d=pd.DataFrame(values,columnName,rowName)
    plt.figure(figsize=(11,9),dpi=100)
    sns.heatmap(data=d,annot=True,fmt='.20g',cmap=matplotlib.cm.Spectral)
    plt.title("Effects of Educational Level and Job Type on citizen Income",fontdict={'fontsize':20})
    plt.show()






