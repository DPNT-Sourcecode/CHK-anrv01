from lib.solutions.CHK.checkout_solution import checkout


class Test:
    def test_special_offer(self):
        input_skus = "AABAB"
        total_value = checkout(input_skus)
        assert total_value == 175

    def test_get_one_free(self):
        input_skus = "EBEEE"
        total_value = checkout(input_skus)
        assert total_value == 160

    def test_get_3_free(self):
        input_skus = "EEBEEBEEB"
        total_value = checkout(input_skus)
        assert total_value == 240

    def test_5_a(self):
        input_skus = "AAAAA"
        total_value = checkout(input_skus)
        assert total_value == 200