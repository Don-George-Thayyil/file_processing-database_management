import xml.etree.ElementTree as et

# num = 8.5
# numb = num.__trunc__()
# print(numb)

class Converter:
    def convert(self,celsius):
        #f=9/5 * c + 32
        self.farenheit = (9/5)*float(celsius) + 32
        return self.farenheit

class Xml(Converter):
    def __init__(self,name):
        tree = et.parse(name)
        self.data = tree.getroot()
        self.celsius = [celsius.text for celsius in self.data.iter("temperature_in_celsius")]
        self.farenheit = [round(self.convert(item),1) for item in self.celsius]
    def parse(self):
        for day, cel, far in zip(self.data.iter("day"), self.celsius, self.farenheit):
            print(f"{str(day.text).ljust(10)}: {str(cel).ljust(3)}Celsius or {str(far).ljust(5)}Farenheit")


weather = Xml("forecast.xml")

weather.parse()