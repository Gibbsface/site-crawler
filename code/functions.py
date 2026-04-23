import argparse
import re
import requests

def handle_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("-v", "--verbose", action="store_true")
    p = parser.parse_args()
    return p.url, p.verbose

def verify_base_url(url):
    if url.startswith("https://") or url.startswith("http://"):
        return True
    else:
        raise Exception

def fetch_response(url):
    try:
        return requests.get(url)
    except requests.exceptions.MissingSchema as e:
        # print(f"Error: \"{url}\" is missing schema.\n\tretrying this url with \"https://\" prefixed...")
        return fetch_response("https://" + url)
    
def extract_links(text, base_url):
    ans = re.findall(r"href=\"(.*?)\"", text)
    ans = list(filter(lambda x: not x.startswith("#"), ans))
    ans = list(map(lambda x: base_url + x if x.startswith("/") else x, ans))
    ans = list(filter(lambda x: x.startswith(base_url), ans))
    return ans

