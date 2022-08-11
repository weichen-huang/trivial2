import requests, json, datetime, time, re

pages = []
problems = []

sess = requests.Session()

params = {
    "action": "query",
    "format": "json",
    "list": "allpages",
    "aplimit": "max",
    "origin": "*",
    "apprefix": "1950"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "DNT": "1",
    "Connection": "close",
    "Upgrade-Insecure-Requests": "1"
}

cur_year = int(datetime.date.today().year)+2

for year in range(1950, cur_year):
    params["apprefix"] = str(year)
    r = sess.get("https://artofproblemsolving.com/wiki/api.php", params=params, headers=headers)
    print("Got {} / {}".format(year - 1949, cur_year - 1950))
    data = r.json()['query']['allpages']
    for page in data:
        if page['title'][0] != '/':
            pages.append(page['title'])

for page in pages:
    if "Problems/Problem" in page and re.match('^\d{4}', page) and page.split(" ")[-1].isnumeric():
        problems.append(page)

with open("data/allproblems.json", "w") as f:
    json.dump(problems, f, indent=2)
    f.close()
