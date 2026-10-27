operation = input("Enter an operation (+, -, *, /): ").strip()

first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))

if operation == "+":
	result = first + second
elif operation == "-":
	result = first - second
elif operation == "*":
	result = first * second
elif operation == "/":
	if second == 0:
		raise ValueError("Cannot divide by zero.")
	result = first / second
else:
	raise ValueError("Unsupported operation. Use +, -, *, or /.")

print(f"Result: {result}")
