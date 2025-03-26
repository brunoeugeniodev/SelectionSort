def selection_sort(array):
    n = len(array)
    for i in range(n):
        menor = i
        for j in range(i+1, n):           
            if(array[j] < array[menor]):
                menor = j


        if menor != i:
         array[i], array[menor] = array[menor], array[i]