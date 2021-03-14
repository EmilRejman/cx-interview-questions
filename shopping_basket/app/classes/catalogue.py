from typing import List
from app.classes.common import BasketPricerException


class ProductPrice:
    def __init__(self, product_id: str, price: float):
        self.id = product_id
        self.price = price
        # add `unit` or other needed attribute in future

    def __str__(self):
        return f"id: {self.id}, price: {format(self.price, '.2f')}"


class Catalogue:
    def __init__(self, iterable: List[List]):
        self.product_list = [ProductPrice(product_id=el[0], price=el[1]) for el in iterable]

    def __iter__(self):
        return iter(self.product_list)

    @property
    def product_list(self):
        return self.__product_list

    @product_list.setter
    def product_list(self, iterable: List[ProductPrice]):
        self._check_if_input_product_list_has_no_negative_prices(iterable)
        self.__product_list = iterable

    @staticmethod
    def _check_if_input_product_list_has_no_negative_prices(iterable: List[ProductPrice]):
        for el in iterable:
            if el.price < 0:
                raise BasketPricerException(f"Price of item {el.id} is negative.")

    def __str__(self):
        return f"Catalogue products: {[str(product) for product in self.product_list]}"
