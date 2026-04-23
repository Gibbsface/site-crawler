import argparse
import re
import requests

def handle_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("-v", "--verbose", action="store_true")
    return parser.parse_args()

def fetch_response(url):
    try:
        return requests.get(url)
    except requests.exceptions.MissingSchema as e:
        # print(f"Error: \"{url}\" is missing schema.\n\tretrying this url with \"https://\" prefixed...")
        return fetch_response("https://" + url)