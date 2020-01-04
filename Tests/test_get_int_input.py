from unittest import TestCase, mock


class TestGet_int_input(TestCase):
    def test_get_int_input(self):
        from user_input import get_int_input
        with mock.patch('builtins.input', side_effect=[
                    'hello', '21', '-1234', '1-1', '0', '-0', '4', '10']):
            self.assertEqual(0, get_int_input(0, 10, "pick a number between 0 and 10: "))
            self.assertEqual(0, get_int_input(0, 10, "pick a number between 0 and 10: "))
            self.assertEqual(4, get_int_input(0, 10, "pick a number between 0 and 10: "))
            self.assertEqual(10, get_int_input(0, 10, "pick a number between 0 and 10: "))

