def countfiles():
    filename=input("Enter the file name: ")
    file=open(filename,"r")
    numberofwords=0
    for line in file:
        words=line.split()
        numberofwords=numberofwords + len(words)

    print("Number of words")      
    print(numberofwords)

countfiles()