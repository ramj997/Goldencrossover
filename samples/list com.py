
var=500 # global variable
print("Value of global var is\t",var)
def myfun():
    global var # try commenting this line
    print(var)
    var=300 # changing global variable
    print("var inside main\t",var) # by default local is given
# precedence
myfun()
print("Value of global var is\t",var)


# lst=[1,2,3]
# lst2=[4,5,6]
#
# dct={key:value for key, value in zip(lst, lst2)}
# dct=[i for i in range(3,20) if i%2==0]
# print(dct)

# class sample:
#     def __init__(self, num):
#         self.num=num
#     def __add__(self, numm):
#         return self.num+numm.num
#
#     def __mul__(self, numm):
#         return self.num*numm.num
#     def __sub__(self, numm):
#         return self.num-numm.num
#
#
# s1=sample(7)
# s2=sample(5)
# s3=sample(8)
# s4=sample(12)
# s5=s4-s1+s3*s1
# print(s5)
# print(s1+s2)

# class Votingnotallowed(Exception):
#     pass
# class voter:
#     def __init__(self, name, age):
#         if age<18:
#             raise Votingnotallowed("age should be greater than 18")
#         self.name=name
#         self.age=age
# try:
#     s = voter('ram', 9)
#     print(s.name, s.age)
# except Votingnotallowed as e:
#     print(e)
# finally:
#     print("done")

# if age<18:
#     raise Votingnotallowed("under age")
# else:
#     print("you have successfully voted")
#

# class sample:
#     def __init__(self, num):
#         self.num=num
#     def __add__(self, other):
#         return sample(self.num-other.num)
#     def __mul__(self, other):
#         return sample(self.num*other.num)
#     def __str__(self):
#         return str(self.num)
#
# c=sample(19)
# c1=sample(10)
# c2=sample(2)
# add= c+c1*c2
# print(add)

