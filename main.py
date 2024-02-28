import sqlite3 as s
import matplotlib.pyplot as plt

database = s.connect("database.db")
cursor = database.cursor()

def str_to_float(ch):
    ind = ch.index(",")
    ch1 , ch2 = ch[:ind] , ch[ind+1:]
    ch1 = ch1[ : :-1]
    f= 0
    for i in range(len(ch1)):
        f += int(ch1[i]) * 10**i
    for i in range(len(ch2)):
        f += int(ch2[i]) * 10**-(i+1)
    return(f)

def reform(l):
    ll = []
    for i in range(1,len(l)):
        ll.append(l[i][0])
        try :
            ll[i] = float(ll[i])
        except :
            pass
    return(ll)

for i in range(40,147):

    res1 = cursor.execute(f"SELECT field{i} FROM liver_tumors as t WHERE t.field2 ='CCK' ")
    l1 = reform(res1.fetchall())
    res3 = cursor.execute(f"SELECT field{i} FROM liver_tumors as t WHERE t.field2 ='CHC' ")
    l3 = reform(res3.fetchall())
    res5 = cursor.execute(f"SELECT field{i} FROM liver_tumors as t WHERE t.field2 ='Mixtes' ")
    l5 = reform(res5.fetchall())
    for j in range(40, 147):

        if i != j :

            res2 = cursor.execute(f"SELECT field{j} FROM liver_tumors as t WHERE t.field2 ='CCK' ")
            l2 = reform(res2.fetchall())
            res4 = cursor.execute(f"SELECT field{j} FROM liver_tumors as t WHERE t.field2 ='CHC' ")
            l4 = reform(res4.fetchall())
            res6 = cursor.execute(f"SELECT field{j} FROM liver_tumors as t WHERE t.field2 ='Mixtes' ")
            l6 = reform(res6.fetchall())

            plt.figure()
            plt.scatter(l1,l2, s=4, label="CCK")
            plt.scatter(l3, l4, s=4, label="CHC")
            plt.scatter(l5, l6, s=4, label="Mixtes")
            plt.title(f'field{i}=f(field{j})')
            plt.legend()

            plt.savefig(f'graph/field{i}=f(field{j}).png')
            plt.close()