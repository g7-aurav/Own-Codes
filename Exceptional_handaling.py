from loguru import logger

#concept
a= input("Enter the number: ")
logger.info(f"Multiplication table of {a} is :")
try:
    for i in range(1,11):
        logger.info(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    logger.info(e)
    logger.info("sorry some error occured")
logger.info('Code ran')

try:
    # Code that might cause an error
    number = int(input("Enter a number: "))
    result = 10 / number
    logger.info(result)
except ZeroDivisionError:
    # Runs if you divide by zero
    logger.info("Error: Cannot divide by zero!")
except ValueError:
    # Runs if the input isn't a valid number
    logger.info("Error: Please enter a valid integer.")

def final_cart_amount(*args,discount=0.1):
    try:
        result = 0
        for amount in args:
            result= result + amount
        logger.info(result)
        amount_after_discount = result - (result*discount)

        return amount_after_discount
    except NameError:
        logger.info("variable is not found")
        raise Exception("please check the variable name")
    except TypeError:
        logger.info('please provide amount in integer')
        raise Exception ('value provided is not an integer coming from type error') 
    except Exception as e:
        logger.info('cannot process the cart amount')
        # raise e
try:        
    final_amount_tobe_paid = final_cart_amount(100,500,100,300,500,discount = 0.5)
    logger.info(final_amount_tobe_paid)
except Exception as e:
    logger.info(e)
logger.info('Job ran successfuly')