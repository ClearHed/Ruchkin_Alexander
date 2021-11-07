def nextBigger(n):
    number = [int(i) for i in str(n)]
    ptr = len(number) - 1
    next_biggest = float('inf')
    next_biggest_counter = float('inf')



    if (len(number) == 1 or number == sorted(number, reverse = True)):
        return -1

    for i in range(len(number) -1, 0, -1):
        if(number[i] > number[i-1]):
            ptr -= 1
            break
        ptr -=1

    for i in range(ptr, len(number)):
        if(number[i] > number[ptr] and number[i] < next_biggest):
            next_biggest = number[i]
            next_biggest_counter = i
    number[ptr], number[next_biggest_counter] = number[next_biggest_counter], number[ptr]
    Nxtnumber = number[ptr+1:]
    Nxtnumber.sort()
    for i in range(len(Nxtnumber)):
        number[i+ptr+1] = Nxtnumber[i]

    number = [str(x) for x in number]
    S = ''.join(number)
    return int(S)


print(nextBigger(12))