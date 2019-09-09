import threading, time

print('Start of program.')


def takeANap():
    time.sleep(5)
    print('Wake up!')


threadOjb = threading.Thread(target=takeANap)
threadOjb.start()
time.sleep(3)
print('End of program.')
