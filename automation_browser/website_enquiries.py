# write a python code that enquire https://www.gov.uk and look for an announcement with specified words

import requests
from bs4 import BeautifulSoup

date = '27/06/2023'
user_keywords = ['UN']
keyword_list = ''
for k in user_keywords:
    keyword_list = keyword_list + '%20' + k
keyword_list = keyword_list[3:]

base_url = "https://www.gov.uk"
url = f"{base_url}/search/news-and-communications?keywords={keyword_list}&public_timestamp%5Bfrom%5D={date}&order=relevance"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    announcements = soup.find_all("li", class_="gem-c-document-list__item")

    for announcement in announcements:
        title = announcement.find(class_="gem-c-document-list__item-title").text.strip()
        description = announcement.find(class_="gem-c-document-list__item-description").text.strip()
        announcement_url = announcement.find("a")["href"]

        print("Title:", title)
        print("Description:", description)
        print("url:", f"{base_url}{announcement_url}")
        print("-" * 50)
else:
    print("Failed to fetch the webpage. Status code:", response.status_code)
