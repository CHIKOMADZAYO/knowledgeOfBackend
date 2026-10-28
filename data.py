import time

start=time.time()
marks=[65,90,70,98,79,83,100,130,300,400,120,350,45,9000]
total=0
for i in marks:
    total=total+i
average=total/len(marks)
print(f"{total}")
print(f"{average}")
end=time.time()

stop=start-end
print(stop)