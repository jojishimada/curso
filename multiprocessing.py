from multiprocessing import process

def numbers(start_num):
    for i in range(5):
        print(start_num+i, end=' ')

if __name__ == '__main__':
    p1 = process(target=numbers, args=(1,))
    p2 = process(target=numbers, args=(10,))
    p1.start()
    p2.start()
    # wait for the processes to finish
    p1.join()
    p2.join()

# output:
# 1 2 3 4 5 10 11 12 13 14