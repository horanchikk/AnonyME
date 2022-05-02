import unittest
from client.python.client import AnonymeClient


class Client(unittest.TestCase):
    client: AnonymeClient

    @staticmethod
    def test_1_init():
        Client.client = AnonymeClient(
            'http://109.248.133.17:8000/'
        )

    @staticmethod
    def test_2_get_all_users():
        print(Client.client.users_get_all())


if __name__ == '__main__':
    unittest.main(verbosity=2)
