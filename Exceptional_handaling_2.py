try:
    num = int("0")
    result = 100 / num
except ValueError:
    print("Conversion failed")
except ZeroDivisionError:
    print("Division by zero")
else:
    print("Result:", result)
finally:
    print("Execution completed")

squares = []
for x in range(10):
    if x % 2 == 0:
        squares.append(x**2)
print(squares)
# Output: [0, 4, 16, 36, 64]





