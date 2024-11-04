
class gp:
    def old(self):
        print("walk slowly")

class par(gp):
    def young(self):
        print("walk")
ref=par()

if isinstance(ref, par):
    ref.young()

if hasattr(par(), "young"):
    par().young()

if hasattr(par(), "young"):
    ref.young()
else:
    print("not young")





# st="my name is akshay"
# lst=list(st.split())
# max=0
# word=''
# for i in lst:
#     if len(i)>max:
#         max=len(i)
#         word=i
# print(lst)
# print("biggest word in sentence: ", max)
# print("word is: ", i)

import numpy as np
# ser = np.array([[1,2,3,4,5],[9,8,7,6,5]])
# ser=np.arange(12,20).reshape(2,2,2)
# ser= np.array([1,2,3,4,5])
# ser1= np.array([9,8,7,6,5])
# ser3=np.stack((ser,ser1), axis=1)
# print(ser3)
# print(ser.ndim)
# print(ser)

# class student:
#     def __init__(self, name, age, address, qual):
#         self.name=name
#         self.age=age
#         self.address=address
#         self.qual=qual
#     def __str__(self):
#         return f'{self.name}, {str(self.age)}, {self.address}, {self.qual}'
# s1=student('ram', 27, 'lalbaug', 'btech')
# s2=student('priyank', 22, 'dadar', 'mca')
# s3=student('affan', 23, 'kurla', 'be')
# print(s1.name)
# dic={1:s1, 2:s2, 3:s3}
# for i,j in dic.items():
#     print(i, j )


# import pandas as pd
# mydict={'ram':27, 'priyank':24, 'pratik':22}
# df2=pd.Series(mydict)
# # print(df2)
# print(df2.sum())
# print(df2.add(2))
# print(df2.sub(3))
# print(df2.mul(10))


# print(df2[1:2])






# name= {}
# for i in range(3):
#     n=input("enter name")
#     runs=int(input("enter runs"))
#     name[n]=runs
# df1=pd.Series(name)
# print(df1)

# mydict={'name':['ram', 'priyank', 'pratik'], 'age': [27,24,22]}
# df=pd.DataFrame({'name':['ram', 'priyank', 'pratik'], 'age': [27,24,22]}, index=[1,2,3,])
# print(df)

# 5) accept 5 names,designations and salaries and display them with DataFrame.

# dic={}
# names=[]
# desig=[]
# salaries=[]
# for i in range(2):
#     name=input("enter name")
#     names.append(name)
#     design=input("enter designation")
#     desig.append(design)
#     salary=int(input("enter salary"))
#     salaries.append(salary)
# dic={'names':names, 'designations':desig, 'salaries': salary}
# df=pd.DataFrame(dic)
# print(df)

# df1=pd.Series(desig, index=names)
# print(df1)


# f = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
# flst=f.values.tolist()
# flst1=f.to_string()
# print(f+10)
# print(f[1:3])
# print(f.iloc[1:3])
# print(f.loc['a':'c'])


#
# print(flst)
# print(flst1)

# df=pd.DataFrame({'names':[], 'designation':[], 'salary':[] })
# for i in range(3):
#     df['names', 'designation', 'salary']=('ram','deve',234)
# print(df)


# df= pd.DataFrame({'name':['ram', 'priyank', 'pratik'],'marks':[98,99,95]}, index=[1,2,3])
# print(df)

# print(df.iloc[0, :2])


# from abc import ABC, abstractmethod
# class ab(ABC):
#     def start(self):
#         pass
# class ab1(ab):
#     def start(self):
#         print("ab1 start")
# a=ab1()
# a.start()

# pal=lambda st: st==st[::-1]
# print(pal('madam'))

# from multipledispatch import dispatch
#
# @dispatch()
# def fun():
#     print("fun")
# @dispatch(int)
# def fun(num):
#     print(num)
# @dispatch(int, str)
# def fun(num, name):
#     print(name, num)
# fun()
# fun(23)
# fun(23, 'rj')


# def decor_functio(fun):
#     def with_init_releas():
#         print("initialise")
#         fun()
#         print("release")
#     return with_init_releas
# @decor_functio
# def func():
#     print("in func")
# func()

# def outer():
#     def inner():
#         print("inner")
#     print("outer")
# outer()



# def fun(arg):
#     if callable(arg):
#         arg()
#     else:
#         print("it is not callble arg")
# def disp():
#     print("disp")
# dip=100
# fun(dip)


