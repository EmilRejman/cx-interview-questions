import pytest
from app.classes import Basket, BasketPricer, Catalogue, Offers, BasketPricerException


def test_basket_with_zero_products_returns_only_zeros():
    empty_basket = Basket([])
    empty_catalogue = Catalogue([])
    empty_offers = Offers([])

    SUT = BasketPricer(basket=empty_basket, catalogue=empty_catalogue, offers=empty_offers)

    assert SUT.total == 0.0
    assert SUT.sub_total == 0.0
    assert SUT.discount == 0.0


def test_offers_on_items_which_are_not_in_catalogue_are_not_applicable():
    basket = Basket([["shampoo", 1]])
    catalogue = Catalogue([["shampoo", 1.0]])
    offers = Offers([["ham", "percent", 50]])

    SUT = BasketPricer(basket=basket, catalogue=catalogue, offers=offers)

    assert SUT.discount == 0.0


@pytest.mark.parametrize("number_of_items", [1, 2, 10])
def test_percent_discount(number_of_items):
    price = 1.0
    discount = 50.0
    basket = Basket([["shampoo", number_of_items]])
    catalogue = Catalogue([["shampoo", price]])
    offers = Offers([["shampoo", "percent", discount]])

    SUT = BasketPricer(basket=basket, catalogue=catalogue, offers=offers)

    assert SUT.discount == number_of_items * price * discount / 100

def test_percent_discount_multiple_times_total_price_cant_be_lower_than_zero():
    price = 1.0
    basket = Basket([["shampoo", 1]])
    catalogue = Catalogue([["shampoo", price]])
    offers = Offers([["shampoo", "percent", 50], ["shampoo", "percent", 50], ["shampoo", "percent", 50]])

    SUT = BasketPricer(basket=basket, catalogue=catalogue, offers=offers)

    assert SUT.total == 0.0
