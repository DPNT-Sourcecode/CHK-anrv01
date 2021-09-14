from lib.solutions.CHK.checkout_solution import checkout


class Test:
    def test_read_functionality(self):
        input_skus = "ABCDADC"
        total_value = checkout(input_skus)
        assert total_value == 200

    def test_bad_input(self):
        input_skus = 400
        total_value = checkout(input_skus)
        assert total_value == -1

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


