import argparse
import re

def handle_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("-v", "--verbose", action="store_true")
    return parser.parse_args()

def is_url_valid(url):
    # do I really even need this? 
    return True