import requests
import beautifulsoup4


headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Connection': 'keep-alive'
}

hh_request = requests.get("https://hh.ru/search/vacancy?text=python&items_on_page=100&st=searchVacancy", headers=headers)

print(hh_request.text)