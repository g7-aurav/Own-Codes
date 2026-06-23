from loguru import logger
labour_name = ['Mahesh','Ramesh','Mithlesh','Sumesh']
logger.info(f"second element in the list is {labour_name[1]}")
labour_name.append("Ram")
logger.info(f"elements in the list is {labour_name}")
#for more than 1 to add
labour_new = ['Mohan','Sohan']
labour_name.extend(labour_new)
logger.info(f"total element in the list is {labour_name}")
# inserting in index position
labour_name.insert(1,'Ramlal')
logger.info(f"updated element in the list is {labour_name}")

# Multidimensional list
labour_with_cost = [['Mahesh',500],['Ramesh',400],['Mithlesh',400],['sumesh',300]]
logger.info(labour_with_cost[1][0])
# best method
labour_name = labour_name + labour_new
logger.info(labour_name)
logger.info(labour_name[0:3])
print(len(labour_name))
# pop will delete last value
logger.info(labour_name.pop())
logger.info(labour_name.pop(2))
labour_name.remove("Ram")
print(labour_name)
# updating name
labour_name[2]= "Mitlesh"
print(labour_name)
# split
URL = "D:\\GAURAV\\My Learnings\\Spark Tutorials Youtube\\Data Bricks Notebook\\If Else"
New_URL = URL.split("\\")
logger.info(New_URL)
logger.info(New_URL[-2])