from loguru import logger
def final_cart_amount(*args,discount=0.1):
    result = 0
    for amount in args:
        result= result + amount
    print(result)
    amount_after_discount = result - (result*discount)

    return amount_after_discount

final_amount_tobe_paid = final_cart_amount(100,500,100,300,500,discount = 0.5)

logger.info(final_amount_tobe_paid)

#Q1 Write a program where u need to take n number of inputs from user and return total sum of it

def sum_of_n(*sums):
    Number = 0
    for i in sums:
        Number = Number + i
    return Number

sumofnumberis = sum_of_n(1,1,1,1,1)
logger.info(sumofnumberis)
# GPT
def sum_of_inputs():
    total_numbers = int(input("How many numbers do you want to add? "))
    total_sum = 0

    for i in range(total_numbers):
        num = float(input(f"Enter number {i+1}: "))
        total_sum += num

    return total_sum

result = sum_of_inputs()
print("Total sum is:", result)

# Q2 write a program in which function take logs input from the user and write this into a file 
# def write_logs_to_file():
#     filename = "logs.txt"       # File where logs will be stored
#     log = input("Enter your log message: ")

#     with open(filename, "a") as f:   # 'a' means append mode
#         f.write(log + "\n")

#     print("Log written to", filename)

# # Call the function
# write_logs_to_file()
