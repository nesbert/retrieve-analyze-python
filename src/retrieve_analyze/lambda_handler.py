from . import analyze
from . import retrieve

def lambda_handler(event, context):
    # fetch data
    user_data = retrieve.fetch_user_data(event['id'])
    # analyze data
    comparison = analyze.compare_user_data(user_data)
    # TODO save to S3
    # id, id_match?, name_match?, email_match?, gender_match?, status_match?
    return [
        event['id'],
        comparison['id'],
        comparison['name'],
        comparison['email'],
        comparison['gender'],
        comparison['status']
    ]

def main():
    import argparse
    import json
    import os

    parser = argparse.ArgumentParser()
    parser.add_argument('event', type=str, help='JSON event object or file path')
    args = parser.parse_args()

    try:
        # Try to parse as JSON object
        event = json.loads(args.event)
        print(f'Parsed JSON event object: {event}')
    except json.JSONDecodeError:
        # Not a JSON object, treat as a file path
        if os.path.isfile(args.event):
            with open(args.event, 'r') as f:
                event = json.load(f)
                print(f'Loaded JSON event object from file: {event}')
        else:
            print(f"No JSON event object could be decoded and no file found at path: {args.event}")

    context = {}
    return lambda_handler(event, context)

if __name__ == "__main__":
    main()
