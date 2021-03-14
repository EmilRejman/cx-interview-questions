from typing import List
from app.classes.common import BasketPricerException


class ProductQuantity:
    def __init__(self, product_id: str, quantity: int):
        self.id = product_id
        self.quantity = quantity
        # add category or other attribute needed in the future

    def __str__(self):
        return f"id: {self.id}, quantity: {self.quantity}"


class Basket:
    def __init__(self, iterable: List[List]):
        self.product_list = [ProductQuantity(product_id=el[0], quantity=el[1]) for el in iterable]
        # we could add e.g. basket_currency here, so user can pick his currency and catalog prices in different
        # currencies may be calculated.

    def __iter__(self):
        return iter(self.product_list)

    @property
    def product_list(self):
        return self.__product_list

    @product_list.setter
    def product_list(self, iterable: List[ProductQuantity]):
        self._check_if_input_product_list_has_no_negative_quantity(iterable)
        self.__product_list = iterable

    @staticmethod
    def _check_if_input_product_list_has_no_negative_quantity(iterable: List[ProductQuantity]):
        for el in iterable:
            if el.quantity < 0:
                raise BasketPricerException(f"Quantity of item {el.id} is negative.")

    def __str__(self):
        return f"Basket products: {[str(product) for product in self.product_list]}"
