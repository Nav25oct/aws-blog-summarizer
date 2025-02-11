import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

AWS_BLOG_URL = "https://aws.amazon.com/blogs/big-data/"

def fetch_aws_blogs():
    """Fetches the list of AWS blogs with title and link."""
    response = requests.get(AWS_BLOG_URL)
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("article")

    blogs = []
    for article in articles:
        title = article.find("h2").text.strip()
        link = article.find("a")["href"]
        
        # Ensure the link is a full URL
        if not link.startswith("http"):
            link = "https://aws.amazon.com" + link

        blogs.append({"title": title, "link": link})

    return blogs

from playwright.sync_api import sync_playwright

def fetch_blog_content(blog_url):
    """Fetches the full content of an AWS blog post using Playwright to handle JavaScript rendering."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Run in headless mode
        page = browser.new_page()
        page.goto(blog_url, timeout=60000)  # Wait for the page to load

        # Wait for blog content to be visible
        page.wait_for_selector("article", timeout=15000)  # Adjust selector as needed

        # Extract the full page content
        ## content = page.locator("article").inner_text()

        content = page.inner_text("body")

        browser.close()

    # Debugging: Print first 500 characters of fetched content
    print("Fetched Blog Content:", content[:500])

    return content if content else "Error: No blog content found."