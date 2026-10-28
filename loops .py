# for  i in range(1,11):
#     print(f"Welcome To Our School {i}")



# customers =["Willm","Bn","MB","PL"]
# for c in customers:
#     print(f"Welcome to the Shop!Customer {c}")



# my_shopping=[200,100,230,400]
# # New List created
# nl=[m/2 for m in my_shopping] #List Comprehension
# # print(m)

# print(nl)


# total=0

# for m in my_shopping:
#     total=total+m

# print(f"My total Shopping cost is {total}")




# # 5-customers
# # each pay 100 

# total=0
# for i in range(5):
#     total=total+100

# print(f"Total is {total}")


# money=0
# while money<=1000:
#     money=money+100
#     print(f"Money saved {money}")

# print("Congrats!You hit your target")

# from math import pi
import  time

start=time.time()
money=0
while money<=1000:
    money=money+100
    print(f"Money saved {money}")

print("Congrats!You hit your target")
end=time.time()

stop=start-end
print(stop)


start=time.time()*1000
marks=[65,90,70,98,79,83,100,130,300,400,120,350,45,9000]
largest=max(marks)
end=time.time()*1000

stop=start-end
print(stop)