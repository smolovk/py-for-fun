import requests

urls = ["https://ftl.kherson.ua/"]

for url in urls:
    print(f'Analyzing {url}')
    for i in range(10):
        r = requests.get(url)
        if r.status_code != 200:
            print(f'WOW!!!, found code {r.status_code} on {i} iteration of analyzing {url}')