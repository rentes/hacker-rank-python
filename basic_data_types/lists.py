if __name__ == '__main__':
    N = int(input())
    list = []
    while N > 0:
        line = input()
        command = line.split()[0]
        if command == "insert":
            param1 = int(line.split()[1])
            param2 = int(line.split()[2])
            list.insert(param1, param2)
        elif command == "remove":
            param1 = int(line.split()[1])
            list.remove(param1)
        elif command == "append":
            param1 = int(line.split()[1])
            list.append(param1)
        elif command == "print":
            print(list)
        elif command == "sort":
            list.sort()
        elif command == "pop":
            list.pop()
        elif command == "reverse":
            list.reverse()
        N = N - 1
