# Python backend boilerplate

Meant to be a bootstrap for setting up a micro backend without having to write all the tedious boilerplate.
To start a new project simply clone the code and save yourself time of setting basics every time.

## Requirements

This project is using pdm for dependency managment. To install pdm, run:

```commandline
pip install pdm
```

Then, to install dependencies run:

```commandline
make install
```

### Optional:

`pre-commit` can be configured to be used as commit hook. To install pre-commit, run:

```commandline
pip install pre-commit
```

Then, to initialize pre-commit for the repository, run:

```commandline
pre-commit install
```

## Running local backend

To run local backend execute:

```commandline
make up
```

Local backend can be verified by running:

```commandline
curl localhost:5000/hello
```

## Tech stack

- Flask
- Pytest
  - Pytest coverage
  - Pytest factoryboy
- Docker
  - Postgres database
