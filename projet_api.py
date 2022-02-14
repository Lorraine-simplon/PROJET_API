import requests
from bs4 import BeautifulSoup

# Metttre le lien du site que l'on veut utiliser
url = 'https://fr.wikipedia.org/wiki/Liste_des_pays_par_population'

# Faire une requête 
response = requests.get(url)

#print(response)
# Va nous donner le résultat 200 qui signifie que la demande HTTP a réussi
# Pour GET la réponse contiendra une entité correspondant à la ressource demandée

#print(response.headers)

print(response.text)
# Donne le code HTML de la page

#if response.ok:
    #soup = BeautifulSoup(response.text)
    #title = soup.find('title')
    #print(title.text) # .text permet de retirer les balises <> autour du titre
# Va permettre d'aller chercher des éléments à l'intérieur de la page
    
if response.ok:
    soup = BeautifulSoup(response.text)
    tds = soup.findAll('tr')
    print(len(tds))
    [print(str(tr.text) + '\n)') for tr in tds]