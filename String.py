from loguru import logger
name = "Gaurav Trivedi"

# for character in name:
#     logger.info(character)
# logger.info(name[:2])

counter = 0
for character in name:
    logger.info(f"{counter}, {character}")
    counter += 1
# OR
for character in name:
    print(counter,character)
    counter+=1
print(name.count('a'))

print(ord('a'))
print(ord('A'))
print(ord('z'))
print(ord('Z'))

print(name.islower())
print(name.upper())

new_name = name.replace("Gaurav Trivedi","Sourabh Trivedi")
print(new_name)
name = "Gaurav Trivedi        "
print(len(name))
print(name.strip())
print(len(name.strip()))

print(name.swapcase())

name =  "Gaurav sourabh rohan ram"
new_name = name.split(" ")
print(new_name)

lst = []
for N in new_name:
    if N.endswith("v"):
        lst.append(N)
        print(f"{N} ends with v")
    else:
        print(f"{N} does not end with v")
print(lst)

# Q. convert below list into ** format keep first and last alphabets/number only before @ and put it in new list
Email = ["trivedi.gaurav936@gmail.com","trivedi.gaurav1111@gmail.com","g.trivedi@telushealth.com","gaurav.t@telus.com"] 
new_list = []

for e in Email:
    username, domain = e.split("@")   # split into username and domain
    print(username,domain)
    if len(username) > 2:
        masked = username[0] + "*"*(len(username)-2) + username[-1]
    else:
        masked = username  # if username is too short, keep as is
    new_list.append(masked + "@" + domain)

print(new_list)