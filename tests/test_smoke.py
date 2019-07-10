from http import HTTPStatus

from tests import BaseTestCase


class SmokeTest(BaseTestCase):

    def test_get_smoke(self):
        response = self.app.get('/')

        self.assertEqual(HTTPStatus.OK, response.status_code)
