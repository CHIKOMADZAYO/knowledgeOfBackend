# import time


# start=time.time()
# num1=int(input("Enter First  Number:  "))

# num2=int(input("Enter Second  Number: "))

# num3=int(input("Enter Third Number:  "))


# # if num1 > num2 and num1 > num3:
# #     largest = num1
# # elif num2 > num1 and num2 > num3:
# #     largest = num2
# # else:
# #     largest = num3

# # print(f"The largest number is {largest}")

# stop=time.time()

# end=start-stop

# print(end)


# start=time.time()
# l=[num1,num2,num3]

# largest=[m for m in l ]


# for i in range(len(largest)):
#     nm=max(largest)

# print(nm)

# stop=time.time()

# end=start-stop

# print(end)




import time

num1=int(input("Enter First  Number:  "))
num2=int(input("Enter Second  Number: "))
num3=int(input("Enter Third Number:  "))


start = time.perf_counter()

numbers = [num1, num2, num3]
largest = max(numbers)

print("Largest number:", largest)

stop = time.perf_counter()
elapsed = (stop - start)*1000

print("Execution time:", elapsed, "seconds")