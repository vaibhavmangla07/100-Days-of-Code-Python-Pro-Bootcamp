from bs4 import BeautifulSoup

with open(r"/Users/vmangla/Documents/Vaibhav/Programming/Programming in Python/100 - Days of Code/Day 45/WebScraping/website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))
    pass

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

github_anchor = soup.select_one(selector="p a")
print(github_anchor)

name = soup.select_one(selector="#name")
print(name)

headings = soup.select(".heading")
print(heading)