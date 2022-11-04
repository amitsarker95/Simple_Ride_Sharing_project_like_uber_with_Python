import random

class BRTA:
    def __init__(self) -> None:
        self.__licences = {}

    def take_driving_test(self, email):
        score = random.randint(0,100)
        if score >= 33:
            licenseNumber = random.randint(5000,15000)
            self.__licences[email] = licenseNumber
            # print(f"Congretulation You have been passed the test!! Your licence No. is {licenseNumber} Your Score {score}")
            return licenseNumber
        else:
            # print(f"You have failed the test!! Your Score {score}")
            return False


    def validate_license(self, email, license):
        for key, value in self.__licences.items():
            if key == email and value == license:
                return True
        return False
        