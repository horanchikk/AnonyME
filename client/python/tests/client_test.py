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
    def test_2_get_all_users_rooms():
        print(Client.client.users_get_all())
        print(Client.client.rooms_get_all())

    @staticmethod
    def test_3_create_room_and_active():
        username1 = 'ETHOSA2'
        username2 = 'HORANCHIKK2'
        user1 = Client.client.users_new(username1)
        print('create user:', user1)
        user2 = Client.client.users_new(username2)

        room = Client.client.rooms_new('Ethosa room', user1['response']['token'], 4)
        print('create room:', room)

        response = Client.client.users_room_enter(user2['response']['token'], room['response']['token'])
        print('enter in the room:', response)

        response = Client.client.users_remove(user1['response']['token'])
        Client.client.users_remove(user2['response']['token'])
        print('delete users:', response)


if __name__ == '__main__':
    unittest.main(verbosity=2)
