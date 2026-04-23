import requests
import time

from code.functions import *
from code.queue import Queue

MAX_PAGES = 200

def main():
    base_url, v = handle_args()
    if v: print(f"Base URL: {base_url}")

    try:
        verify_base_url(base_url)
    except Exception:
        print("Error: base url provided is missing schema. " \
        "\n\tPrepending \"https://\" and continuing...")
        base_url = "https://" + base_url
    # if not base_url.endswith("/"): base_url += "/"

    q = Queue()
    memo = []
    n = 0
    #TODO initialize log. 
    # we want to log every url attempted and the outcome
    # url, response code (200, 4XX, 5XX, other), external urls, count of every duplicate, which links it had

    # start timer
    start_time = time.perf_counter()

    q.push(base_url)
    while q.can_pop() and n < MAX_PAGES:
        url = q.pop()
        if v: print(f"\n{url}")

        # check memo
        if url in memo:
            if v: print(f"\tSKIP: duplicate {url}")
            continue

        # this first block just tries to fetch a response
        try:
            r = fetch_response(url)
        except requests.exceptions.SSLError as e:
            if v: print("\tRETRY: SSL could not be verified, retrying with SSl verification disabled...")
            try:
                r = fetch_response(url, verify=False)
            except Exception as e:
                if v: print("\tFAILED: skipping")
                continue
        except Exception as e:
            if v: print(f"\tSKIP: unable to get a response...")
            print(e)
            continue

        if v: print(f"\t{r.status_code} received for {url}")

        memo.append(url)

        # this second block actually processes the result
        if r.status_code == requests.codes.ok:
            n += 1
            links = extract_links(r.text, base_url)
            for l in links:
                q.push(l)

        else:
            print(f"\n{r.status_code} for {url}")
            # invalid response, log it

        # if v: print(f"\tfound {len(links)} links, added {} to queue")
        if v: print(f"\n{q.size()} IN QUEUE\n")
        

    #end of loop, queue is empty (or max hit)
    exec_time = time.perf_counter() - start_time
    print("\n--- DONE ---")
    if n >= MAX_PAGES: print(f"Max page limit reached")
    print(f"Processed {n} unique valid pages in {exec_time:.4f}s\n")

    
main()