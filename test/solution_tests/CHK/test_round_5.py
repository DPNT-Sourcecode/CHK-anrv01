from lib.solutions.CHK.checkout_solution import checkout


class Test:
    def test_group_discount_buy_3(self):
        input_skus = "XYY"
        total_value = checkout(input_skus)
        assert total_value == 45

    def test_group_discount_buy_7(self):
        input_skus = "XYYXSTS"
        total_value = checkout(input_skus)
        assert total_value == 107

    def test_group_discount_only_2_discounted(self):
        input_skus = "XAY"
        total_value = checkout(input_skus)
        assert total_value == 87

    def test_group_discount_4_all_discounted(self):
        input_skus = "SSSZ"
        total_value = checkout(input_skus)
        assert total_value == 65

    def test_group_discount_4_all_discounted(self):
        input_skus = "STXSTX"
        total_value = checkout(input_skus)
        assert total_value == 90




