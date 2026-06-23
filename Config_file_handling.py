from loguru import logger
import configparser

config = configparser.ConfigParser()

config.read(r"D:\GAURAV\My Learnings\Spark Tutorials Youtube\Python Files\config_file.ini")

# brick_cost = config["raw_materials"]["brick_cost"]

# logger.info(f"{brick_cost}, type of brick is {type(brick_cost)}")

# def total_no_of_bricks(length, breadth, height):
#     # Perimeter of house
#     perimeter = 2 * (length + breadth)
#     wall_area = perimeter * height
    
#     # Brick dimensions (height is half of length)
#     brick_length = 1
#     brick_height = 0.5
    
#     # Brick face area
#     brick_area = brick_length * brick_height
    
#     # Total bricks using real formula
#     total_bricks = wall_area / brick_area
#     return total_bricks


# def total_cost_for_bricks(config):
#     brick_cost = float(config["raw_materials"]["brick_cost"])
    
#     total_bricks = total_no_of_bricks(15, 15, 10)
#     logger.info(total_bricks)
#     final_cost = brick_cost * total_bricks
#     return final_cost


# result = total_cost_for_bricks(config)
# logger.info(f"Total bricks cost to make 1 room {result}")


book_cost = config["book_cost"]["physics"]
logger.info(f"{book_cost}, type of book is {type(book_cost)}")

student_details = {1:["math","history"],
                   2:["biology","chemistry","history"],
                   3:["science"]
                   }


for student, books in student_details.items():
    total_cost = 0
    for book in books:
        price = int(config["book_cost"][book])
        total_cost = total_cost + price

    if len(student_details[student]) >2:
        total_cost = total_cost * 0.9
    else:
        total_cost
    logger.info(f"Student {student} total book cost = {total_cost}")