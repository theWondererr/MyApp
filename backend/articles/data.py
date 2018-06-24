# read data

def get_articles():
    import pandas as pd

    articles = pd.read_excel('./class_articles.xlsx', sep=";",  header=[0,1], index_col=[0,1])
    return(articles)