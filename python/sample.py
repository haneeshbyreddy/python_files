# Find the first unique element in a stream of characters 
# at any given point.

MAX_CHAR_SIZE = 256

def find_first_unique_char(msg):

    # charDLL is doubly linked list.
    # if x is present in DLL, charDLL[x] contains pointer to a DLL node. 
    # If x is not present in DLL, then charDLL[x] is NULL
    charDLL = [] * MAX_CHAR_SIZE

	# repeated is the list of boolean values.
    # Here, repeated[x] is true if x is repeated two or more times. 
    # Else, False
    
    repeated = [False] * MAX_CHAR_SIZE

    out = ""
    for i in range(len(msg)):
        ch = msg[i]

        # We process this character only if it has nomat occurred
        # or occurred only once. repeated[x] is true if x is
        # repeated twice or more.
        if not repeated[ord(ch)]:

            # If the character is not in charDLL, then add this
            # at the end of DLL
            if not ch in charDLL:
                charDLL.append(ch)
            else:
                charDLL.remove(ch)
                repeated[ord(ch)] = True

        if len(charDLL) != 0:
            out += charDLL[0]

    return out



msgs = ["abcdabc", "csestacklearnprogrammingpracticaly"]
for msg in msgs:
    print("\nInput string:")
    print(msg)
    print("Output string:")
    out = find_first_unique_char(msg)
    print(out)