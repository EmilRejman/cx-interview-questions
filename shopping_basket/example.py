from app import BasketPricer, Basket, Catalogue, Offers

if __name__ == "__main__":
    import sys
    from os.path import dirname, abspath

    sys.path.insert(0, dirname(dirname(abspath(__file__))))

    example_basket = [["shampoo", 1], ["milk", 2], ["bread", 2]]
    example_catalogue = [["shampoo", 2.0], ["milk", 4.0], ["bread", 2.0]]
    example_offers = [["shampoo", "percent", 25], ["milk", "buy_x_get_y_free", {"buy": 2, "free": 2}],
                      ["bread", "buy_x_for_price_of_y", {"buy": 5, "price_of": 3}]]
    pricer = BasketPricer(Basket(example_basket), Catalogue(example_catalogue), Offers(example_offers))
    print(pricer.basket)
    print(pricer.catalogue)
    print(pricer.offers)

    print("sub_total price:", pricer.sub_total)
    print("total discount:", pricer.discount)
    print("total price:", pricer.total)
