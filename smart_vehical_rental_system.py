class vehicle:
    def __init__(self, vehicle_id,brand, model, rent_per_day, rental_status):
        self.vehicle_id=vehicle_id
        self.brand=brand
        self.model=model
        self.rent_per_day=rent_per_day
        self.__rental_status=rental_status
    def get_rental_status(self):
        return self.__rental_status
    def calculate_rent(self,days):
        return self.rent_per_day*days
    def display_info(self):
        print(f"ID:{self.vehicle_id}")
        print(f"brand:{self.brand}")
        print(f"Model:{self.model}")
        print(f"rent:{self.rent_per_day}")
        print(f"rent status:{self.get_rental_status()}")

        
class car(vehicle):
    def __init__(self,vehicle_id,brand,model,rent_per_day,rental_status, number_of_doors):
        super().__init__(vehicle_id,brand,model,rent_per_day,rental_status)
        self.number_of_doors=number_of_doors
    def calculate_rent(self,days):
        return self.rent_per_day*days
    def display_info(self):
        super().display_info()
        print(f"doors:{self.number_of_doors}")
class bike(vehicle):
    def __init__(self, vehicle_id, brand, model, rent_per_day, rental_status,engine_cc):
        super().__init__(vehicle_id,brand,model,rent_per_day, rental_status)
        self.engine_cc=engine_cc
    def calculate_rent(self, days):
        return self.rent_per_day*days
    def display_info(self):
        super().display_info()
        print(f"engine cc:{self.engine_cc}")
c1= car(101,"BMW","luxury",7000,"yes",4)
c2=car(102,"Ford","family",4000,"no",4)
b1=bike(101,"Kawasaki","ss",7000,"yes",1000)
b2=bike(102,"harley","davidson",15000,"yes",700)
c1.display_info()
c2.display_info()
b1.display_info()
b2.display_info()


        

    



