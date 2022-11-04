from abc import ABC, abstractclassmethod, abstractmethod

from pyautogui import sleep

class Vehicles(ABC):
    speed = {
        'car' : 80,'bike' : 60,'cng' : 40
    }
    def __init__(self,vehicle_type, licence_number, driver, rate) -> None:
        self.vehicle_type = vehicle_type
        self.driver = driver
        self.rate = rate
        self.status = 'available'
        self.licence_number = licence_number
        self.speed = self.speed[vehicle_type]
    @abstractmethod
    def start_driving(self):
        pass
    @abstractmethod
    def trip_finish(self):
        pass

class Car(Vehicles):
    def __init__(self, vehicle_type, licence_number, driver, rate) -> None:
        super().__init__(vehicle_type, licence_number, driver, rate)
    
    def start_driving(self,start,destination):
        self.status = 'unavailable'
        print(f"{self.vehicle_type} Start Trip\n")
        distance = abs(start - destination)
        for i in range(0, distance):
            sleep(0.5)
            print(f'Driving {self.licence_number} current position {i} of {distance}\n')
        self.trip_finish()
        return super().start_driving()
        

    def trip_finish(self):
        self.status = 'available'
        print(f"{self.vehicle_type} Trip finished.")
        return super().trip_finish()

class Bike(Vehicles):
    def __init__(self, vehicle_type, licence_number, driver, rate) -> None:
        super().__init__(vehicle_type, licence_number, driver, rate)
    
    def start_driving(self,start,destination):
        self.status = 'unavailable'
        print(f"{self.vehicle_type} Trip start\n")
        distance = abs(start - destination)
        for i in range(0, distance):
            sleep(0.3)
            print(f'Driving {self.licence_number} current position {i} of {distance}\n')
        self.trip_finish()
        return super().start_driving()

    def trip_finish(self):
        self.status = 'available'
        print(f"{self.vehicle_type} Trip finish\n")
        return super().trip_finish()

class Cng(Vehicles):
    def __init__(self, vehicle_type, licence_number, driver, rate) -> None:
        super().__init__(vehicle_type, licence_number, driver, rate)
    
    def start_driving(self,start,destination):
        self.status = 'unavailable'
        print(f"{self.vehicle_type} Trip start\n")
        distance = abs(start - destination)
        for i in range(0, distance):
            sleep(0.3)
            print(f'Driving {self.licence_number} current position {i} of {distance}\n')
        self.trip_finish()
        return super().start_driving()

    def trip_finish(self):
        self.status = 'available'
        print(f"{self.vehicle_type} Trip finish\n")
        return super().trip_finish()
