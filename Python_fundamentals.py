import logging
from loguru import logger
# Basic configuration
logging.basicConfig(format='%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S',
    level=logging.DEBUG)

length_of_land = 100
breadth_of_land = 200
bricks_cost_per_peice = 10.5
labour_mistri1 = "Jagmohan"
is_home = True

print("length of land is ", length_of_land)

print("My home is of 4 BHK length of total land is 100")
# For new line we have to use \n
print("My home is of 4 BHK \nlength of total land is 100")
#use triple quote to multipline print
print("My home is of \t\"4BHK\" " )
#\t give 4 space

print("length of total land is", length_of_land,"Ft")

print(f"Cost of bricks per unit is {bricks_cost_per_peice} bricks cost per peice")

print("cost of bricks per unit is {} {} {}".format(bricks_cost_per_peice,length_of_land,labour_mistri1))

#logging


logging.info(f"Cost of bricks per unit is {bricks_cost_per_peice} bricks cost per peice")
logger.info(f"Cost of bricks per unit is {bricks_cost_per_peice} bricks cost per peice")
# print(length_of_land,breadth_of_land,labour_mistri1,is_home)
# print(type(length_of_land),type(breadth_of_land),type(labour_mistri1),type(is_home))

