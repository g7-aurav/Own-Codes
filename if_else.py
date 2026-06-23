from loguru import logger
import math
length_of_land = 100
breadth_of_land = 100
bricks_cost_per_peice = 10.5
labour_mistri1 = "Jagmohan"
labour_mistri2 = "Rampyare"
is_home = True

length_of_land = int(input("enter the length of land : "))
if (length_of_land <100):
    logger.info(f"Your length is not sufficient to build 4 BHK")
    if (length_of_land >80):
        logger.info(f"you can build 3 bhk")
    else:
        logger.info(f"your land is not haveing proper space")
elif (length_of_land>=500):
    logger.info(f"you can build more than 2 buildings")
else:
    logger.info("share more details with us")