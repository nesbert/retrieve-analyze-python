import json
import os
import requests

from gorest import users_v1
from gorest import users_v2
from retrieve_analyze import OUTPUT_DIR

# Fetch user details from each source/module
def fetch_user_data(user_id):
    print(f"Retrieving user #{user_id} from sources")

    try:
        user_data_v1 = users_v1.fetch(user_id)
    except requests.exceptions.HTTPError as err:
        user_data_v1 = f"An HTTP error occurred: {err}"
    except Exception as err:
        user_data_v1 = f"An error occurred: {err}"

    try:
        user_data_v2 = users_v2.fetch(user_id)
    except requests.exceptions.HTTPError as err:
        user_data_v2 = f"An HTTP error occurred: {err}"
    except Exception as err:
        user_data_v2 = f"An error occurred: {err}"

    return {
        'users_v1': user_data_v1,
        'users_v2': user_data_v2
    }

# Save user details from each source/module
def save_user_data(user_id, user_data):
    user_directory = f'{OUTPUT_DIR}/{user_id}'

    print(f"Saving user data to {user_directory}")

    try:
        # Ensure directory exists, create it if necessary
        os.makedirs(user_directory, exist_ok=True)

        # Save data from each source to a separate JSON file
        for source, data in user_data.items():
            with open(f'{user_directory}/{source}.json', 'w') as f:
                json.dump(data, f)

    except PermissionError:
        print(f"Permission denied when trying to write to '{user_directory}'")
    except IsADirectoryError:
        print(f"Expected a directory, but found a file at '{user_directory}'")
    except FileNotFoundError:
        print(f"Invalid path: '{user_directory}' does not exist")
    except IOError as e:
        print(f"An I/O error occurred: {str(e)}")

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('user_id', type=str, help='User ID to retrieve data from API sources')
    args = parser.parse_args()

    user_data = fetch_user_data(args.user_id)

    save_user_data(args.user_id, user_data)

    return user_data

if __name__ == "__main__":
    main()
