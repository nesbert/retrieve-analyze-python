from gorest import users_v2 as client


def fetch_users(page: int = 1, limit: int = 10):
    return client.fetch_all(page, limit)


def main():
    # pylint: disable=import-outside-toplevel
    import argparse
    import json

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p", "--page", type=int, default=1, help="Page number for request"
    )
    parser.add_argument(
        "-l", "--limit", type=int, default=10, help="results per page for request"
    )
    args = parser.parse_args()
    users = fetch_users(args.page, args.limit)
    print(json.dumps(users))


if __name__ == "__main__":
    main()
