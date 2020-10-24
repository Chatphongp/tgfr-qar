# tgfr-qar

## RUN at project folder /tgfr-qar

This will use a default file raw.dat as an input file.

```bash
python src/main.py
```

or for a specific file name. The file path is related to your current location.

```bash
python src/main.py ./data/raw.dat
```

## Prerequisites

```bash
pip install -r requirements.txt
```

You may need to create virtualenv first [virtualenv](https://docs.python-guide.org/dev/virtualenvs/) then

```bash
workon ...
```

before doing pip install

## Running tests

```bash
python -m unittest -b tests/*.py
```
