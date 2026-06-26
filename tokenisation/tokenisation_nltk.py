from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.util import bigrams
from collections import Counter


class TokenisationNltk:

    @staticmethod
    def tokenise(text):
        # ===> Tokenise le texte 
        tokens = word_tokenize(text,language='french')
        return tokens
    

    @staticmethod
    def remove_stopwords(tokens):
        # ===> Supprime les stopwords français.
        stop_words = set(stopwords.words('french'))

        token_filtre = [t for t in tokens if t.lower() not in  stop_words]

        return token_filtre
    

    @staticmethod
    def get_bigramme(tokens):
        # ===> Affiche le nombre de bigramme
        bigrammes = list(bigrams(tokens))
        return bigrammes
    
    
    @staticmethod
    def get_nbr_token(tokens):
        # ===> Affiche le nombre de tokens
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


