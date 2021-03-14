from typing import List


class Discount:
    def __init__(self, product_id: str, type: str, discount_data: object):
        self.product_id = product_id
        self.type = type  # str just for visibility for this result. Use id or get data from single_table_inheritance discount table or sth else
        self.discount_data = discount_data
        # add other needed data in future, like `connects_with_other_discounts` etc etc.

    def __str__(self):
        return f"item id: {self.product_id}, type: {self.type}, discount: {self.discount_data}"


class Offers:
    def __init__(self, iterable: List[List]):
        self.offers_list = [Discount(product_id=el[0], type=el[1], discount_data=el[2]) for el in iterable]

    def __iter__(self):
        return iter(self.offers_list)

    def __str__(self):
        return f"Product discounts: {[str(discount) for discount in self.offers_list]}"
