# retrieve-analyze-python
 Retrieve and analyze user details from different API versions (uses [Go REST](https://gorest.co.in)). Goal of this project is to refresh myself with Python and create an AWS λ with this example.

 Learn by doing! :)

<!-- GETTING STARTED -->
## Getting Started

### Installation

```sh
# create virtual environment
python -m venv venv

# activiate virtual environment
source venv/bin/activate

# install virtual environment packages
pip install --upgrade pip
pip install poetry
```

### Project Dependencies

Use `poetry` to manage project package dependencies.

```sh
# install all required package dependencies
poetry install

# add a dependency
poetry add requests

# add a development dependency
poetry add --dev black

# remove a dependency
poetry remove requests

# update dependencies to latest
poetry update
```

### Code Quailty

Requires `dev` dependinces to be installed.

#### Testing

```sh
# run all tests
pytest -v

# run test a single method
pytest tests/gorest/test_users.py::test_fetch_all -v

# run test based on an expression
pytest -k "all or main" -v
```

#### Coverage Reporting
```sh
# run coverage analysis
coverage run -m pytest -v

# view coverage reports
coverage report
coverage html
```

#### Linting & Style Guide

```sh
# lint project files
pylint ./src/* ./tests/*

# format code with black
black src/retrieve_analyze/analyze.py # single file
black src/gorest/*.py # all files in directory
black src/**/*.py # all files in directory recursively
```

## Usage

Here are a few ways to use this application.

### CLI Examples

#### Project CLI Scripts

Requires venv to be active `source venv/bin/activate`.

```sh
# retrieve user data from APIs
retrieve {user_id}

# retrieve user data from APIs and save to files './out/users/{user_id}'
retrieve {user_id} --save 1

# analyze user data from saved to files './out/users/{user_id}'
analyze {user_id}

# analyze user and create `analysis.json`
analyze {user_id} --save 1

# retrieve & analyze user realtime from APIs
retrieve {user_id} | analyze

# test lambda handler locally
lambda-handler '{"id": 3186779}'
```

#### AWS Lambda Layer Creation

Starting from the project root.

```sh
# clean dist dir
rm -rfv dist/layer

# package project
pip install . -t dist/layer/python/lib/python3.10/site-packages

# zip layer
cd dist/layer
zip -r retrieve-analyze-python.zip *
```

#### Misc Helpers

```sh
# get a list of users for testing
curl -s "https://gorest.co.in/public/v2/users" | jq -r '.[] | [.id, .email] | @csv' > "./out/users/list-$(date +"%Y-%m-%dT%H%M").csv"
```


<!-- ROADMAP -->
## Roadmap

- [x] Learn Python basics
- [x] MVP
    - [x] Retrieve data
    - [x] Save data
    - [x] Analyze data
- [ ] Cloud Support
    - [x] Create an AWS Lambda
    - [x] Create an AWS Lambda Layer
    - [ ] Save data on AWS S3
    - [ ] Create AWS Step Functions (Distributed Maps)
- [ ] Developer Experience
    - [x] Setup repo structure
    - [ ] Environment and configuration properties
    - [ ] Add a unit test framework
    - [ ] Add linter support
    - [ ] Add a proper logger
- [ ] Learn advance Python
