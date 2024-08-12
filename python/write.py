
def write_file(data,l) :
	with open("output.txt", "a+") as fopen:
		fopen.write(data)
		for i in l :
			fopen.write(str(i)+' ')
		fopen.write("\n")
	fopen.close()
