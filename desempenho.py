import time
import multiprocessing

start = time.perf_counter()

lista = []

def fazer():
    for i in range(100):
        lista.append(i)

p = multiprocessing.Process(target=fazer())
p.start()
 
print(lista)

finish = time.perf_counter()

print(f'demorou {round(finish-start,2)} segundos')