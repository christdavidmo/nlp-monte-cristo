import requests

class LoadRoman:

    @staticmethod
    def Load(url):

        response = requests.get(url)
        response.encoding = 'utf-8'
        raw_text = response.text

        DEBUT = '*** START OF THE PROJECT GUTENBERG EBOOK 17989 ***'
        FIN   = '*** END OF THE PROJECT GUTENBERG EBOOK 17989 ***'

        roman = raw_text.split(DEBUT)[1].split(FIN)[0]

        # print(f'Taille du roman (sans métadonnées) : {len(roman):,} caractères')
        # print(f'Nombre de lignes : {roman.count(chr(10)):,}')
        # print(f'Aperçu :\n{roman[:500]}')

        return roman
