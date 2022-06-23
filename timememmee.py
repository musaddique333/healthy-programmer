import time
t = time.time()
while True:
    x = time.time()
    if x == t + 5:
        print("after 5 seconds")
        t = t + 5
