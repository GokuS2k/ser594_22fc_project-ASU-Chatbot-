import requests
from bs4 import BeautifulSoup

def file_reader():
    f = open(r"chatbot2_prime.txt")
    print("Reading the DB")
    return f

def web_scrapping(loc_name):
    loc_name = loc_name.lower()
    url1 = "https://www.asu.edu/about/facts-and-figures"
    classname = "uds-table"
    res = requests.get(url1)
    soup = BeautifulSoup(res.content, 'html.parser')
    table = soup.find('div', class_="uds-table")
    tbody = table.find('tbody')
    rows = tbody.findAll('tr')[1:6]
    dict = {}
    for row in rows:
        cols = row.findAll('td')
        dict[cols[0].text.split(' ')[0].lower()] = cols[1].text

    return dict[loc_name] if loc_name in dict else ''
#web_scrapping("")