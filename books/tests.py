from django.test import TestCase

import books.rest as rest


class BookTestCase(TestCase):

    def test_page_num(self):
        num1 = rest.get_page_num('aaa')
        num2 = rest.get_page_num(6)
        num3 = rest.get_page_num(None)
        self.assertFalse(num1)
        self.assertEqual(num2, 6)
        self.assertEqual(num3, 1)
