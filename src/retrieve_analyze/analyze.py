import json
import os

from retrieve_analyze import OUTPUT_DIR

def user_directory(user_id):
    return f'{OUTPUT_DIR}/{user_id}'

def analyze_user_data(data_dic):
    # Extract the 'data' from users_v1.json
    users_v1_data = data_dic['users_v1'].get('data')

    # Compare the JSON objects
    comparison = {}
    for key in data_dic['users_v2'].keys():
        if users_v1_data.get(key) == data_dic['users_v2'].get(key):
            comparison[key] = True
        else:
            comparison[key] = False

    return comparison

def read_user_data(user_id):
    directory = user_directory(user_id)
    users_v1_file = f'{directory}/users_v1.json'
    users_v2_file = f'{directory}/users_v2.json'

    try:
        data_dic = {}
        # Load the JSON data from each file
        with open(users_v1_file) as f:
            data_dic['users_v1'] = json.load(f)
            if not isinstance(data_dic['users_v1'], dict):
                print(f'Error: Data in {users_v1_file} is not a JSON object')
                return

        with open(users_v2_file) as f:
            data_dic['users_v2'] = json.load(f)
            if not isinstance(data_dic['users_v2'], dict):
                print(f'Error: Data in {users_v2_file} is not a JSON object')
                return

        comparison = analyze_user_data(data_dic)

        return {
            'id': user_id,
            'files': [
                users_v1_file,
                users_v2_file
            ],
            'results': comparison
        }

    except FileNotFoundError:
        print(f"No data found for user ID: {user_id}")
    except json.JSONDecodeError:
        print(f"Error decoding JSON for user ID: {user_id}")

# Save user details from each source/module
def save_analysis_data(user_id, analysis_data):
    if analysis_data is None:
        return

    directory = user_directory(user_id)
    analysis_file = f'{directory}/analysis.json'
    print(f"Saving analysis to {analysis_file}")

    try:
        # Ensure directory exists, create it if necessary
        os.makedirs(directory, exist_ok=True)

        # Save data from each source to a separate JSON file
        with open(analysis_file, 'w') as f:
            json.dump(analysis_data, f)

    except PermissionError:
        print(f"Permission denied when trying to write to '{directory}'")
    except IsADirectoryError:
        print(f"Expected a directory, but found a file at '{directory}'")
    except FileNotFoundError:
        print(f"Invalid path: '{directory}' does not exist")
    except IOError as e:
        print(f"An I/O error occurred: {str(e)}")


def main():
    import argparse
    import sys

    parser = argparse.ArgumentParser()
    parser.add_argument('user_id', type=str, nargs='?', help='User ID to analyze data')
    parser.add_argument('--save', nargs='?', const=0, type=int)
    args = parser.parse_args()

    if args.user_id:
        analysis_data = read_user_data(args.user_id)
        if args.save:
            save_analysis_data(args.user_id, analysis_data)
    else:
        # No arguments, read from standard input
        user_data = json.load(sys.stdin)
        analysis_data = analyze_user_data(user_data)

    if analysis_data:
        print(json.dumps(analysis_data))

if __name__ == "__main__":
    main()
