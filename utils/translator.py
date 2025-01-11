import requests

class Translator:

    def __init__(self, api_key):

        self.api_key = api_key

    def translate(self, word):

        # Примерный запрос к API (замените на корректный)

        response = requests.get(

            f"https://api.translationapi.com/translate?text={word}&key={self.api_key}")

        return response.json().get('translatedText', "Translation Error")

