def selection_sort_otimizado(array):
    n = len(array)
    for i in range(n // 2): 
        menor = i
        maior = i

        for j in range(i + 1, n - i): 
            if array[j] < array[menor]:
                menor = j
            elif array[j] > array[maior]: 
                maior = j

        if menor != i:
            array[i], array[menor] = array[menor], array[i]

        if maior == i:
            maior = menor

        if maior != n - i - 1:
            array[n - i - 1], array[maior] = array[maior], array[n - i - 1]
