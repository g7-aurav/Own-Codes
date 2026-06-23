from loguru import logger
labour_with_cost = {"Mahesh":500,"Ramesh":400,"Mithlesh":400,"Sumesh":300}
labour_with_cost["Jagannath"] = 1000
labour_with_cost["Rampyare"] = 800

logger.info(labour_with_cost.keys())
logger.info(labour_with_cost.values())
logger.info(labour_with_cost.items())

# logger.info(labour_with_cost)

# for abc in labour_with_cost:
#     print(abc)
# So basically its giving key
for name in labour_with_cost:
    logger.info(f"{name},{labour_with_cost[name]}")

for key,value in labour_with_cost.items():
    logger.info(f"{key},{value}")


final_list =[]
for key,value in labour_with_cost.items():
    final_list.append(f"{key} = {value}")
logger.info(final_list)

# Total labour cost if total working days was 50
# out of whih mahesh was absent for 3 days and jagmohan 7 days
# find total labour cost

cost = 0
for name in labour_with_cost:
    cost = cost + 50*(labour_with_cost[name])
cost = cost - 3*int((labour_with_cost["Mahesh"])) - 7*int((labour_with_cost["Jagannath"]))
print(cost)