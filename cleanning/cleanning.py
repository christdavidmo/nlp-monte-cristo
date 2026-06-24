import requests
import re


class Cleanning :

    @staticmethod
    def clean_text(text):
        """Nettoie un texte pour une analyse NLP en français."""

        # 1. Mise en minuscules
        text = text.lower()

        # 2. Suppression des marqueurs d'italique Gutenberg (_mot_)
        text = re.sub(r'_([^_]+)_', r'\1', text)

        # 3. Remplacement des sauts de ligne et tabulations par des espaces
        text = re.sub(r'[\n\r\t]+', ' ', text)

        text = re.sub(r'-','_',text) # ===> Je remplace d'abord le trait d'union par tiret du 8

        # 4. Suppression de la ponctuation et des caractères spéciaux
        #    On conserve les lettres françaises accentuées
        text = re.sub(r"[^a-zàâçéèêëîïôûùüÿñæœ'_ ]", ' ', text)

        text = re.sub(r'\b\d+\b', ' ', text) # ===> supprimer les nombres isolés

        # 5. Normalisation des apostrophes typographiques
        text = re.sub(r"[''`]", "'", text)

        # 6. Suppression des espaces multiples
        text = re.sub(r'\s+', ' ', text)

        # 7. Suppression des espaces en début et fin
        text = text.strip()
        
        return text
   
