from loguru import logger
import math
length_of_land = 100
breadth_of_land = 100
bricks_cost_per_peice = 10.5
labour_mistri1 = "Jagmohan"
labour_mistri2 = "Rampyare"
is_home = True

#clculate total area of land

total_area_of_land =  length_of_land * breadth_of_land
perimeter_of_land = 2 *( length_of_land + breadth_of_land)

# Modulo operator
print(15%6)
print(15//6)

print(math.floor(15/7))
print(math.ceil(15/7))

logger.info(f"Total perimeter of land is {perimeter_of_land}")
logger.info(f"Total are of my land is {total_area_of_land}")

length_of_land = input("Please enter the length of land :")
breadth_of_land = input("Please enter the breadth of land :")

total_area_of_your_land = int(length_of_land) * int(breadth_of_land)
logger.info(f"Total area of your land is {total_area_of_your_land}")