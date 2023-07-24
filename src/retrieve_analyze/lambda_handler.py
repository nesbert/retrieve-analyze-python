from typing import Dict, Any
from . import analyze
from . import retrieve


# pylint: disable=unused-argument
def lambda_handler(event: Dict[str, Any], context: Any):
    # fetch data
    user_data = retrieve.fetch_user_data(event["id"])
    # analyze data
    comparison = analyze.analyze_user_data(user_data)
    # id, id_match?, name_match?, email_match?, gender_match?, status_match?
    return [
        event["id"],
        comparison["id"],
        comparison["name"],
        comparison["email"],
        comparison["gender"],
        comparison["status"],
    ]


def main():
    # pylint: disable=import-outside-toplevel
    import argparse
    import json
    import os
    import sys

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "event", type=str, nargs="?", help="JSON event object or file path"
    )
    args = parser.parse_args()

    event = None
    context = None

    if args.event:
        try:
            # Try to parse as JSON object
            event = json.loads(args.event)
            print(f"Parsed JSON event object: {event}")
        except json.JSONDecodeError:
            # Not a JSON object, treat as a file path
            if os.path.isfile(args.event):
                with open(args.event, "r", encoding="utf-8") as file:
                    event = json.load(file)
                    print(f"Loaded JSON event object from file: {event}")
            else:
                print(
                    f"No JSON event object could be decoded and no file found at path: {args.event}"
                )
    else:
        # No arguments, read from standard input
        event = json.load(sys.stdin)

    result = lambda_handler(event, context)
    print(json.dumps(result))


if __name__ == "__main__":
    main()
