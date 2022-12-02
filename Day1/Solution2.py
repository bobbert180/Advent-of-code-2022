if __name__ == "__main__":
    f = open("input1.txt", "r")
    numberList = []
    j = 0
    prev = 1000000
    current = 0
    for line in f:
        t = line.strip()
        numberList.append(t)
        #numberList.append(str(t))
        #numberList.append(float(t))
    x = len(numberList)
    for i in range(x - 2): #
        current = int(numberList[i]) + int(numberList[i + 1]) + int(numberList[i + 2])
        if(int(current) > int(prev)):
            j = j + 1
        prev = current
        print(numberList[i + 2])
    print(j)
