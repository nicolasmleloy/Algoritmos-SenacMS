import time

i = 10

while(i > 0):
    print(i)
    time.sleep(1)
    i -= 1
    if(i == 0):
        print("FIM!")