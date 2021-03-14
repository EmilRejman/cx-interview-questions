from app.classes.basket import Basket
from app.classes.catalogue import Catalogue
from app.classes.offers import Offers


class BasketPricer:
    def __init__(self, basket: Basket, catalogue: Catalogue, offers: Offers):
        self.basket = basket
        self.catalogue = catalogue
        self.offers = offers
