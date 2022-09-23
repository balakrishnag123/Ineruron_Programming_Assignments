class car:
    def __init__(self, body, engine, tyre):
        self.body = body
        self.engine = engine
        self.tyre = tyre

    def millage(self):
        print("millage of this car is ")

class tata(car):
    pass


t = tata("sedan","A500","flat")

print(t.millage())
