from app.classes.basket import Basket
from app.classes.catalogue import Catalogue
from app.classes.offers import Offers
from app.classes.common import BasketPricerException


class BasketPricer:
    def __init__(self, basket: Basket, catalogue: Catalogue, offers: Offers):
        self.basket = basket
        self.catalogue = catalogue
        self.offers = offers

    @property
    def sub_total(self):
        sub_total_price = 0.0
        for product_and_quantity in self.basket:
            product_price = self._get_product_price(product_and_quantity.id)
            sub_total_price += product_and_quantity.quantity * product_price
        return sub_total_price

    @property
    def discount(self):
        total_discount = 0.0
        for product_and_quantity in self.basket:
            item_discounts = [discount for discount in self.offers if discount.product_id == product_and_quantity.id]
            product_price = self._get_product_price(product_and_quantity.id)
            for discount in item_discounts:
                total_discount += self._count_discount(discount.type, product_and_quantity, product_price, discount)

        return total_discount

    @property
    def total(self):
        total = self.sub_total - self.discount
        total = 0 if total < 0 else total

        return total

    def _get_product_price(self, product_id):
        product_price = next(
            (product_price.price for product_price in self.catalogue if product_price.id == product_id),
            None)

        if product_price is None:
            raise BasketPricerException(f"The item form bucket {product_id} is not existing in catalouge!")

        return product_price

    def _count_discount(self, discount_type: str, *args):
        """ some additional logic should probably be added in counting discounts, although I believe it is not the
        point of this task, so I left counting multiple offers in the simplest way (without looking at other
        discounts """
        discount_types = {
            "percent": self._count_discount_percent,
            "buy_x_get_y_free": self._count_discount_buy_x_get_y_free
        }

        return discount_types[discount_type](*args)

    @staticmethod
    def _count_discount_percent(product_and_quantity, product_price, discount):
        return product_and_quantity.quantity * product_price * discount.discount_data / 100.0

    @staticmethod
    def _count_discount_buy_x_get_y_free(product_and_quantity, product_price, discount):
        if discount.discount_data["buy"] <= 0 or discount.discount_data["free"] <= 0:
            raise BasketPricerException(f"Discount has incorrect data: {discount}")
        total_discount = 0.0
        buy_plus_free = discount.discount_data["buy"] + discount.discount_data["free"]
        full_discounts, remaining_products_quantity = divmod(product_and_quantity.quantity,
                                                             buy_plus_free)
        # get discount value form full_discounts
        total_discount += full_discounts * discount.discount_data["free"] * product_price

        # get discount from remaining products if applicable
        remaining_discount_quantity = remaining_products_quantity - discount.discount_data["buy"]
        if remaining_discount_quantity > 0:
            total_discount += remaining_discount_quantity * product_price

        return total_discount
