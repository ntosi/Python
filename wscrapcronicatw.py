from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

cronica = 'https://twitter.com/cronicatv'
#conecto con la pag y la descargo

uClient = uReq(cronica)
page_html = uClient.read()
uClient.close()

#html parse
page_soup = soup(page_html, "html.parser")

#
containers = page_soup.find_all("div",{"class":"content"})


filename = 'tuits.csv'
f = open(filename, 'w')
header = 'tuit\n'
f.write("")

for container in containers:
    print(container.p.text)
    print(98 * "*")
    f.write(container.p.text + "\n")
    #f.write(98 * "*" + "\n")

f.close()
