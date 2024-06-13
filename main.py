import requests
from bs4 import BeautifulSoup


# This is the website that we want to scrape
website = 'https://quotes.toscrape.com/'
result = requests.get(website)
content = result.text

# This is the parser that we want to use
soup = BeautifulSoup(content,'html.parser')

# These are the authors that we want to scrape from the website
authors = (soup.find_all("small",{"class":"author"}))
authors_text = [author.get_text() for author in authors]

# These are the quote we want to scrape from the website
quotes = soup.find_all("span", {"class": "text"})
quotes_text = [quote.get_text() for quote in quotes]



# These are the authors and quotes that we want to print together
for author, quote in zip(authors_text, quotes_text):
    print(f"{quote} - {author}")
    print()
    

    









    
    

