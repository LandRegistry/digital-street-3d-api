import unittest

from index_map_3d_api.main import app


class TestHealth(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_health(self):
        self.assertEqual((self.app.get('/health')).status_code, 200)
