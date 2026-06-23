from loguru import logger
labour_name = ['Mahesh','Ramesh','Mithlesh','Sumesh']
import time

name_iter = 0
while(name_iter<len(labour_name)):
    print(labour_name[name_iter])
    time.sleep(4)
    name_iter+=1