from code.functions import handle_args, is_url_valid
from code.queue import Queue

MAX_PAGES = 1_000

def main():
    args = handle_args()
    v = args.verbose
    if v:
        print(f"Base URL: {args.url}")

    q = Queue()
    q.push(args.url)
    n = 0
    #TODO initialize memo
    #TODO initialize error log

    while q.can_pop() and n < MAX_PAGES:
        url = q.pop()

        # this first block just tries to fetch a response
        try:
            response = request(url)
        except Exception as e:
            if v: print(f"Error: {e}\n\tSkipping Invalid URL: {url}")
        
        #this next block needs to use validate_ helper function to see if request is OK
        # if valid, we will parse the repsonse, memoize this url so we don't repeat it, and increment n
        # otherwise we will log the response code if it is a 4XX or 5XX error
        if validate_url(url)
        if response.status_code == requests.codes.ok:
            links = parse_the_response(url)
            memoize(url)
            n += 1
            # put that^ in a try block so we can catch parsing errors.
            # we still want to memoize and increment n, even if there's a parsing error
            # then if we find links, we'll queue them
            for links, check if in memo, else append to Queue
            
        else:
            log_error_stuff
    

    

main()