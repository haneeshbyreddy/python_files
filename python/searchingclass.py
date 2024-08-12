import functions as bub

class File1:

    # Code for hemanth.txt
    '''
    with open("hemanth.txt", "r") as fopen:
        list1 = []
        lines = fopen.readline()
        list1.extend(map(int, lines.split()))
    '''

    # Code for 2602.txt here the input is line by line
    with open("2602.txt", "r") as fopen:
        list1 = []
        line = fopen.readline().rstrip()
        while line != "":
            list1.append(int(line))
            line = fopen.readline().rstrip()
        list1=bub.bubble_sort(list1)
    fopen.close()

class Linear_Search(File1):
    def myfun(self):
        print("The list of elements is : ", self.list1)
        key = int(input("Enter the Search Element : "))
        y = bub.linear_search(self.list1, key)
        if y != -1:
            data = "Linear_Search Element : "
        else:
            data = "Linear_Search Element is not found : "
        bub.write_file(data, y)

class Binary_Search(File1):
    def myfun(self):
        print("The list of elements is : ", self.list1)
        key = int(input("Enter the Search Element : "))
        y = bub.binary_search(self.list1, key)
        if y != -1:
            data = "Binary_Search Element : "
        else:
            data = "Binary_Search Element is not found : "
        bub.write_file(data, y)

class Terenary_Search(File1):
    def myfun(self):
        print("The list of elements is : ", self.list1)
        key = int(input("Enter the Search Element : "))
        y = bub.terenary_search(self.list1, key)
        if y != -1:
            data = "Terenary_Search Element : "
        else:
            data = "Terenary_Search Element is not found : "
        bub.write_file(data, y)

class Exponential_Search(File1):
    def myfun(self):
        print("The list of elements is : ", self.list1)
        key = int(input("Enter the Search Element : "))
        y = bub.exponential_search(self.list1, key)
        if y != -1:
            data = "Exponential_Search Element : "
        else:
            data = "Exponential_Search Element is not found : "
        bub.write_file(data, y)

class Interpolation_Search(File1):
    def myfun(self):
        print("The list of elements is : ", self.list1)
        key = int(input("Enter the Search Element : "))
        y = bub.interpolation_search(self.list1, key)
        if y != -1:
            data = "Interpolation_Search Element : "
        else:
            data = "Interpolation_Search Element is not found : "
        bub.write_file(data, y)

class Jump_Search(File1):
    def myfun(self):
        print("The list of elements is : ", self.list1)
        key = int(input("Enter the Search Element : "))
        y = bub.jump_search(self.list1, key)
        if y != -1:
            data = "Jump_Search Element : "
        else:
            data = "Jump_Search Element is not found : "
        bub.write_file(data, y)

if __name__ == "__main__":
    num = 1
    while num != 0:
        print("1.Linear Search\n2.Binary Search\n3.Terenary Search\n4.Exponential Search\n5.Inter-Polation Search\n6.Jump Search\n0.Exit\n")
        num = int(input("Enter the choice : "))
        match num:
            case 1:
                x = Linear_Search()
                x.myfun()
            case 2:
                x = Binary_Search()
                x.myfun()
            case 3:
                x = Terenary_Search()
                x.myfun()
            case 4:
                x = Exponential_Search()
                x.myfun()
            case 5:
                x = Interpolation_Search()
                x.myfun()
            case 6:
                x = Jump_Search()
                x.myfun()
            case 0:
                f = open("output.txt", "w")
                f.close()
                print("Exiting The program")
            case _:
                print("Invalid")

