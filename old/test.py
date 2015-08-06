from splinter import Browser
from bs4 import BeautifulSoup



with Browser() as browser:
    # Visit URL
    url = "http://www.twstats.com/en81/index.php?page=village_locator&stage=2&source=village"
    browser.visit(url)
    aaa = browser.find_by_name('village_coords')
    browser.fill(aaa, '440|429')
    browser.find_by_css('.ui-button.ui-widget.ui-state-default.ui-corner-all').click()
    

    html_doc = browser.html
    soup = BeautifulSoup(html_doc, 'html.parser')

    print(soup.prettify())
