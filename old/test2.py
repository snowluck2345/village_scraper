import csv
from bs4 import BeautifulSoup
import re
import csv

soup = BeautifulSoup(open("TWStats.html"))

dschreib_list = soup.find_all(href="index.php?page=village&id=9125")

#print soup.prettify

body = soup.body.find(id="main")
table = body.find(style="width: 100%")
sub_table = table.tbody.tr.contents[3]
tbody = sub_table.div.table.tbody
contents = tbody.contents

print contents
