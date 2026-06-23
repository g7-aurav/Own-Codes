from loguru import logger
class user:
    def __init__(self,ip,phone_details,location):
        self.ip = ip
        self.phone_details = phone_details
        self.location = location

        def signup(self):
            pass

        def login(self):
            pass

        def profile_update(self):
            pass


user1 = user("10.123.1.10","samsung/android","delhi")
logger.info(user1)
logger.info(user1.__dict__)
logger.info(dir(user1))
# user2 = user("10.123.1.12","iphone 16/ios","jaipur")
# print(user2)