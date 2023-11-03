class Car:
    name = None
    color = None
    model = None
    company = None
    speed = None

    def start(self):
        print("start")

    def reverse(self):
        print("reverse")

    def run(self, ):
        print("run ", self.speed)

    def stop(self):
        return "stop"

    def horn(self):
        return "horn"


tata_obj = Car()
tata_obj.name = "Nexon"
tata_obj.color = "black"
tata_obj.model = "ppx"
tata_obj.company = "tata"
tata_obj.speed = 220
tata_obj.run()
print(tata_obj.stop(), tata_obj.company)

mahindra_obj = Car()
mahindra_obj.name = "xuv"
mahindra_obj.color = "red"
mahindra_obj.model = "uvr"
mahindra_obj.company = "mahindra"
mahindra_obj.speed = 210
mahindra_obj.run()
print(mahindra_obj.stop(), mahindra_obj.company)
