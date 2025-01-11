import random

class QuizGenerator:

    def __init__(self, words):

        self.words = words

    def generate_quiz(self):

        return random.sample(self.words, k=min(3, len(self.words)))

