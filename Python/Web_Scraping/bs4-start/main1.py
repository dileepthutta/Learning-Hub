
import requests
from bs4 import BeautifulSoup

response = requests.get(
    url="https://news.ycombinator.com/news"
)

yc_webpage = BeautifulSoup(response.text, "html.parser")

#To find the Headings of the specific web Page through inspecting it.

#To get the first Data in the website.
soup = yc_webpage.find("span", class_="titleline")

#To print the 1st data link text score

# To print the link
link = soup.find("a").get("href")

# To print the text
text = soup.text

# To print the score.
score_points = yc_webpage.find(name="span", class_="score").getText()

print(text)
print(link)
print(score_points)

#To print the all links in the website.
all_att_links = yc_webpage.find_all("span",class_="titleline")
for i in all_att_links:
    print(i.find("a").get("href"))

#To Store all the article_text,article_links,article_points in the List Format.

#Loops runs until the articles reaches to end.
article_texts = []
article_links = []

articles = yc_webpage.find_all(name="span",class_="titleline")
for article in articles:
    article_texts.append(article.text)
    article_links.append(article.find('a').get('href'))

#To find the Scores of the articles.

article_scores = [int(score.getText().split()[0]) for score in yc_webpage.find_all(name="span",class_="score")]
print(article_scores)
print(article_texts)
print(article_links)


#To print the highest Score Article and Link and Text.
num = max(article_scores)
highest_index = article_scores.index(num)

print(f"Highest Score is {num} and Link:  {article_links[highest_index]} Article text: {article_texts[highest_index]}")
