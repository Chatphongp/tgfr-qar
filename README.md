# tgfr-qar

## Using Docker

### Prerequisite

- Install Docker

  - Ubuntu
    https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository
  - Mac & Windows
    https://docs.docker.com/get-docker/

- Install Docker Compose
  https://docs.docker.com/compose/install/

- Install make cmd
  - Ubuntu
    ```bash
    sudo apt-get install build-essential
    ```
  - Others
    ```bash
    not sure T-T
    ```

### Run server at port 9000

```bash
make reset
```

#### to inspect log of the docker

```bash
docker logs -f "docker_id"
```

### Run Tests

```bash
make tests
```

## Without Docker

### RUN at project folder /tgfr-qar

This will use a default file raw.dat as an input file.

```bash
python src/main.py
```

or for a specific file name. The file path is related to your current location.

```bash
python src/main.py ./data/raw.dat
```

### Prerequisites

```bash
pip install -r requirements.txt
```

You may need to create virtualenv first [virtualenv](https://docs.python-guide.org/dev/virtualenvs/) then

```bash
workon ...
```

before doing pip install

### Running tests

```bash
python -m unittest -b src/tests/*.py
```
