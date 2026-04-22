import argparse

def handle_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("-v", "--verbose", action="store_true")
    return parser.parse_args()