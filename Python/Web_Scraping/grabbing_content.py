import requests 
import bs4 
# It Takes the url and and Stores the Html Content in the variable (results)
results = requests.get("https://www.example.com/")

#Returns Object Type 
print(type(results))

#Prints html source code.
print(results.text)

#
soup = bs4.BeautifulSoup(results.text,'lxml')

#It prints the code in the Format.
print(soup)

#To print the title of the WebPage.
#It returns in the list format because they may be more then one titles for the complecated webpages.

print(soup.select('title'))

#To grab all the Paragraphs in the html page.
print(soup.select('p'))

#Accessing the content Content 

#Storeing all the paragraph Tag data  in the variable.
#It returns in the list format So we can index them.
site_paragraphs = soup.select('p')

#Handling the data 
#->.getText() :- It is a meathod to asscess the data using indexing. And prints only data without HTML Tags
site_paragraphs[0].getText()

