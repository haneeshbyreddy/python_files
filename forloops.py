#printing the numbers using for loop
for i in range(int(input("enter the numbers do you want to print upto : "))):
    print(i)
#sum of first natural numbers
sum=0
for i in range(10):
    sum+=i
print("sum of the first natural 10 numbers is ",sum)

#factorials of an number
num=5
numbers=num
factorial=1
for i in range(1,num):
    factorial*=numbers
    numbers-=1
print("factarial of an  number ",num,"is ",factorial)




