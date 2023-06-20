from django.test import TestCase
from rest_framework.test import APIClient
from unitTest.models import Game
from .views import send_notification
from unittest.mock import patch

class GameViewsetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.game1 = Game.objects.create(name='Game 1', editor='Editor 1', nb_players=2)
        self.game2 = Game.objects.create(name='Game 2', editor='Editor 2', nb_players=4)

    def test_list_games(self):
        response = self.client.get('http://127.0.0.1:8000/api/game/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_game(self):
        response = self.client.get(f'http://127.0.0.1:8000/api/game/{self.game1.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Game 1')
        self.assertEqual(response.data['editor'], 'Editor 1')
        self.assertEqual(response.data['nb_players'], 2)

    def test_create_game(self):
        data = {'name': 'New Game', 'editor': 'New Editor', 'nb_players': 3}
        response = self.client.post('http://127.0.0.1:8000/api/game/', data)
        self.assertEqual(response.status_code, 201)
        print(response.data)
        self.assertEqual(Game.objects.count(), 3)
        self.assertEqual(Game.objects.last().name, 'New Game')
        self.assertEqual(Game.objects.last().editor, 'New Editor')
        self.assertEqual(Game.objects.last().nb_players, 3)

    def test_update_game(self):
        data = {'name': 'Updated Game', 'editor': 'Updated Editor', 'nb_players': 5}
        response = self.client.put(f'http://127.0.0.1:8000/api/game/{self.game1.id}/', data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Game.objects.get(id=self.game1.id).name, 'Updated Game')
        self.assertEqual(Game.objects.get(id=self.game1.id).editor, 'Updated Editor')
        self.assertEqual(Game.objects.get(id=self.game1.id).nb_players, 5)

    def test_update_game_2(self):
        data = {'nb_players': 6}
        response = self.client.patch(f'http://127.0.0.1:8000/api/game/{self.game1.id}/', data)
        self.assertEqual(response.status_code, 200)

        self.assertEqual(Game.objects.get(id=self.game1.id).nb_players, 6)


    def test_delete_game(self):
        response = self.client.delete(f'http://127.0.0.1:8000/api/game/{self.game1.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Game.objects.count(), 1)

# Erreur

    def test_retrieve_game_error(self):
        response = self.client.get(f'http://127.0.0.1:8000/api/game/5') # Missing data in bdd
        self.assertEqual(response.status_code, 301)

    def test_create_game_error(self):
        data = {'name': 'New Game', 'editor': 'New Editor'}  # Missing 'nb_players' field
        response = self.client.post('http://127.0.0.1:8000/api/game/', data)
        self.assertEqual(response.status_code, 400)
        
    def test_create_game_error_2(self):
        data = {'name': 'New Game', 'editor': 'New Editor', 'nb_players': "yuyuy"}  # nb_players string instead of integer
        response = self.client.post('http://127.0.0.1:8000/api/game/', data)
        self.assertEqual(response.status_code, 400)

    def test_create_game_error_3(self):
        data = {'name': 'New Game', 'editor': 'New Editor', 'nb_players': -2}  # nb_players negatif
        response = self.client.post('http://127.0.0.1:8000/api/game/', data)
        self.assertEqual(response.status_code, 400)

    def test_update_game_error(self):
        data = {'name': 'Updated Game 2', 'editor': 'Updated Editor 2', 'nb_players': 5} # Missing data in bdd
        response = self.client.put(f'http://127.0.0.1:8000/api/game/5', data)
        self.assertEqual(response.status_code, 301)

    def test_delete_game(self):
        response = self.client.delete(f'http://127.0.0.1:8000/api/game/5/') # Missing data in bdd
        self.assertEqual(response.status_code, 404)


    



class GameViewsetTestCaseMocked(TestCase):
    print('voila')

