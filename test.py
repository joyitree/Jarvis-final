import requests
import bs4 

base_url="https://www.google.com/search?q="
url = base_url+"what is the weather in mumbai"
requests_result =  requests.get(url)
soup = bs4.BeautifulSoup(requests_result.text,"html.parser")

ans = soup.find("div", class_="BNeave")
print(ans)