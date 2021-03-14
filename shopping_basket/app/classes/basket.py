from typing import List, Dict
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


class ListOfDictBasketAdapter(Basket):
    """ This adapter allows baskets in form of List of Dicts be used in BasketPricer.
    Adapter just as an example - similar one could be used as adapter to any format, such as
    DB connectors, API connect, other format converters, etc."""

    def __init__(self, iterable: List[Dict]):
        correct_iterable = self._convert_list_of_dict_to_list_of_list(iterable)
        super().__init__(correct_iterable)

    @staticmethod
    def _convert_list_of_dict_to_list_of_list(iterable: List[Dict]):
        """ fcn converts list of dict to Basket target init format """
        return [[el["id"], el["quantity"]] for el in iterable]
