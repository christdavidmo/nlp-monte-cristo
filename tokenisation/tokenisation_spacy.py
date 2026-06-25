import spacy

class TokenisationSpacy:

    @staticmethod
    def Tokenise(text):

        NLP = spacy.load('fr_core_news_sm')

        doc =NLP(text)

        token_spacy = [token.text for token in doc]

        return token_spacy
