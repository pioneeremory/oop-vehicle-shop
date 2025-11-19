class CarManager:

    all_cars = []
    total_cars: 0

    def __init__(self, _id, _make, _model, _year, _mileage, _services):
        self._id = _id
        self._make = _make
        self._model = _model
        self._year = _year
        self._mileage = _mileage
        self._services = _services

    def terminal_ui(self):
        print("""
        ----  WELCOME  ----
        1. Add a car
        2. View all cars
        3. View total number of cars
        4. See a car's details
        5. Service a car
        6. Update mileage
        7. Quit""")

        menu_items = {
            "1": self.add_car,
            "2": self.view_car,
            "3": self.view_car_num,
            "4": self.car_detail,
            "5": self.service_car,
            "6": self.update_mileage,
            "7": self.quit_program
        }
      
    def add_car(self):
        self._id = input('Welcome to the Add Car wizard. Please enter the vehicle ID: ')
        self._make = input('What is the make of the car?: ')
        self._model = input('What is the model of the car?: ')
        self._year = input('What is the year of the car?: ')
        self._mileage = input('How many miles does the car have?: ')
        self._services = input('Were any services performed?: ')

        CarManager.all_cars.append(self)
        total_cars += 1
    
    def view_car(self):
        print(f"Here's a list of all the cars in the garage: \n {self.all.cars}")

    def view_car_num(self):
        print(f"There are currently {self.total_cars} in the garage.")
    
    def car_detail(self, id):
        self.id = id
        for i in self.all_cars.items():
            if i["ID"] == id:
                print(f"Here are the details for car with the ID of {id}: {i}")
                #for key, value in self.all_cars:
    def service_car(self, id):
        self.id = id
        return True

    def update_mileage(self, id):
        self.id = id
        return True
    def quit_program(self):
        return True
    

car1 = CarManager("s", "2", "3", "3", "four", "44", "Timmy")



