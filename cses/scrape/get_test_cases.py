# PHPSESSID=dea8da2e970174256948f0c286282a8f053066f8
import requests
import os
import re

cnt = 0
for x in open("test_cases.txt"):

    data = x.strip().split()

    url = data[0]
    id = data[1].split("/")[-1]

    cnt += 1
    if os.path.exists(f"test_cases/{id}"):
        continue

    os.system(f"mkdir -p test_cases/{id}")

    headers = {
        "Cookie": "PHPSESSID=dea8da2e970174256948f0c286282a8f053066f8"
    }

    r = requests.get(url, headers=headers)

    # <a class="save" title="Save" href="{href}">save</a>

    # find all
    all_urls = re.findall(
        r'<a class="save" title="Save" href="(.+?)">save</a>', r.text)
    assert len(all_urls) % 2 == 0, id

    for i, url in enumerate(all_urls):
        test_case = requests.get("https://cses.fi" + url, headers=headers)

        # print(test_case.text)

        if '/1/' in url:
            with open(f"test_cases/{id}/{i // 2}.in", "w") as f:
                f.write(test_case.text)
        else:
            with open(f"test_cases/{id}/{i // 2}.out", "w") as f:
                f.write(test_case.text)

    print()

print(cnt)
