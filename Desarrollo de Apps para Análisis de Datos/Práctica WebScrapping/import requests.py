import requests
from bs4 import BeautifulSoup

# r = requests.get('https://en.wikipedia.org/wiki/List_of_U.S._states_by_date_of_admission_to_the_Union')
# print(r)
# print(r.status_code)
# print(r.text)
# print(r.content)

# soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.prettify())

# states = soup.find(id="firstHeading").find(class_="firstHeading mw-first-heading").get_text()


page = requests.get("https://en.wikipedia.org/wiki/List_of_U.S._states_by_date_of_admission_to_the_Union")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="toc")
forecast_items = seven_day.find_all(class_="toclevel-1 tocsection-1")
tonight = forecast_items[0].find(text=True)
# print(tonight.prettify())
# print(type(tonight.prettify()))
# print(type(tonight))
print(tonight)