from django.test import TestCase,Client
import unittest


class test(unittest.TestCase):
    def test_home(self):
        response=self.client.get('/learn/home/')
        self.assertEqual(response.status_code,200)
