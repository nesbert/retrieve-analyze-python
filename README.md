# retrieve-analyze-python
 Retrieve and analyze user details from different API versions (uses [Go REST](https://gorest.co.in)). Goal of this project is to refresh myself with Python and create an AWS λ with this example.

 Learn by doing! :)

<!-- GETTING STARTED -->
## Getting Started

### Installation

```sh
python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

pip install -e .
```

<!-- USAGE EXAMPLES -->
## Usage

Here are a few ways to use this application.

### CLI Examples

```sh
# fetch user data from APIs and save to files './out/users/{user_id}'
retrieve {user_id}

# compare user data from saved to files './out/users/{user_id}' and create `analyze.json`
analyze {user_id}
```

<!-- ROADMAP -->
## Roadmap

- [x] Learn Python basics
- [ ] MVP
    - [x] Retrieve data
    - [x] Save data
    - [x] Analyze data
- [ ] Cloud Support
    - [ ] Create an AWS Lambda
    - [ ] Save data on AWS S3
- [ ] Developer Experience
    - [x] Setup repo structure
    - [ ] Environment and configuration properties
    - [ ] Add a unit test framework
    - [ ] Add linter support
    - [ ] Add a proper logger
- [ ] Learn advance Python
