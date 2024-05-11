# PHPSESSID=dea8da2e970174256948f0c286282a8f053066f8
import requests
import os
import re
# https://cses.fi/problemset/view/1068/


# for x in open("tasks.txt"):
for id in ['2191', '2192', '2193', '2194', '2195']:
    # data = x.strip().split()
    # id = data[0].split("/")[-1]

    url = f"https://cses.fi/problemset/task/{id}/"

    headers = {
        "Cookie": "PHPSESSID=dea8da2e970174256948f0c286282a8f053066f8"
    }

    response = requests.get(url, headers=headers)

    # print(response.text)

    # href="/problemset/result/9128534/"
    # find first
    first = re.search(r'href="/problemset/result/(\d+)/"', response.text)

    if first:
        print(id, f"https://cses.fi/problemset/result/{first.group(1)}/")
        pass
    else:
        print(id, "Not found")
