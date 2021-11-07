def PairCount(array, n ,sum):
    count = 0  
    for i in range(0, n):
        for j in range(i + 1, n):
            if array[i] + array[j] == sum:
                count += 1
 
    return count
 
 

array = [1, 3, 6, 2, 2, 0, 4, 5]
n = len(array)
sum = 5
print(PairCount(array, n, sum))