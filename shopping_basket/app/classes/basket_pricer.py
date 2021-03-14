from app.classes.basket import Basket
from app.classes.catalogue import Catalogue


class BasketPricer:
    def __init__(self, basket: Basket, catalogue: Catalogue):
        self.basket = basket
        self.catalogue = catalogue
