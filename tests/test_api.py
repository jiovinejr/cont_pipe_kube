import unittest
from unittest.mock import patch
from src.api import fetch_pokemon

class TestPokemonAPI(unittest.TestCase):
    @patch("src.api.requests.get")
    def test_fetch_pokemon_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"results": [{"name": "bulbasaur"}]}
        
        data = fetch_pokemon()
        self.assertIsNotNone(data)
        self.assertIn("results", data)
        self.assertEqual(data["results"][0]["name"], "bulbasaur")

if __name__ == "__main__":
    unittest.main()