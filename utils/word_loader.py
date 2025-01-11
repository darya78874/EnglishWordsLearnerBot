class WordLoader:

    def __init__(self):

        self.words = []

    def load_words(self):

        # В реальном приложении, возможно, загрузка слов из базы данных или API

        return self.words

    def add_word(self, word):

        self.words.append(word)

