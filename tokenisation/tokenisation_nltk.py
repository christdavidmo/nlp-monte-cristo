import requests
from nltk.tokenize import word_tokenize


class TokenisationNltk:

    @classmethod
    def tokenise(text):

        tokens = word_tokenize(text,language='french')
        return tokens
      