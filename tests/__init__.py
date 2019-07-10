from unittest import TestCase
from service_app.app import app


class BaseTestCase(TestCase):

    def setUp(self):
        self.app = app.test_client()
