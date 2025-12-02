# parent class
class Car:
    name = 'unknown'
    wheels = 4
    power = 'unknown'
    doors = None

    def information(self):
        msg = "\nName: {}\nWheels: {}\nPower: {}\nDoors: {}".format(self.name, self.wheels, self.power, self.doors)
        return msg


# child class instance
class Bentley(Car):
    name = 'Bentley'
    power = 'Gas'
    doors = 2
    model = '3 Litre'
    year = 1921

    def exposition(self):
        msg = "\nThis car is featured as being driven by the demon Crowley in the book 'Good Omens', written by Neil Gaiman and Terry Pratchett."
        return msg

    def information(self):
        msg = "\nName: {}\nWheels: {}\nPower: {}\nDoors: {}\nModel: {}\nYear: {}".format(self.name, self.wheels, self.power, self.doors, self.model, self.year)
        return msg

# child class instance
class Ioniq(Car):
    name = 'Ioniq'
    power = 'Electric'
    doors = 4
    safety = ['airbags', 'seatbelts', 'ABS', 'lane assist']

    def information(self):
        msg = "\nSafety features included with the Ioniq car are: {}".format(self.safety)
        return msg


if __name__ == "__main__":
    bentley = Bentley()
    print(bentley.information())
    print(bentley.exposition())

    ioniq = Ioniq()
    print(ioniq.information())
