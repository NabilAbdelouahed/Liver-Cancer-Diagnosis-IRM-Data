import sqlite3 as s
import matplotlib.pyplot as plt
import numpy as np
import math


def reform(l):
    ll = []
    for i in range(0,len(l)):
        try :
            ll.append(l[i][0])
        except :
            ll.append(None)
    return(ll)

# res1 = cursor.execute("SELECT field147 FROM liver_tumors as t  ")
# l= res1.fetchall()
# l = reform(l)

def create_mat() :
    database = s.connect("database.db")
    cursor = database.cursor()
    res = cursor.execute("SELECT * FROM liver_tumors as t")
    patient = []
    cancer = []
    phase = []
    l_pat = []

    for row in res :
        l_pat1 = row[39:-2]
        valid = True
        for i in range(len(l_pat1)):
            if l_pat1[i] == None :
                valid = False
                break
        if valid == True :
            patient.append(row[-2])
            cancer.append(row[1])
            phase.append(row[-1])
            l_pat.append(list(l_pat1))
    patient = patient[1:]
    cancer = cancer[1:]
    phase = phase[1:]
    l_pat = l_pat[1:]

    for i in range(len(patient)):
        patient[i]= float(patient[i])
        for j in range(len(l_pat[i])):
            l_pat[i][j] = float(l_pat[i][j])


    for i in range(len(patient)-1) :
        min = patient[i]
        for j in range(i+1,len(patient)) :
            if patient[j] < patient[i] :
                patient[i], patient[j] = patient[j], patient[i]
                cancer[i], cancer[j] = cancer[j], cancer[i]
                l_pat[i], l_pat[j] = l_pat[j], l_pat[i]
                phase[i], phase[j] = phase[j], phase[i]

    i = 0
    while i < (len(patient)-1) :
        j = i+1
        while patient[i]==patient[j] and j <len(patient)-1:
            if cancer[j] == cancer[i] :
                cancer[i+1], cancer[j] = cancer[j], cancer[i+1]
                l_pat[i+1], l_pat[j] = l_pat[j], l_pat[i+1]
                phase[i+1], phase[j] = phase[j], phase[i+1]
            j +=1
        i+=1
    pat_can = []
    for i in range(len(patient)):
        pat_can.append((patient[i],cancer[i]))

    j = 0
    while j <len(pat_can) :
        key = pat_can[j]
        if pat_can[j] != pat_can[j+3]:
            while pat_can[j] == key :
                pat_can.pop(j)
                phase.pop(j)
                l_pat.pop(j)
                j -= 4
        j +=4

    mat = [[None for i in range(5)] for j in range(len(pat_can)//4)]

    for i in range(0,len(pat_can),4):
        mat[i//4][0] = pat_can[i]
        for j in range(4):
            if phase[i+j] == 'ART':
                mat[i // 4][1] = l_pat[i+j]
            elif phase[i+j] == 'PORT':
                mat[i // 4][2] = l_pat[i+j]
            elif phase[i + j] == 'VEIN':
                mat[i // 4][3] = l_pat[i+j]
            elif phase[i + j] == 'TARD':
                mat[i // 4][4] = l_pat[i+j]

    z = 0
    while z < len(mat) :
        if mat[z][0] == (3,"CCK") or mat[z][0] == (11,"CCK") or mat[z][0] == (20,"CHC") or mat[z][0] == (58,"CHC") or mat[z][0] == (96,"CHC") or mat[z][0] == (32,"Mixtes") :
            mat.pop(z)
            z -= 1
        z+=1

    return(mat)

def create_vect_x_y(mat) :
    x , y = [] , []
    for i in range(len(mat)):
        if mat[i][0][1] != 'Mixtes' :
            for j in range(4,1,-1):
                for k in range(1, j):
                    a = np.array(mat[i][j])-np.array(mat[i][k])
                    a = list(a)
                    y.append(mat[i][0][1])
                    x.append(a)
    return( x , y )

def etiquette_y(y) :
     etiquette = {'CHC':1 , 'CCK':2}
     l = []
     for cancer in y:
         l.append(etiquette[cancer])
     return(l)

def etiquette_y_1(y):
    etiquette = {1:'CHC', 2: 'CCK'}
    l = []
    for i in y:
        l.append(etiquette[i])
    return (l)