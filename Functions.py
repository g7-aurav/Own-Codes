from loguru import logger

length_of_land = 100
breadth_of_land = 100

length_of_garden = 100
breadth_of_garden = 20

length_of_home = 80
breadth_of_home = 60

grass_cost_per_sq_ft = 10

def calculate_fencing_cost(length,breadth,cost_per_feet):
    circumference = 2*(length + breadth)
    cost_for_fencing = circumference * cost_per_feet
    return cost_for_fencing
cost_for_fencing_land = calculate_fencing_cost(length_of_land,breadth_of_land,17)

logger.info(f"fencing cost of land is {cost_for_fencing_land} ")

def grass_area(L1,B1,L2,B2,L3,B3,cost_per_sq_feet):
    total_area_of_land = L1*B1
    area_of_garden = L2*B2
    area_of_home = L3*B3
    remaining_area = total_area_of_land - area_of_garden - area_of_home
    total_cost_of_grass = remaining_area * cost_per_sq_feet
    return total_cost_of_grass
pre_result = grass_area(length_of_land,breadth_of_land,
                        length_of_garden,breadth_of_garden,length_of_home,breadth_of_home,grass_cost_per_sq_ft)

logger.info(f"Grass area is {pre_result}")

