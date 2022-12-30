import requests
def get_news_api(url, end_point):
    print("hi")
res = requests.get(url="https://github.com/DIYgod/RSSHub/tree/master/lib/routes")
print(res.headers)
res = res.json()
# print(res)
