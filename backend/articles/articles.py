class Article:
    def __init__(self, nom ='', numero=0):
        self.nom = nom
        self.text = ""
        self.numero = numero
    
    def write(self, text, value):
        self.text = text.format(value)

class Convention:
    def __init__(self):
        self.dic_articles = {}
    
    def add_article(self, article):
        
        if article.numero in self.dic_articles:
            raise KeyError('This article number already exists')

        else:
            self.dic_articles[article.numero] = article

class Categorie_articles():
    def __init__(self, regles, numero=0, nom="nom"):
        self.numero = numero
        self.nom = nom
        self.regles = regles
        