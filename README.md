# Python backend boilerplate

Meant to be a bootstrap for setting up a micro backend without having to write all the tedious boilerplate.

## Requirements

This project is using pdm for dependency managment. To install pdm, run:

```commandline
pip install pdm
```

Then, to install dependencies run:

```commandline
make install
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
