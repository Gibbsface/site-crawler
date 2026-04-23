import requests
import time

from code.functions import handle_args, fetch_response
from code.queue import Queue

MAX_PAGES = 1_000

def main():
    args = handle_args()
    v = args.verbose
    if v:
        print(f"Base URL: {args.url}")

    q = Queue()
    memo = []
    n = 0
    #TODO initialize memo
    #TODO initialize error log

    #TEST STUFF
    q.push("www.dts.edu")
    q.push("http://www.dts.edu")
    q.push("https://www.dts.edu")
    q.push("www.dts.edu/3245")
    q.push("asdfasdf.dtsesf.owij")
    q.push("www.dts.edu")
    #TEST STUFF

    # start timer
    start_time = time.perf_counter()

    q.push(args.url)
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
        except Exception as e:
            if v: print(f"\tSKIP: unable to get a response...")
            continue

        if v: print(f"\t{r.status_code} received for {url}")

        memo.append(url)

        # this second block actually processes the result
        if r.status_code == requests.codes.ok:
            # valid response recieved, time to parse and stuff
            # links = parse_the_response(r.text) this function will accept html and spit out a list of links to queue
            links = []
            n += 1
            pass
        else:
            pass
            # invalid response, log it

        # this final block will queue original links
        for l in links:
            if l not in memo: q.push(l)

    #end of loop, queue is empty
    exec_time = time.perf_counter() - start_time
    print("\n--- DONE ---")
    print(f"Processed {n} unique valid pages in {exec_time:.4f}s\n")
        
        #this next block needs to use validate_ helper function to see if request is OK
        # if valid, we will parse the repsonse, memoize this url so we don't repeat it, and increment n
        # # otherwise we will log the response code if it is a 4XX or 5XX error
        # if validate_url(url)
        # if response.status_code == requests.codes.ok:
        #     links = parse_the_response(url)
        #     memoize(url)
        #     n += 1
        #     # put that^ in a try block so we can catch parsing errors.
        #     # we still want to memoize and increment n, even if there's a parsing error
        #     # then if we find links, we'll queue them
        #     for links, check if in memo, else append to Queue
            
        # else:
        #     log_error_stuff
    

    

main()