from splinter import Browser
from bs4 import BeautifulSoup



with Browser() as browser:
    # Visit URL
    url = "http://www.twstats.com/en81/index.php"
    browser.visit(url)
    html_doc = browser.html
    soup = BeautifulSoup(html_doc, 'html.parser')

    print(soup.prettify())
