'''import numpy as np

n=int(input())
list1=(map(int,input().split("\n")))
lenght=len(list1)

for i in range(lenght):
    k=0
    print(list1[i],end=",")
    k=k+1
    if k==50:
        print("\n")
        k=0

    '''
import numpy as np
1
2
3
4
5
6
# Input the number of elements
'''
n = int(input("Enter the number of elements: "))

# Input the elements one at a time

list1 = []
for _ in range(n):
    element = int(input())
    list1.append(element)

# Specify the number of elements per row
elements_per_row = 2

# Print the elements with the specified number of elements per row
k = 0
for i in range(n):
    print(list1[i], end=", ")
    k += 1
    if k == elements_per_row:
        print("\n")
        k = 0
        '''

file = open(r"E:\frnds\python\number.txt", 'r')

elements_per_row = 5
data = file.read().split()  # Split the data into individual elements

k = 0
for i in range(len(data)):
    print(data[i], end=", ")
    k += 1
    if k == elements_per_row:
        print("\n")
        k = 0

file.close()  # Don't forget to close the file after reading


