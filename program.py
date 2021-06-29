import requests, bs4

search_query = "valorant live"
search_query = search_query.replace(" ","%20")

url = "https://rapidtags.io/api/generator?query=" + search_query + "&type=YouTube"

response = requests.get(url)
soup = bs4.BeautifulSoup(response.content, 'lxml')
# print(soup.text)

total_char = 0

tags = (eval(soup.text))["tags"]

for word in tags:
    total_char += len(word)

if total_char > 500:
    tags.pop()

print(total_char)
print(tags)