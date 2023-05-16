from base_product import BaseProduct
from size_chart import SizeChart


class MaleClothing(BaseProduct):

    def __init__(self, clothing_name, brand, mrp):
        super().__init__(clothing_name=clothing_name, brand=brand, mrp=mrp)
        pass

    def set_dimensions(self, dimensions):
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
        if clothing_type == 'pant':
            super.clothing_type = clothing_type
        elif clothing_type == 'shirt':
            super.clothing_type = clothing_type
        elif clothing_type == 'kurtha':
            super.clothing_type = clothing_type
        else:
            Exception("Invalid Dress Type")