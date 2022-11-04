class RideManager:
    def __init__(self):
        self.__income = 0
        self.__trip_history = []
        self.__availableCars = []
        self.__availableBikes = []
        self.__availableCngs = []

    def add_a_vehicle(self,vehicles_type, vehicle):
        if vehicles_type == 'car':
            self.__availableCars.append(vehicle)
        elif vehicles_type == 'bike':
            self.__availableBikes.append(vehicle)
        elif vehicles_type == 'cng':
            self.__availableCngs.append(vehicle)

    def get_available_cars(self):
        return self.__availableCars
    
    def total_income(self):
        return self.__income

    def trip_history(self):
        return self.__trip_history

    def find_a_vehicle(self,rider,vechicle_type,destination):
        if vechicle_type == 'car':
            vechicles = self.__availableCars
        elif vechicle_type == 'bike':
            vechicles = self.__availableBikes
        else:
            vechicles = self.__availableCars
        if len(vechicles) == 0:
            print('No car available right now..')
            return False
        for vehicle in vechicles:
            # print('Potential',rider.location, vehicle.driver.location)
            if abs(rider.location - vehicle.driver.location) <= 10:
                distance = abs(rider.location - destination)
                fare = distance * vehicle.rate
                if rider.balance < fare:
                    print("Insurficient balance..",rider.balance)
                    return False
                if vehicle.status == 'available':
                    vechicles.remove(vehicle)
                    trip_info = f'Match {vechicle_type} for {rider.name} fare {fare} with {vehicle.driver.name} started from : {rider.location} to {destination}..'
                    print(trip_info)
                    rider.start_a_trip(fare,trip_info)
                    self.__income += fare*0.2
                    vehicle.driver.start_a_trip(rider.location,destination,fare*0.8,trip_info)
                    self.__trip_history.append(trip_info)
                    return True
        

uber = RideManager()