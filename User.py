import hashlib
import random
import threading
from Licence import BRTA
from vehicles import *
from ride_manager import uber

licence_authority = BRTA()

class UserAlreadyExist(Exception):
    def __init__(self, email, *args: object) -> None:
        print(f'{email}This User already exist')
        super().__init__(*args)
    

class User:
    def __init__(self,name,email,password,) -> None:
        self.name = name
        self.email = email
        self.pass_encrypted = hashlib.md5(password.encode()).hexdigest()
        with open('User.txt', 'r') as file:
            if email in file.read():
                pass
                # raise UserAlreadyExist(email)
        file.close()

        with open('User.txt','a') as file:
            file.write(f"{email} {self.pass_encrypted}\n")
        file.close()
        # print(f"{self.name}, User created")
        
    @staticmethod
    def log_in(email, password):
        with open("user.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                db_email, db_pass = line.split(" ")
        file.close()
        password = hashlib.md5(password.encode()).hexdigest()
        if email == db_email and password == db_pass:
            print("User Logged in Successfully")
        else:
            print("User not Logged in.")


class Rider(User):
    def __init__(self, name, email, password, location, balance) -> None:
        self.location = location
        self.balance = balance
        self.__trip_history = []
        super().__init__(name, email, password)

    def set_location(self,location):
        self.location = location

    def get_location(self):
        return self.location
    
    def start_a_trip(self, fare,trip_info):
        self.__trip_history.append(trip_info)
        self.balance -= fare

    def get_trip_history(self):
        return self.__trip_history

class Driver(User):
    def __init__(self, name, email, password, location, licence) -> None:
        super().__init__(name, email, password)
        self.location = location
        self.licence = licence
        self.valid_driver = licence_authority.validate_license(email, licence)
        self.earning = 0
        self.__trip_history = []
        self.vehicle = None
        

    def take_driving_test(self):
        result = licence_authority.take_driving_test(self.email)
        if result == False:
            self.licence = None
            # print(f"Sorry {self.name} You have failed!!")
        else:
            self.licence = result
            self.valid_driver = True
            # print(f"Congratulation {self.name} You have Passed!!")

    def registar_a_vehicle(self, vehicle_type, licence_number, rate):
        if self.valid_driver is True:
            if vehicle_type == 'car':
                self.vehicle = Car(vehicle_type,licence_number,self,rate)
                uber.add_a_vehicle(vehicle_type,self.vehicle)
            elif vehicle_type == 'bike':
                self.vehicle = Bike(vehicle_type,licence_number,self,rate)
                uber.add_a_vehicle(vehicle_type,self.vehicle)
            elif vehicle_type == 'cng':
                self.vehicle = Cng(vehicle_type,licence_number,self,rate)
                uber.add_a_vehicle(vehicle_type,self.vehicle)
        else:
            pass
            # print("You are not a valid driver!!")
    def start_a_trip(self,start, destination, fare, trip_info):
        self.earning += fare
        self.location = destination
        self.__trip_history.append(trip_info)
        # self.vehicle.start_driving(start,destination)
        trip_thread = threading.Thread(target=self.vehicle.start_driving,args=(start,destination,))
        trip_thread.start()

    def get_trip_history(self):
        return self.__trip_history



# user = User('Amit',"amitsarker95@gmail.com","123")
# user.log_in(user.email,'123')


rider1 = Rider("Foysal","foysal@gamil.com","rider1",random.randint(0,100),10000)
rider2 = Rider("Lord","Lord@gamil.com","rider2",random.randint(0,100),1100)
rider3 = Rider("Ark","ark@gamil.com","rider3",random.randint(0,100),11000)

vehicle_types = ['car','bike','cng']

for i in range(1, 40):
    driver1 = Driver(f"Rahim{i}",f"Rahim{i}@gmail.com",f"1122{i}", random.randint(1,100), random.randint(10000,99999))
    driver1.take_driving_test()
    driver1.registar_a_vehicle(random.choice(vehicle_types), random.randint(100, 1000), 10)

# cars=uber.get_available_cars()
# print(cars)
uber.find_a_vehicle(rider1, random.choice(vehicle_types), 40)
uber.find_a_vehicle(rider2, random.choice(vehicle_types), 66)
uber.find_a_vehicle(rider3, random.choice(vehicle_types), 90)
print(rider1.get_trip_history())


