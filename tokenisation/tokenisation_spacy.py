import spacy
from nltk.corpus import stopwords
from nltk.util import bigrams



from collections import Counter

class TokenisationSpacy:

    @staticmethod
    def Tokenise(text):

        NLP = spacy.load('fr_core_news_sm')
        doc =NLP(text)
        tokens = [token.text for token in doc]
        return tokens
    

    @staticmethod
    def Remove_Stopwords(tokens):

        stop_words= set(stopwords.words('french'))
        token_filtre = [t for t in tokens if t.lower() not in stop_words]
        return token_filtre
    

    @staticmethod
    def Get_Bigramme(tokens):

        bigrammes = list(bigrams(tokens))
        return bigrammes
    

    @staticmethod
    def Get_Nbr_Token(tokens):
        compteur = Counter(tokens)
        return compteur
    

    @staticmethod
    def get_status(tokens):
        # ===> Affiche les statistiques

        total = len(tokens)
        unique = len(set(tokens))
        richesse_lexicale = unique / total if total > 0 else 0


        stats ={
            'total' : total ,
            'unique' : unique ,
            'richesse_lexicale' : richesse_lexicale
        }

        return stats
