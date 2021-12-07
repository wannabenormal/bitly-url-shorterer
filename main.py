import os
import argparse
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv
load_dotenv()


def shorten_link(token, url):
    headers = {
      "Authorization": f"Bearer {token}"
    }

    payload = {
      "long_url": url
    }

    response = requests.post(
        "https://api-ssl.bitly.com/v4/bitlinks",
        headers=headers,
        json=payload
    )

    response.raise_for_status()

    return response.json()["link"]


def count_clicks(token, bitlink):
    headers = {
      "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary",
        headers=headers
    )

    response.raise_for_status()

    return response.json()["total_clicks"]


def is_bitlink(token, link):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        f"https://api-ssl.bitly.com/v4/bitlinks/{link}",
        headers=headers
    )

    return response.ok


def main():
    bitly_token = os.getenv("BITLY_TOKEN")

    parser = argparse.ArgumentParser(description="Создание и подсчет кликов bit.ly")
    parser.add_argument("link", help="Ссылка для преобразования или bitly-сыллка")
    args = parser.parse_args()

    inputed_url = args.link
    parsed_url = urlparse(inputed_url)
    
    if not parsed_url.scheme:
        inputed_url = f"http://{inputed_url}"

    link = f"{parsed_url.netloc}{parsed_url.path}"

    try:
        if is_bitlink(bitly_token, link):
            print("Кол-во кликов", count_clicks(bitly_token, link))

        else:
            print("Битлинк: ", shorten_link(bitly_token, inputed_url))

    except requests.exceptions.HTTPError:
        print("Введена некорректная ссылка")


if __name__ == "__main__":
    main()
