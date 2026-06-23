score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

#ternary approch- one liner
# return <value_if_true> if <condition> else <value_if_false>
age = 17
# Use a ternary to set `status` to "adult" if age >= 18, else "minor"
output =  "adult" if age >=18 else "minor"
print(output)

fruits = ["apple", "banana", "mango"]
# Use a ternary to set `result` to "found" if "mango" in fruits, else "not found"

result = "found" if "mango" in fruits else "not found"
print(result)

def get_discount(price, is_member):
    # Use a ternary to return price * 0.9 if is_member is True, else return full price
    return price * 0.9 if is_member else price

print(get_discount(100, True))   # → 90.0
print(get_discount(100, False))  # → 100

data = {"name": "Alice", "score": 85}
# Use a ternary to set `grade` to "pass" if "score" in data and data["score"] >= 50, else "fail"
grade = "pass" if "score" in data and data["score"] >= 50 else "fail"
print(grade)

