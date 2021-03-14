import pytest
from app.classes import Basket, Catalogue, BasketPricerException, ListOfDictBasketAdapter, BasketPricer, Offers


def test_basket_item_cannot_have_negative_quantity():
    with pytest.raises(BasketPricerException):
        SUT = Basket([["shampoo", -1]])


def test_catalogue_cannot_have_negative_price():
    with pytest.raises(BasketPricerException):
        SUT = Catalogue([["shampoo", -0.1]])


def test_basket_adapters_work_with_basket_pricer():
    example_basket_input_data = [{"id": "shampoo", "quantity": 3}, {"id": "milk", "quantity": 14}]
    basket_adapter = ListOfDictBasketAdapter(example_basket_input_data)
    empty_catalogue = Catalogue([])
    empty_offers = Offers([])

    # basket pricer can be crated with adapter
    SUT = BasketPricer(basket_adapter, empty_catalogue, empty_offers)
