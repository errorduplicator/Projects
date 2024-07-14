import requests
from bs4 import BeautifulSoup

def get_proxy():

    # URL of the web page you want to extract text from
    url = "https://httpbin.io/ip"

    # Send a GET request to the URL and fetch the HTML content
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content,'html.parser')

    # Find all the text within HTML tags
    text = soup.get_text()

    # Print the extracted text
    proxy = text[text.find(':') + 3 : text.find('"\n}')]
    
    return proxy