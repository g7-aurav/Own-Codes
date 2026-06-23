from loguru import logger
new_list = []
for i in range(1,11):
    if i%2 == 0:
        new_list.append(i)
logger.info(new_list)

new_list = [i for i in range(1,11) if i%2 == 0]
logger.info(new_list)

new_list = []
for i in range(1,11):
    if i%2 == 0:
        new_list.append("even")
    else:
        new_list.append("odd")
logger.info(new_list)

new_list = ["even" if i%2 == 0 else "odd" for i in range(1,11)]
logger.info(new_list)

squares = []
for x in range(10):
    if x % 2 == 0:
        squares.append(x**2)
logger.info(squares)
# Output: [0, 4, 16, 36, 64]

squares = [x**2 for x in range(10) if x % 2 == 0]
logger.info(squares)
# Output: [0, 4, 16, 36, 64]

names = ["Alice", "Bob", "Alex", "Charlie"]
a_names = [name for name in names if name.startswith("A")]
logger.info(a_names)
# Result: ['Alice', 'Alex']


names = ["Alice", "Bob", "Alex", "Charlie"]
# If name starts with 'A', keep it; otherwise, label as 'Other'
a_names = [name if name.startswith("A") else "Other" for name in names]

logger.info(a_names)