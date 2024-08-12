'''import pdb 
breakpoint()
def decor(func):
    def inner(name):
        print("decor "+name )
        func(name)
    return inner
def decor1(func):
    def inner(name):
        print("Decor1")
        func(name)
        
    return inner


@decor1
@decor
def num(name):
    print("hello "+name+" good maorning")
num("srivalli")
'''
def maxArea(height):
    maxele=max(height)
    index1=height.index(maxele)
    print(index1)
    list2=set(height)
    if height[index1] in list2:
        list2.remove(height[index1])
    print(list2)
    minele=max(list2)
    print(minele)
    index2=height.index(minele)
    print(index2)
    sum=1
    for i in range(index1,index2+1):
        print(height[i])
        sum*=height[i]
    print(sum)
List=[1,8,6,2,5,4,8,3,7]
maxArea(List)