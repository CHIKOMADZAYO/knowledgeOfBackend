units = float(input("Enter the number of units consumed: "))

if units <= 100:
	bill = units * 25
elif units <= 200:
	bill = 100 * 25 + (units - 100) * 35
elif units <= 300:
	bill = 100 * 25 + 100 * 35 + (units - 200) * 45
else:
	raise ValueError("The billing rates only cover up to 300 units.")

print(f"Electricity bill: {bill}")