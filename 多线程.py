from datetime import datetime
import time
import threading


def f1():
    print('hello python')
    time.sleep(3)
    print('f1 end')


def f2():
    print('f2 is start...')
    time.sleep(5)
    print('f2 id end')


def main():
    ti1 = time.time()
    f1()
    f2()
    ti2 = time.time()
    # print(t2 - t1)

ti1 = time.time()
threads = []
t1 = threading.Thread(target=f1, args=())
threads.append(t1)
t2 = threading.Thread(target=f2, args=())
threads.append(t2)

for i in threads:
    i.start()
ti2 = time.time()
print(ti2 - ti1)

# if __name__ == '__main__':
#     main()
