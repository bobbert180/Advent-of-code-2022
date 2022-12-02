if __name__ == "__main__":
    f = open("Day1/input1.txt", "r")
    i = 0
    elf = [0] * 1000
    for line in f:
        if line.strip():
            elf[i] += int(line)
        else:
            i = i + 1
    print(max(elf))
    j = max(elf)
    elf.remove(max(elf))
    j = j + max(elf)
    print(max(elf))
    elf.remove(max(elf))
    j = j+ max(elf)
    print(max(elf))
    print(j)