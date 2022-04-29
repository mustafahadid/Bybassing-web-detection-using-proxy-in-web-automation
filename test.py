
from urllib.request import Request, urlopen
import json
import random
import undetected_chromedriver as uc
import time


if __name__ == "__main__":
    req = Request('https://proxylist.geonode.com/api/proxy-list?limit=50&page=1&sort_by=lastChecked&sort_type=desc&country=TR',
                  headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req)
    data = json.load(webpage)
    list_ip = []
    for item in data['data']:
        name = item['ip']
        port = item['port']
        list_ip.append(f"{name}:{port}")

    ip = random.choice(list_ip)
    print(ip)

    opts = uc.ChromeOptions()
    opts.add_argument(f'--proxy-server=socks4://{ip}')
    browser = uc.Chrome(options=opts)
    browser.get('https://ifconfig.me/')
    time.sleep(15)
