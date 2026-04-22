from code.arg_handler import handle_args

def main():
    args = handle_args()

    if args.verbose:
        print(f"Base URL: {args.url}")

    

    

main()