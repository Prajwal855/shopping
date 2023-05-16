import random
from dimensions import Dimensions
from size_chart import SizeChart


class BaseProduct:
    id = int
    discount: float
    delivery_time: int
    dimensions: Dimensions
    size_chart: SizeChart
    clothing_type: str
    material_type: str

    def __init__(self, clothing_name: str, brand: str, mrp: float):
        self.id = random.randint(1000, 9000)
        self.clothing_name = clothing_name
        self.brand = brand
        self.mrp = mrp

    def set_dimensions(self, dimensions):
        self.dimensions = dimensions
        if dimensions.lower() == 's':
            self.size_chart = SizeChart(36, 33, 35, 31, 5, 120)
        elif dimensions.lower() == 'm':
            self.size_chart = SizeChart(38, 33, 37, 31, 6, 130)
        elif dimensions.lower() == 'l':
            self.size_chart = SizeChart(40, 35, 38, 32, 7, 155)
        elif dimensions.lower() == 'xl':
            self.size_chart = SizeChart(42, 39, 42, 34, 8, 175)
        elif dimensions.lower() == 'xxl':
            self.size_chart = SizeChart(45, 41, 44, 35, 6, 195)

    def set_clothing_type(self, clothing_type):
        if clothing_type == 't-shirt':
            self.clothing_type = clothing_type
        elif clothing_type == 'sweatshirt':
            self.clothing_type = clothing_type
        else:
            Exception("Invalid Dress Type")

    def __str__(self):
        return self.brand, self.dimensions, self.id, self.mrp, self.clothing_type, self.clothing_name, self.discount, \
            self.size_chart, self.delivery_time
