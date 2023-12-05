class Mycar:
    color=None
    model=None
    engine=None
    comfort=None

    def car_Details(self):
        print("hemlo",
              self.engine,self.model)

car_color=input("enter your color ; ")
car_model=input("enter your model : ")
car_engine=input("enter your engine : ")
car_comfort=input("enter your comfort : ")

car_obj=Mycar()
car_obj.color=car_color
car_obj.model=car_model
car_obj.engine=car_engine
car_obj.comfort=car_comfort

car_obj.car_Details()
