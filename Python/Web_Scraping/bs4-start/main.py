from bs4 import BeautifulSoup
import lxml

with open('website.html',encoding='utf-8',mode='r')as file:
    contents = file.read()

soup = BeautifulSoup(contents,"html.parser")

#To print the Entire Tag and Content.
print(soup.title)

#To print the Tag name.
print(soup.title.name)

#To print the data inside the Tag.
print(soup.title.string)

# Will provide all the indented code.
print(soup.prettify())

#To print the attribute link.
print(soup.a)


# .find_all(name="Name of the Tag") :=It finds the list of Tags which we have specified.
#It returns all the List of anchor Tags.
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)



for tag in all_anchor_tags:
    #.getText() := It returns the Text in side the Anchor Tag.
    print(tag.getText())

    #.get('href') := To get the Link inside the href.
    print(tag.get('href'))


#To get the Tag with Specified Selectors.
heading = soup.find("h1",id="name")
print(heading.getText)

#To Select with CSS in descendant way.
url = soup.select_one(selector="p a")
print(url)

#Select By ID
id_selector = soup.select_one(selector="#name")
print(id_selector)