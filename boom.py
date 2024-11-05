import time

times = int(input("Enter the time is secounds: "))

for i in range(times,0,-1):
    sec = i % 60
    mint = int(i/60) % 60
    hour = int(i / 3600)
    print(f"{hour:02}:{mint:02}:{sec:02}")
    time.sleep(1)


print("** Boooom **")