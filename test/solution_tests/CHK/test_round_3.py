from lib.solutions.CHK.checkout_solution import checkout


class Test:
    def test_2_discounts_applied(self):
        input_skus = "FFFFFF"
        total_value = checkout(input_skus)
        assert total_value == 40

    def test_1_discount_applied(self):
        input_skus = "FFFFF"
        total_value = checkout(input_skus)
        assert total_value == 40
