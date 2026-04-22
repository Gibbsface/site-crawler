from code.arg_handler import handle_args

def main():
    args = handle_args()
    is_v = args.verbose
    base_url = args.url

    if is_v:
        print(f"Base URL: {base_url}")

    

    

main()