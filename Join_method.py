from loguru import logger

names = ["gaurav" , "sourabh" , "Rohit"]
final_result = " "
for name in names :
    final_result = final_result + " " + name
print(final_result)

#above is the general method
final_result1 = "-".join(names)
print(final_result1)

# Join only works on string
lst_of_no = ['1','2','3','4']
result = "-".join(lst_of_no)
print(result)

labour_with_cost = {"Mahesh":500,"Ramesh":400,"Mithlesh":400,"Sumesh":300}
result = " @ ".join(labour_with_cost)
print(result)

query = """ select * from(select e.employee_name,  e.state, e.zip, e.salary, d.department, from employee_tbl
e join department d on e.emp_id = d.emp_id) a where salary>10000 
"""

state_dept_info = [{"State" : "Bihar","Department" : "IT"},{"State": "Delhi","Department" : "Marketing"}]
final_filter_condition = []
for condition in state_dept_info:
    for key,value in condition.items():
        final_filter_condition.append(f"{key} = {value}")
logger.info(final_filter_condition)
result = " OR ".join(final_filter_condition)

logger.info(query + " And " + result)

query = """ select * from(select e.employee_name,  e.state, e.zip, e.salary, d.department, from employee_tbl
e join department d on e.emp_id = d.emp_id) a where salary>10000 
"""

# Q2. Print the list of all unique ip addresses using split?

Input = ["/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.2",
"/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.156.2",
"/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2",
"/region/japan/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.22",
"/region/india/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.167.2",
"/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.179.28",
"/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.31",
"/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2"
]

new_list = []
for i in Input :
        first,last = i.split("server/")
        new_list.append(last)       
unique_ips = list(set(new_list))

print(unique_ips)