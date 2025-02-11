import requests
from bs4 import BeautifulSoup

URL = "https://aws.amazon.com/blogs/big-data/"

def fetch_aws_blogs():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("article")

    blogs = []
    for article in articles:
        title = article.find("h2").text.strip()
        link = article.find("a")["href"]
        blogs.append({"title": title, "link": link})

    return blogs