from user_ratings import UserRatings
from maleclothing import MaleClothing
from femaleclothing import FemaleClothing
from unisex import UniSex


class MainClass:

    product = []
    rating = []
    product1 = MaleClothing("Pant", "Allen-Solly", 2000)
    product1.deliveryTime = 2
    product1.discountPercentage = 10.0
    product1.set_dimensions(dimensions='s')
    product1.set_clothing_type("Shirt")
    product.append(product1)

    product2 = FemaleClothing("Skirt", "Allen", 3000)
    product2.deliveryTime = 10
    product2.discountPercentage = 12.3
    product2.set_dimensions(dimensions='m')
    product2.set_clothing_type("Skirt")
    product.append(product2)

    product3 = UniSex("sweater", "Roadstar", 5000)
    product3.deliveryTime = 15
    product3.discountPercentage = 2.0
    product3.set_dimensions(dimensions='l')
    product3.set_clothing_type("sweater")
    product.append(product3)

    userRating1 = UserRatings(product1.id, "It's Bad")
    rating.append(userRating1)

    print(product)
    print(rating)