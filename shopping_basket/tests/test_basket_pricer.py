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


@pytest.mark.parametrize(
    "number_of_items, x, y, expected_discounted_products",
    [(2, 2, 2, 0), (4, 2, 2, 2), (3, 2, 2, 1), (8, 2, 2, 4), (11, 2, 2, 5)],
)
def test_buy_x_get_y_free_discount(number_of_items, x, y, expected_discounted_products):
    price = 1.0
    basket = Basket([["shampoo", number_of_items]])
    catalogue = Catalogue([["shampoo", price]])
    offers = Offers([["shampoo", "buy_x_get_y_free", {"buy": x, "free": y}]])

    SUT = BasketPricer(basket=basket, catalogue=catalogue, offers=offers)

    expected_discount = expected_discounted_products * price
    assert SUT.discount == expected_discount


@pytest.mark.parametrize("x, y", [(0, 1), (1, 0), (-1, 1), (1, -1)])
def test_buy_x_get_y_free_exceptions(x, y):
    price = 1.0
    basket = Basket([["shampoo", 1]])
    catalogue = Catalogue([["shampoo", price]])
    offers = Offers([["shampoo", "buy_x_get_y_free", {"buy": x, "free": y}]])

    SUT = BasketPricer(basket=basket, catalogue=catalogue, offers=offers)

    with pytest.raises(BasketPricerException):
        SUT.discount


@pytest.mark.parametrize(
    "number_of_items, x, y, expected_discounted_products",
    [(2, 4, 2, 0), (3, 4, 2, 0), (4, 4, 2, 2), (8, 4, 2, 4), (11, 4, 2, 4)],
)
def test_buy_x_for_price_of_y_discount(number_of_items, x, y, expected_discounted_products):
    price = 1.0
    basket = Basket([["shampoo", number_of_items]])
    catalogue = Catalogue([["shampoo", price]])
    offers = Offers([["shampoo", "buy_x_for_price_of_y", {"buy": x, "price_of": y}]])

    SUT = BasketPricer(basket=basket, catalogue=catalogue, offers=offers)

    expected_discount = expected_discounted_products * price
    assert SUT.discount == expected_discount


@pytest.mark.parametrize("x, y", [(0, 1), (1, 0), (-1, 1), (1, -1), (2, 2), (2, 3)])
def test_buy_x_for_price_of_y_exceptions(x, y):
    price = 1.0
    basket = Basket([["shampoo", 1]])
    catalogue = Catalogue([["shampoo", price]])
    offers = Offers([["shampoo", "buy_x_for_price_of_y", {"buy": x, "price_of": y}]])

    SUT = BasketPricer(basket=basket, catalogue=catalogue, offers=offers)

    with pytest.raises(BasketPricerException):
        SUT.discount


def test_multiple_offers_on_the_same_items_are_all_applied():
    """ discount is counted for all offers without any additional logic """
    basket = Basket([["shampoo", 2]])
    catalogue = Catalogue([["shampoo", 1.0]])
    offers = Offers([["shampoo", "percent", 50], ["shampoo", "buy_x_get_y_free", {"buy": 1, "free": 1}]])

    SUT = BasketPricer(basket=basket, catalogue=catalogue, offers=offers)

    assert SUT.discount == 2.0
