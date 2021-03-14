import pytest
from app.classes import Basket, Catalogue, BasketPricerException


def test_basket_item_cannot_have_negative_quantity():
    with pytest.raises(BasketPricerException):
        SUT = Basket([["shampoo", -1]])


def test_catalogue_cannot_have_negative_price():
    with pytest.raises(BasketPricerException):
        SUT = Catalogue([["shampoo", -0.1]])
