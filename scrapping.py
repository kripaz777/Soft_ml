from bs4 import BeautifulSoup
import requests
import pandas as pd
n = int(input("Enter page no = "))
category = ["political","social","entertainment","sports","view","blog","International"]
news_data = {'category':[],'news_url':[],"News":[]}
for j in category:
    for i in range(1,n+1):
        url = BeautifulSoup(f'https://en.setopati.com/{j}?page={i}', 'html.parser')
        soup = requests.get(url)
        soup = BeautifulSoup(soup.text, "lxml")
        section = soup.section
        for link in section.find_all('a'):
            news_urls = link.get('href')
            if "page" not in news_urls:
                news_data['news_url'].append(news_urls)
                news_data['category'].append(j)


for i in news_data['news_url']:
    url = BeautifulSoup(i, 'html.parser')
    data = requests.get(url)
    news_code = BeautifulSoup(data.text, "lxml")
    try:
        final_new = news_code.find("div", class_="editor-box").text
        news_data["News"].append(final_new)
    except:
        news_data["News"].append("NAN")

print(news_data)        



import pandas as pd
df = pd.DataFrame(news_data)
df.to_csv('scrapped_news.csv')
df






