import numpy as np




# 10) accept start, end and how many numbers to be generated and then using "linspace" create numpy array.
# arr=[[10,20,30,40,50,60,70,80,90,100,110,120]]
# arr = np.linspace(10,100,10)
# print(arr)

# 12) create 2 d array (4*3) with following values:
# [[10,20,30,40],[50,60,70,80],[90,100,110,120]]
# arr=np.array([[10,20,30,40],[50,60,70,80],[90,100,110,120]])
# arr.shape=4,3
# print(arr)
# print(arr[1, :])
# print(arr[2:,1:3])
# print(arr[0][2],arr[1][2],arr[2][2])
# print(arr[[0,1,2],[2,2,2]])
# print(arr[1:,:2])
# print(arr[[1, 1, 2, 2], [0, 1, 0, 1]])  # [50 60 90 100]

# 11) create one-d array of 8 numbers and then using "slicing" concept,
# 	a) print numbers from 1 to 4
# 	b) print all the numbers from 3rd position
# 	c) print last 3 numbers
# arr=np.array([1,2,3,4,5,6,7,8])
# print(arr[:4])
# print(arr[2:])
# print(arr[-3::])

# 9) create two-d array ,display it. Now accept a number from user and perform all arithmetic operations on each and every element of the array using that number.
# arr1=np.array([[1,2],[3,4]])
# ar=arr1*2
# print(ar)
# ar1=arr1/2
# print(ar1)
# ar2=arr1-2
# print(ar2)
# ar3=arr1+2
# print(ar3)

# 8) declare two 2d arrays and calculate the sum as per "axis=0" "axis=1" and "axis=2"
# arr1=np.array([[1,2],[3,4]])
# print(arr1.ndim)

# 7) accept no.of rows and no. of cols from the user , create two-d array accordingly. Now calculate the sum as per "axis=0" and "axis=1"
# row=3
# col=2
# lst=[i for i in range(1, row*col+1)]
# print(lst)
# ar=np.array(lst)
# ar.shape=row,col
# print(ar)

# setdiff1d   intersect1d     union1d
# 6) create two one-d arrays and then find out:
# 	a) common elements of both the array
# 	b) unique elements of first array
# 	c) unique elements of second array
# arr1=([1,4,2,3])
# arr2=([2,9,3,6])
# arr4=np.intersect1d(arr1, arr2)
# print(arr4)
# arr5=np.setdiff1d(arr1, arr2)
# print(arr5)
# arr6=np.setdiff1d(arr2, arr1)
# print(arr6)
# arr3=np.union1d(arr1, arr2)
# print(arr3)

# 5) create two double dimension array and arrange (stack) them using "axis=0" "axis=1" and  "axis=2".
# arr1= np.array([[10,20,30],[40,50,60]])
# arr2=np.array([[70,80,90],[100,110,120]])
# a1=np.dstack((arr1, arr2))
# print(a1)
# a2=np.vstack((arr1, arr2))
# print(a2)
# a3=np.hstack((arr1, arr2))
# print(a3)
# ar1=np.stack((arr1,arr2), axis=0)
# print(ar1)
# ar2=np.stack((arr1,arr2), axis=1)
# print(ar2)
# ar3=np.stack((arr1,arr2), axis=2)
# print(ar3)

# 4) create one-d numpy array of 12 elements , accept 12 numbers and display them. Now convert this one-d array into (4*3) two-d array and display it in a tabular form.
# arr=np.array([i for i in range(1, 13)])
# arr.shape=4,3
# print(arr)

# doubt
# arr=np.array([i%2==0 and i>10 for i in range(12)])
# arr1=arr[arr]
# print(arr1)
# for i in arr:
#     print(i)


#1) create a list, accept 5 numbers , store them in the list and finally convert that list to numpy array.
# 2) create numpy array of 5 numbers and print their sum
# arr=np.arange(5)
# arr=np.array([1,2,3,4,5])
# print(arr.sum())
# print(arr)

# 3) create numpy double dimension array of 3*3 to store your initial and display them in a tabular form.
# arr=np.array([i for i in range(4,13)])
# arr.shape=[3,3]    ##row, number
# print(arr)




# str= input("enter string: ")
# lst= list(str.split(' '))
# print(lst[::-1])


# str= input("enter string: ")
# lst=['a','e','i','o','u']
# count=0
# for i in str:
#     if i in lst:
#         count+=1
# print(count)

# lst1=['ram','priyank','pratik','riya']
# lst1.sort()
# print(lst1)
# lst1.sort(reverse=True)
# print(lst1)

# lst=[1,2,3,4,5,6,7]
# lst.sort()
# print(lst[-2])




