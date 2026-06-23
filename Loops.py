from loguru import logger
users = [
    {"name": "Alice", "role": "Admin"},
    {"name": "Bob", "role": "User"}
]

for user in users:
    logger.info(f"Name: {user['name']}, Role: {user['role']}")

data_list = [
    {"id": 1, "status": "active"},
    {"id": 2, "status": "pending"}
]

for entry in data_list:           # First loop: goes through the array
    for key, value in entry.items():  # Second loop: goes through the dictionary
        logger.info(f"{key}: {value}")


labour_name = ['Mahesh','Ramesh','Mithlesh','Sumesh']
# for name in labour_name:
#     logger.info(name)

# for name in labour_name:
#     logger.info(f"labour 1 name is {name}")

# for i in range(5,10):
#     print(i)

# for i in range(len(labour_name)):
#     print(i)
#     print(labour_name[i])

for i in range(len(labour_name)):
    print(f"labour {i+1} name is {labour_name[i]}")

for i in range(5):
    print(i)

for i in range(5):
    print(i*"*")

for i in range(21):
    if i%2 == 0:
        print(i)
   
for i in range(5,0,-1):
    print(i*"* ")

