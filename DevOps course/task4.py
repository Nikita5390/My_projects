import sys
import requests

URL = input("enter your URL")

try:
    response = requests.get(URL, timeout=5)
    if response.status_code == 200:
        print(f"Сайт доступен: {URL}")
    else:
        print(f"Сайт вернул код {response.status_code}")
        sys.exit(1)
except requests.RequestException as e:
    print(f"Ошибка при подключении к {URL}:\n{e}")
    sys.exit(1)
