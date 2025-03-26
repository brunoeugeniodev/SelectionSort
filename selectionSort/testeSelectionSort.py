import time
from selectionSort import selection_sort

lista = [11, 4, 30, 22, 7, 26]

print("Lista desordenada: ", lista)

inicio = time.time()
selection_sort(lista)
fim = time.time()

print("Lista ordenada: ", lista)

print(f"Tempo gasto: {fim - inicio:.6f} segundos", flush=True)