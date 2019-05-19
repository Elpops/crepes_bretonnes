from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from blog.models import Article

def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return HttpResponse("""
        <h1>Bienvenue sur mon blog !</h1>
        <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>
    """)

def view_article(request, id_article):
    """
    Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
    Son ID est le second paramètre de la fonction (pour rappel, le premier
    paramètre est TOUJOURS la requête de l'utilisateur)
    """
    return HttpResponse(
        "Vous avez demandé l'article n° {0} !".format(id_article)
    )

def date_actuelle(request):
    return render(request, 'blog/date.html', {'date' : datetime.now()})

def addition(request, nombre1, nombre2):
    total  = nombre1 + nombre2

    return render(request, 'blog/addition.html', locals())

def accueil(request):
    articles = Article.objects.all()
    return render(request, 'blog/accueil.html', {"derniers_articles": articles})

def lire(request, id):
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404

    return render(request, 'blog/lire.html', {'article': article})
