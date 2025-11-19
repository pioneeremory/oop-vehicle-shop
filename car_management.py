class CarManager:

    all_cars = {}
    total_cars = 0

    def __init__(self, _id, _make, _model, _year, _mileage, _services):
        self._id = _id
        self._make = _make
        self._model = _model
        self._year = _year
        self._mileage = _mileage
        self._services = _services
        

    def __str__(self):
        return f'printing the {self._id}, {self._make}'

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

        user_choice = int(input("What would you like to do? (Enter a number 1-7): "))
        if user_choice == 1:
            CarManager.add_car(self)
        elif user_choice == 2:
            CarManager.view_car(self)
        elif user_choice == 3:
            CarManager.view_car_num(self)
        elif user_choice == 4:
            CarManager.car_detail(self)
        elif user_choice == 5:
            CarManager.service_car(self)
        elif user_choice == 6:
            CarManager.update_mileage(self)
        else:
            print("See you next time!")
            CarManager.quit_program(self)
        
    def add_car(self):
        #need to make id unique and increment by 1 based on other entries in all_cars
        if len(CarManager.all_cars) > 0:
            new_id = len(CarManager.all_cars) +1
        else:
            new_id = 1
        make = input('What is the make of the car?: ')
        model = input('What is the model of the car?: ')
        year = input('What is the year of the car?: ')
        mileage = input('How many miles does the car have?: ')
        services = input('Were any services performed?: ')

        new_car = CarManager(new_id, make, model, year, mileage, services)

        CarManager.all_cars[new_id] = new_car
        CarManager.total_cars += 1
        print(CarManager.all_cars[new_id])

        decision = input("Type back to return to the menu, otherwise, type exit: ")
        if decision == "back":
            CarManager.terminal_ui(self)
        else:
            CarManager.quit_program(self)
    
    def view_car(self):
        # print(f"Here's a list of all the cars in the garage: \n {CarManager.all_cars[self.new_id]}")
        for car_id, car in CarManager.all_cars.items():
            print(f"ID {car_id}: {car._make} {car._model} ({car._year})")
        decision = input("Type back to return to the menu, otherwise, type exit: ")
        if decision == "back":
            CarManager.terminal_ui(self)
        else:
            CarManager.quit_program(self)

    def view_car_num(self):
        print(f"There are currently {CarManager.total_cars} in the garage.")
    
    def car_detail(self, id):
        self.id = id
        for i in CarManager.all_cars.items():
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
    

car1 = CarManager("s", "2", "3", "3", "four", "44")
CarManager.terminal_ui(car1)





