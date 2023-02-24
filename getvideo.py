import requests
import re
from tqdm import tqdm

url = 'https://new.qqaku.com/20221216/CJ5fNjuq/1100kb/hls/index.m3u8'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

response = requests.get(url=url, headers=headers)
# print(response.text)

urlx = re.findall(r"(https:.+?.ts)", response.text)
print(urlx)

url1 = urlx[0]
print(url1)

# res1 = requests.get(url=url1, headers=headers)
# print(res1.content)

# f = open('aaa.mp4', "ab")
start = 1956
i = 0
for urls in tqdm(urlx):
    i = i + 1
    if i > start:
        res1 = requests.get(url=urls, headers=headers)
        # fxname = str(i) + ".mp4"
        with open("aaa1.mp4", mode='ab') as f:
            f.write(res1.content)

    # print(urls)
    # if i > 50:
    #     break

# f.close()
