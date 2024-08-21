from time import sleep
x = 1
for i in range(100):
    print("HEI! :D", x)
    sleep(0.1)
    x = x + 1
    if x >= 100:
        break 